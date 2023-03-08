# Pendulum

In this example, we show how to run a function requiring a dependency. The function simply returns the current time based on a specific timezone using the [Pendulum](https://pendulum.eustace.io/) library. The dependency is listed in `requirements.txt`.

**Build the deployment package:**
```console
# Create a deployment folder
$ mkdir pendulum-deployment
# Copy the cape function (app.py) in the deployment folder
$ cp app.py pendulum-deployment/.
# Add pendulum as dependencies using docker
$ docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target pendulum-deployment/
```
**Deploy the function:**

Deploy with the CLI the function as follow:
```console
$ cape deploy pendulum-deployment/
Deploying function to Cape ...
Success! Deployed function to Cape.
Function ID       ➜  <FUNCTION_ID>
Function Checksum ➜  <FUNCTION_CHECKSUM>
Function Name     ➜  <FUNCTION_NAME>
```

**Run the function:**
You can run the function with the cli as follow. Just make sure to use the function id returned by `cape deploy`.
```console

cape run <FUNCTION_ID or FUNCTION_NAME> Europe/Paris 
```