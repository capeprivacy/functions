# Cape Functions

## Getting Started

To run these functions with Cape, you need to first install the [Cape CLI](https://github.com/capeprivacy/cli).

### Cape login

Log into Cape by running:
```
cape login
```

### Cape Deploy

Deploys a `function_dir` to Cape. Returns a `function_id`.

```
cape deploy <function_dir>
```

Example:
```
cape deploy echo
```

#### Deploying on Windows

If you are on Windows (or as an alternative to deploying the function as a directory) you can create a zip file and deploy it directly. This will fix issues you may run into with relative paths.

```
cape deploy <function_name>.zip
```

### Cape Run

Runs a cape function by `function_id` and `input_file`. Returns a `result`.

```
cape run <function_id> <input_file>
```

## Examples

### echo

A simple function that returns whatever you send it.

```
cape deploy echo
```

```
cape run 4b4961ef-1f04-4027-850a-3fd39a9501f2 -f input.echo.data
```

### isprime

```
cape deploy isprime
```

```
cape run 28028ae0-cf5c-47f8-8e8e-0da42b6dc142 -f input.isprime.data
```

### np-stats
A simple example with numpy dependencies and `pycape.io_serialize` decorator to deserialize/serialize the input and output of a cape function.

In the instruction below we add the PyCape depedency by cloning it which is really ugly, but in bad we should simplify the process by having PyCape
already installed in the EIF. Also releasing PyCape on PyPI should improve the process.

**Build the deployment package:**

```
$ mkdir np-stats-deployment
$ cp np-stats/app.py np-stats-deployment/.
$ # Clone pycape to add it as dependency (very ugly) until PyCape is released on pypi or pre-install in the EIF.
$ git clone https://github.com/capeprivacy/pycape.git
$ cp -r pycape/pycape np-stats-deployment/
$ # Install dependencies using docker
$ docker run -v `pwd`:/build --rm -it --entrypoint /bin/bash python:3.9-slim-bullseye
$ cd /build/
$ # Add example dependencies
$ pip install -r np-stats/requirements.txt --target np-stats-deployment/
$ # Add PyCape dependencies
$ pip install -r pycape/requirements.txt --target np-stats-deployment/
```

**Deploy the function:**

Deploy with the CLI the function as follow:
```
cape deploy np-stats-deployment --url wss://hackathon.capeprivacy.com --insecure
```

**Run the function:**
You can run the function  with PyCape as follow:
```
export CAPE_FUNCTION="<YOUR FUNCTION ID>"
python np-stats/run.py
```
