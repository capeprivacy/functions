# Sentiment Analysis

This application performs secure sentiment analysis using a tflite model

## Usage

### Prepare deployment folder with dependencies
```
docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target ./deploy/
```

### Deploy and run with Cape

```
cape deploy ./deploy

Deploying function to Cape ...
Success! Deployed function to Cape
Function ID ➜ 8QoFCwrCu4sVd2wDAXxnbV
Function Hash ➜ f420da150d095b9a6151d34dec7b9483bd1e618d5d6ca0b20a6813189c10c45b
```

```
cape run 8QoFCwrCu4sVd2wDAXxnbV -f input.pos.data

('The sentiment is: ', 'positive', ' with a probability of ', 78.08290123939514, '%.')
```

```
cape run 8QoFCwrCu4sVd2wDAXxnbV -f input.neg.data

('The sentiment is: ', 'negative', ' with a probability of ', 86.57390475273132, '%.')
```