# Leader election using enclaves
The premise of this repo is to set up a network of python nodes that will ask the enclave to run the leader election algorithm for them. 

# Setup
## Fetch dependencies for function
Fetch depdencies before deploy:
```
pip install -r function/requirements.txt --target function/
```

You would first have to deploy the function: 
```
cape deploy function/ --url "wss://hackathon.capeprivacy.com"
```

Then update the function hash and function id with when starting up the nodes.

Generate the crypto content (in python) and run:
``` python
key = RSA.generate(2048)
private_key_bytes = key.export_key('PEM')
public_key_bytes = key.publickey().exportKey('PEM')


with open("private.pem", "wb") as f:
    f.write(private_key_bytes)
with open("public.pem", "wb") as f:
    f.write(public_key_bytes)
```
Begin a list of python nodes which are identified by IP and port number. 
```
python start_node.py -p 5000 -n 5001 -f `<FUNCTION_ID>` -fh `<FUNCTION_HASH>`
python start_node.py -p 5001 -n 5000 -f `<FUNCTION_ID>` -fh `<FUNCTION_HASH>`
```

# The algorithm
Typically leader election requires nodes to behave properly when transmitting messages so that each node 
executes the proper logic. Instead of relying on each node deciding who the leader is, we now leverage
the enclave for this gurantee.

A simple example would be for `node A` to gossip and update the list of active nodes it knows. 
It would send this data encrypted with the enclave's public key to make sure only the enclave can decrypt the message (not implemented)
Next the enclave would sign the result and would return both the signature and orginal value. 

This new value is now trusted to be true given the list of nodes available. 
This gurantees that if the list of active nodes matches, then the leader is deterministic.

## Byzantine fault tolerance
What if a node sends an arbitrary list of nodes? 
All good behaving nodes would know that the list of nodes in the signed result doesn't match the list of
active nodes, and would not respect the leader elected in that case.

Health checks, network coalescence are omitted from the current code for simplicity purposes.

The limit for Byzantine fault tolerance is less than half of the node pool. In the case that the number of 
malicious nodes exceeds half, then it becomes impossible for a correct node to identify another correct node.

## Changes from last time
* Way better reliability
* Used Pycape this time
* Focus on the availability and guranteed execution of the program instead of data sensitivity

Feedback: 
Should only initiate one Cape instance, don't do it in a thread, probably should be documented somewhere

## Want: 
If enclave can maintain some form of state of nodes
then this would be way more impressive. Next steps would be to figure out the best way of integrating 
state via part of the data.

## Achieving state of nodes via using Cape encrypt
Just having gossip regarding node information is not enough, we want an algorithm which is tamper-proof. 



## Example
Total number of nodes in system : 4 

Each node and their view of the system: 
Node 1: [1, 2, 3, 4] -> [1, 2, 3, 4]

Node 2: [2, 3, 4] -> [1, 2, 3, 4]

Node 3: [2, 3, 4] -> [1, 2, 3, 4]

Node 4: [1, 4] -> [1, 2, 3, 4]


Each node encrypts their view and send it 

After one round of gossip

Node 1: [1: [1, 2, 3, 4], 2: [2, 3, 4], 3: [2, 3, 4], 4: [1, 4]]

Node 2: [2: [2, 3, 4], 3: [2, 3, 4], 4: [1, 4]]

Node 3: [2: [2, 3, 4], 3: [2, 3, 4], 4: [1, 4]]

Node 4: [1: [1, 2, 3, 4], 4: [1, 4]]

You still need to collect all paths in the system, still keep track of all the votes, you send the encrypted votes one at a time to cape to build a graph, so then
the message can be sent to this cape function to determine how the message will be routed, only Cape will have the entire view of the network. 


Now after you build up the state, you can aggregate the result and perform an action: like sending a message from note 1 to 2.

To run :
```
python start_node.py -p 5000 -n 5001 -f nVs2viSCs9YuUDLXgyiYRK -fh 513466258213de9c01667e4f4fd224a2fb7166f05499b0db71b5cf7758d22410
```

## The goods
We found a way to circumvent not having mixed inputs
We found a way to persist some state using multi invocation
Cape encrypt works great


## The bads
Some weird error with bad URL using pycape


