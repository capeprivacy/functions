# Mortgage Calculator

This application is a mortgage calculator that computes if an applicant is eligible for a mortgage
## Usage

### Deploy and run with Cape
```
cape login

Your CLI confirmation code is: PTHZ-WJFJ
Visit this URL to complete the login process: https://login.capeprivacy.com/activate?user_code=PTHZ-WJFJ
Congratulations, you're all set!
```

```
cape deploy ./app

Deploying function to Cape ...
Function ID       ➜  <function ID>
Function Checksum ➜  <function checksum>
Function Name     ➜  <function name> 
```

```
cape run <Function id or checksum> -f input.mortgage.json

Congratulations! You qualify for a mortgage.
```