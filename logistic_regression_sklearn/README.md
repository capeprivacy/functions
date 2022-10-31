# Logistic Regression Training with Sklearn

This application securely trains and an Sklearn logistic regression model on the breast cancer dataset available at: https://archive.ics.uci.edu/ml/datasets/breast+cancer that predicts if a tumor is benign or malignant.

## Usage

### Prepare deployment folder with dependencies
```
sudo docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target ./app/
```

### Deploy and run with Cape
```
cape login

Your CLI confirmation code is: GZPN-KHMT
Visit this URL to complete the login process: https://login.capeprivacy.com/activate?user_code=GZPN-KHMT
Congratulations, you're all set!
```

```
cape deploy ./app

Deploying function to Cape ...
Success! Deployed function to Cape.
Function ID ➜  aMpFzfsfzM7CUtAtRyiKLA
Function Checksum ➜  a6b1a4e72804ad22d821bb7c89b4647c50920b8a3a4c7e8ecf14b05972215e4d
```

Train  logistic regression model on the breast cancer dataset.
```
cape run aMpFzfsfzM7CUtAtRyiKLA -f breast_cancer_data.csv --insecure -u https://k8s-cape-enclaver-750003af11-e3080498c852b366.elb.us-east-1.amazonaws.com

{'accuracy': 0.983957219251337, 'weights': [[-0.5634828454424664, -0.48968117436692676, -0.5277950966176833, -0.5814241972963736, -0.02288592679744086, 0.463860632669327, -0.8282900462209646, -0.8435707325454246, -0.03884918433068487, 0.6187809658667796, -1.0455764381611419, 0.35974835699506585, -0.6170693739746697, -0.9668590026888855, -0.3292909166850597, 0.6467698083688733, 0.09042092086623944, -0.35750055003409836, 0.27136532243728123, 0.6701363867829073, -0.8061574359542534, -1.3329147207091345, -0.654430417620746, -0.8479339690147301, -1.0087746783757932, 0.05189492319476721, -0.8625911548971675, -1.0343961479743573, -1.0175950492834187, -0.08501942035320843]], 'bias': [0.20440503950068414]}
```
