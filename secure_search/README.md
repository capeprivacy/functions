# Secure Search

Simulates a cybersecurity search function, where the IP addresses you are interested in need to remain private but the data/logs you are searching might be public. The function defines selectors (IP addresses of interest) as variables:
```python
selectors_a = "172.19.0.4"
selectors_b = "1.2.3.4"
```
and accepts a list of json objects containing IP addresses in a "hosts" element:
```json
[{"protocol": "tcp", "hosts": "1.2.3.4", "state": "ESTABLISHED"}, {...}]
```
It will return True or False for each selector that you are interested in, for each object in the json list:
```json
[{"172.19.0.4": false, "1.2.3.4": true}, {...}]
```
It uses a user-supplied public key to encrypt the results within the enclave prior to returning them to the caller. Please see:
* `./test/generate_keys.py`: for how to generate a keypair.
* `./test/test_cape.py`: a sample pycape client which calls the function, receives an encrypted response, and performs decryption using the private key.

```
cape deploy ../secure_search
```