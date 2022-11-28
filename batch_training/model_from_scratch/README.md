# Batch training

This readme describes how to perform batch training on a logistic regression model created from scratch 

## How to perform batch training with Cape

### Prepare deployment folder with dependencies
Create a depoyment folder called `app`:
```
mkdir app
```
Save app.py into the folder:
```
cp app.py ./app
```
Save untrained model into the folder:
```
cp params.json ./app
```
Install necessary libraries listed in `requirements.txt`
```
sudo docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target ./app/
```

### Login and deploy with Cape
```
cape login

Your CLI confirmation code is: GQDK-SNHL
Visit this URL to complete the login process: https://login.capeprivacy.com/activate?user_code=GQDK-SNHL
Congratulations, you're all set!
```

```
cape deploy ./app

Deploying function to Cape ...
Success! Deployed function to Cape
Function ID ➜ 8QoFCwrCu4sVd2wDAXxnbV
Function Hash ➜ f420da150d095b9a6151d34dec7b9483bd1e618d5d6ca0b20a6813189c10c45b
```

### Generate token

```
cape token <FUNCTION_ID> --function-checksum <FUNCTION_CHECKSUM> -o json > app_token.json
```

The file `app_token.json` will be used to create a function reference `pycape.FunctionRef` for estabilishing a connection with the enclave.

### Invoke the deployed Cape function from PyCape
```
python3 invoke_app.py
```
This script will invoke the Cape function repeatedly to train the model batch by batch. After training is completed, the model is printed out as a json file.