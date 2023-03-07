# Cape Functions

## Getting Started

To run these functions with Cape, you need to first install the [Cape CLI](https://docs.capeprivacy.com/getting-started#install-the-cape-cli). Then you will have to sign up from [Cape's website](https://capeprivacy.com/) or using the CLI:
```
cape signup
``` 

These examples can be also executed from Cape's SDKs: [cape-js](https://docs.capeprivacy.com/sdks/javascript-sdk) and [pycape](https://pydocs.capeprivacy.com/). If you execute these functions from one of the SDK, you will have to generate a [personal access token](https://docs.capeprivacy.com/reference/user-tokens). This can be done from [Cape's website](https://capeprivacy.com/) or from the CLI:
```
cape token create --name my-token --description 'for use in the javascript sdk'
```

## Examples

### Echo

A simple function that returns whatever you send it. Check out the folder [echo](.echo/) to learn how to deploy this function. To invoke this function, you can run the following:

```
cape run capedocs/echo -f echo/input.echo.data
```

### Isprime

A simple function checking if your number is prime or not. Checkout the folder [isprime](.isprime/) to learn how to deploy this function. To invoke this function, you can run the following:

```
cape run capedocs/isprime -f isprime/input.isprime.data
```

### Pendulum
In this example, we show how to run a function requiring a dependency. The function simply returns the current time based on a specific timezone using the [Pendulum](https://pendulum.eustace.io/) library. To learn how to deploy this function, checkout the folder [pendulum](./pendulum/). To invoke the function, invoke:

```
cape run capedocs/pendulum Europe/Paris 
```

### Numpy Stats
A simple example with numpy dependencies and using [pycape](https://github.com/capeprivacy/pycape) and [serdio.lift_io](https://pydocs.capeprivacy.com/serdio.io_lifter.html#serdio.io_lifter.lift_io) to handle automatic serialization/deserialization of Cape function input/outputs. You can learn how to deploy this function by checking the folder [np-stats](./np-stats/). You can run the function as follow after install installing in a virtual environment in `np-stats/requirements.txt`:

```
export TOKEN=<YOUR TOKEN>
export FUNCTION_ID=capedocs/np-stats
python np-stats/run.py
```

### Secure Search
Simulates a cybersecurity search function, where the IP addresses you are interested in need to remain private but the data/logs you are searching might be public. You can learn more about this function by checking the folder [secure-search](./secure_search/).

```
cape run capedocs/secure-search  -f secure_search/input.search.data
```

### Leader Election
Demos how a secure trusted execution environment like Cape can be leveraged in consensus in order to guarantee fairness. Details on how to run this example can be found
[here](./leader-election).


### Hide-and-seek
To learn more about the confidential hide-and-seek example, you can check the folder [hide_and_seek](./hide_and_seek).


### Mortgage
This application is a mortgage calculator that computes if an applicant is eligible for a mortgage. To learn how to deploy this application, you can check out the folder (mortgage)[./mortgage]. To call this function, you can run:
```
cape run capedocs/mortgage -f mortgage/input.mortgage.json
```

## Machine Learning examples

### Image Classification Inference with ONNX

To learn how you can deploy and invoke an image classification model using the [onnxruntime](https://onnxruntime.ai/), you can check the [capeprivacy/image-classification-onnx](image-classification-onnxhttps://github.com/capeprivacy/image-classification-onnx) repository.


### Image Classification with tflite
This example demonstrates how you can deploy and invoke an image classification model with [tflite](https://www.tensorflow.org/lite). To learn how to deploy this application, you can checkout the folder [image-classification](./image_recognition). To invoke the model, simply run:

```
cape run capedocs/image-recognition -f image_recognition/coffee.jpg

('Image Label is :', 'espresso', ', with Accuracy :', 84.38, '%.')
```

### Sentiment analysis with tflite
This example demonstrates how you can deploy and invoke a sentiment analysis model with [tflite](https://www.tensorflow.org/lite). To learn how to deploy this application, you can checkout the folder [sentiment_analysis](./sentiment_analysis). To invoke the model, simply run:

```
cape run capedocs/sentiment-analysis -f sentiment_analysis/input.pos.data

('The sentiment is: ', 'positive', ' with a probability of ', 78.08290123939514, '%.')
```

### Training and Inference with Scikit-Learn.
You can check the following examples to learn about how to deploying and invoke machine learning models with Scikit-Learn:
- [credit_card_fraud_detection](./credit_card_fraud_detection/): performs secure inference to classify credit card transactions as fraudulent or legitimate.
- [logistic_regression_sklearn](./logistic_regression_sklearn/): securely train an Sklearn logistic regression model on the breast cancer dataset.
- [batch_training](./batch_training/): shows how to perform batch training with Sklearn model.

 