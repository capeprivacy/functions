from argparse import ArgumentParser

from gossip import GossipNode
from pycape import FunctionRef
# port = 5000
# # ports for the nodes connected to this node
# connected_nodes = [5010, 5020]

# node = GossipNode(port, connected_nodes)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", type=int, help="port")
    parser.add_argument("-f", type=str, help="function_id")
    parser.add_argument("-fh", type=str, help="function_hash")
    parser.add_argument("-n", "--node-list", nargs="+", default=[])
    args = vars(parser.parse_args())
    print(args)
    node = GossipNode(args["p"], 
                      connected_nodes = list(map(int, args["node_list"])),
                      function_ref=FunctionRef(function_id=args["f"],
                                               function_hash=args["fh"]))
