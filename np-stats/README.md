### np-stats

A simple example with numpy dependencies and using [pycape](https://github.com/capeprivacy/pycape) and [serdio.lift_io](https://pydocs.capeprivacy.com/serdio.io_lifter.html#serdio.io_lifter.lift_io) to handle automatic serialization/deserialization of Cape function input/outputs. All commands are run from the repo root directory.

Note the `numpy_serde.py` helper, which defines a custom encoder/decoder bundle that allows `serdio` to handle numpy arrays.

**Build the deployment package:**

```bash
# Create a deployment folder
mkdir np-stats-deployment
# Copy the cape function (app.py) in the deployment folder
cp app.py numpy_serde.py np-stats-deployment/.
# Add serdio and numpy dependencies using docker
docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target np-stats-deployment/
```

**Deploy the function:**

Deploy with the CLI the function as follow:
```
cape deploy np-stats-deployment
export FUNCTION_ID=<function id from above>
```
Generate the function token based on the function ID and function checksum returned by deploy:
```
cape token create --name np-stats
export TOKEN=<token from above>
```

**Run the function:**
You can run the function with PyCape as follow:
```
python run.py
```