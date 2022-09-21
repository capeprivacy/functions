import json
import random
import socket
import time
from threading import Thread
import base64

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from pycape import Cape


class GossipNode:
    def __init__(self, port, connected_nodes, function_ref):
        # create a new socket instance
        # use SOCK_DGRAM to be able to send data without a connection
        # being established (connectionless protocol)
        self.node = socket.socket(type=socket.SOCK_DGRAM)

        # set the address, i.e(hostname and port) of the socket
        self.hostname = socket.gethostname()
        self.port = port
        self.function_ref = function_ref
        # bind the address to the socket created
        self.node.bind((self.hostname, self.port))

        # set the ports of the nodes connected to it as connected nodes
        self.connected_nodes = connected_nodes
        self.all_nodes = [self.port]
        self.received_votes = {}

        print("Node started on port {0}".format(self.port))
        print("Connected nodes =>", self.connected_nodes)
        # expect the public certificate is located under function folder
        public_key = RSA.importKey(open("function/public.pem").read())
        verifier = PKCS1_v1_5.new(public_key)

        self.verifier = verifier
        self.client = Cape()
        edges = {}
        edges["uuid"] = str(self.port)
        edges["generation"] =1
        edges["node_list"] = self.connected_nodes
        edge_info = json.dumps(edges)
        edge_info = bytes(edge_info, "utf8")
        encrypted = self.client.encrypt(input=edge_info)
        string_encoded_encrypted_edge_info = encrypted.decode('utf-8')
        print(f"encrypted value: {string_encoded_encrypted_edge_info}")
        self.iteration = 0
        self.received_votes[str(self.port)] = string_encoded_encrypted_edge_info
        self.start_threads()

    def input_message(self):
        while True:
            self.iteration += 1
            message_dict = {}
            message_dict["node"] = self.port
            message_dict["node_list"] = self.all_nodes
            message_dict["votes"] = self.received_votes
            message_to_send = json.dumps(message_dict)

            # Connect to the enclave function and send in the graph
            self.client.connect(self.function_ref)
            keys = self.received_votes.keys()
            for i in keys:
                # Get the message which has been formatted properly and turn it to bytes.
                graph_message=self.received_votes.get(i)
                enclave_message = json.dumps(graph_message)
                user_data = bytes(enclave_message, "utf8")
                print(f"sending data to enclave: {user_data}")
                result = self.client.invoke(user_data)
                print(f"sent encrypted graph message, got: {result}")

            result = self.client.invoke(b"get")
            self.client.close()
            print(f"current message result: {result.decode()}")
            send_to = self.connected_nodes.copy()
            print("sending message to peers now")
            self.transmit_message(message_to_send.encode("ascii"), send_to)
            print("my current votes", self.received_votes)
            time.sleep(20)

    def receive_message(self):
        while True:
            # since we are using connectionless protocol,
            # we will use 'recvfrom' to receive UDP message
            message_to_forward, address = self.node.recvfrom(1024)
            nodes = json.loads(message_to_forward)

            for i in nodes["node_list"]:
                if i not in self.all_nodes:
                    self.all_nodes.append(i)
            # remove the port(node), from which the message came from,
            to_send = self.connected_nodes.copy()

            print("received from", address[1])
            if address[1] in to_send:
                print("poisoned sender")
                to_send.remove(address[1])


            votes =  nodes["votes"]
            print("received votes", votes)
            keys = votes.keys()
            for i in keys:
                self.received_votes[i] = votes.get(i)
            # remove the port(node), from which the message came from,
            to_send = self.connected_nodes.copy()


            # sleep for 2 seconds in order to show difference in time
            time.sleep(2)

            # print message with the current time.
            # decode message so as to print it, as it was sent
            print(
                "\nMessage is: '{0}'.\nReceived at [{1}] from [{2}]\n".format(
                    message_to_forward.decode("ascii"),
                    time.ctime(time.time()),
                    address[1],
                )
            )

            # call send message to forward the message to other connected nodes
            self.transmit_message(message_to_forward, to_send)

    def transmit_message(self, message, to_send):
        print("sending to", to_send)
        # loop as long as there are connected nodes to send to
        while len(to_send) > 0:
            # select a random port from the list of connected nodes
            selected_port = random.choice(to_send)
            print("Connected nodes =>", to_send)
            print("Port selected is [{0}]".format(selected_port))

            # since we are using connectionless protocol,
            # we will use 'sendto' to transmit the UDP message
            self.node.sendto(message, (self.hostname, selected_port))
            to_send.remove(selected_port)

            print(
                "Message: '{0}' sent to [{1}].".format(
                    message.decode("ascii"), selected_port
                )
            )
            print("Connected nodes =>", self.connected_nodes)
            print("-" * 50)
            time.sleep(2)
            print("\n")

    def start_threads(self):
        # two threads for sending a gossip and receiving a gossip.
        Thread(target=self.input_message).start()
        Thread(target=self.receive_message).start()
