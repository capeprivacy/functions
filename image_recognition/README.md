# Image Recognition

This application performs secure image recognition using a tflite model

## Usage

### Prepare deployment folder with dependencies
```
docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target ./deploy/
```

### Deploy and run with Cape
First deploy the model with:
```
cape deploy ./deploy

Deploying function to Cape ...
Function ID       ➜  <function ID>
Function Checksum ➜  <function checksum>
Function Name     ➜  <function name> 
```

Then invoke the model with:
```
cape run <your function id> -f cat.jpg 

('Image Label is :', 'Egyptian cat', ', with Accuracy :', 72.27, '%.')
```

```
cape run UCBjx2Q9j3sQb3f5ywJgZw -f coffee.jpg

('Image Label is :', 'espresso', ', with Accuracy :', 84.38, '%.')
```

```
cape run UCBjx2Q9j3sQb3f5ywJgZw -f lizzard.jpg

('Image Label is :', 'American chameleon', ', with Accuracy :', 69.14, '%.')
```