# Logistic Regression Training

This application securely trains and a logistic regression model on the breast cancer dataset available at: https://archive.ics.uci that predicts if a tumor is benign or malignant.

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
Success! Deployed function to Cape
Function Checksum ➜ 348ea2008f014b4d62562b4256bf2ddbbebcbd8b958981de5c2e01a973f690f8
Function Id ➜ 5wggR4ZaEBdfHQSbV2RcN5
```

Train  logistic regression model on the breast cancer dataset.
```
cape run 5wggR4ZaEBdfHQSbV2RcN5 -f breast_cancer_data.csv

{'accuracy': 0.9197860962566845, 'weights': [10256.691270418847, 19071.613672774896, 63157.95554188486, 97842.31573298419, 106.154850842932, 43.29810217015701, -44.1862890971466, -22.519840356544492, 198.12010662303672, 78.6238754895288, 48.39822623036688, 1508.6634081937177, 342.695612801048, -22814.6600120419, 8.905474463874354, 16.958969184554977, 18.625567417774857, 7.857666827748692, 25.00139435235602, 4.305377619109947, 9667.094831413606, 24077.953801047104, 59698.82218324606, -91019.69570680606, 137.85512994764406, 64.23315269371734, -35.801829085602265, 1.0606119748691598, 287.2889897905756, 89.52499975392664], 'bias': 3.247905759162303}
```
