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

Then update the function hash and function id with the output in gossip_protocol.py file.

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
It would send this data encrypted with the enclave's public key to make sure only the enclave can decrypt the message (did not get to)
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
You would get a trusted service with high availability to track alive nodes.


