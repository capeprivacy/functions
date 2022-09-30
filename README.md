# Cape Functions

## Getting Started

To run these functions with Cape, you need to first install the [Cape CLI](https://github.com/capeprivacy/cli).

### Cape Login

Log in to Cape by running:
```
cape login
```

### Cape Deploy

Deploys your function and any dependencies within a `function_dir` to Cape. Returns a `function_id`:

```
cape deploy <function_dir>
```

For example, if your function code was within a folder named `echo`:
```
cape deploy echo
```

#### Deploying on Windows

If you are on Windows (or as an alternative to deploying the function as a directory) you can create a zip file and deploy it directly. This will fix issues you may run into with relative paths:

```
cape deploy <function_name>.zip
```

### Cape Run

Runs a cape function by `function_id` and takes `input_data`. Returns the result of the function:

```
cape run <function_id> <input_data>
```

to pass `input_data` as a file, use `-f`:
```
cape run <function_id> -f <input_file>
```


## Examples

### echo

A simple function that returns whatever you send it.

```
cape deploy echo
```

```
cape run <YOUR_FUNCTION_ID> -f input.echo.data
```

### isprime

```
cape deploy isprime
```

```
cape run <YOUR_FUNCTION_ID> -f input.isprime.data
```

### mobilenet

```
cape deploy mobilenet
```

```
cape run <YOUR_FUNCTION_ID> -f input.dog_segmentation.bmp
```

### pendulum
In this example, we show how to run a function requiring a dependency. The function simply returns the current time based on a specific timezone using the [Pendulum](https://pendulum.eustace.io/) library. The dependency is listed in `pendulum/requirements.txt`.

**Build the deployment package:**
```
# Create a deployment folder
mkdir pendulum-deployment
# Copy the cape function in the deployment folder
cp pendulum/app.py pendulum-deployment/.
# Add pendulum as dependencies using docker
docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r pendulum/requirements.txt --target pendulum-deployment/
```
**Deploy the function:**

Deploy with the CLI the function as follow:
```bash
cape deploy pendulum-deployment/
```

**Run the function:**
You can run the function with the cli as follow. Just make sure to use the function id returned by `cape deploy`.
```
cape run <YOUR_FUNCTION_ID> Europe/Paris 
```

### np-stats
A simple example with numpy dependencies and using [pycape](https://github.com/capeprivacy/pycape) and [serdio.lift_io](https://github.com/capeprivacy/pycape/tree/main/serdio) to handle automatic serialization/deserialization of Cape function input/outputs. All commands are run from the repo root directory.

Note the `numpy_serde.py` helper, which defines a custom encoder/decoder bundle that allows `serdio` to handle numpy arrays.

**Build the deployment package:**

```bash
mkdir np-stats/np-stats-deployment
cp np-stats/app.py np-stats/numpy_serde.py np-stats/np-stats-deployment/.
# Add serdio and numpy dependencies using docker
docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r np-stats/requirements.txt --target np-stats/np-stats-deployment/
```

**Deploy the function:**

Deploy with the CLI the function as follow:
```
cape deploy np-stats/np-stats-deployment
```
Generate the function token based on the function ID and function checksum returned by deploy:
```
cape token <FUNCTION_ID> --function-checksum <FUNCTION _CHECKSUM> o json >  np-stats/numpy_token.json
```

**Run the function:**
You can run the function with PyCape as follow:
```
export TOKEN_FILE=np-stats/numpy_token.json
python np-stats/run.py
```

### secure_search

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
* `secure_search/test/generate_keys.py`: for how to generate a keypair.
* `secure_search/test/test_cape.py`: a sample pycape client which calls the function, receives an encrypted response, and performs decryption using the private key.

```
cape deploy secure_search
```

```
cape run <YOUR_FUNCTION_ID> -f input.search.data
```
