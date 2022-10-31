# Credit Card Fraud Detection: Random Forest Clasifier Inference with Sklearn

This application performs secure inference to classify credit card transactions as fraudulent or legitimate.
The model is trained with `train_model.py`, which uses `Sklearn` random forest classifier.

## Usage

### Prepare deployment folder with dependencies
```
sudo docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target ./app/
```

### Deploy and run with Cape
```
cape login

Your CLI confirmation code is: BZCS-NLTD
Visit this URL to complete the login process: https://login.capeprivacy.com/activate?user_code=BZCS-NLTD
Congratulations, you're all set!
```

```
cape deploy ./app

Deploying function to Cape ...
Success! Deployed function to Cape.
Function ID ➜  huM9vYySCV62Ln98wYiUfD
Function Checksum ➜  0d5c578b20f9fcfec77fcc2d950eacbf267a4401694b93a9af1c1ca7d347aa01
```

```
cape run huM9vYySCV62Ln98wYiUfD -f fraudulent_transaction.csv --insecure -u https://k8s-cape-enclaver-750003af11-e3080498c852b366.elb.us-east-1.amazonaws.com

This credit card transaction is fraudulent
```

```
cape run huM9vYySCV62Ln98wYiUfD -f legitimate_transaction.csv --insecure -u https://k8s-cape-enclaver-750003af11-e3080498c852b366.elb.us-east-1.amazonaws.com

This credit card transaction is legitimate
```