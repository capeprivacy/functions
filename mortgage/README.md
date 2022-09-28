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
Success! Deployed function to Cape
Function Id ➜ 47KVugdSrbeAJ3QPTfqhwS
Function Checksum ➜ c1ca2ce6057bc9b7ffc3903ddce2f3a3cb6b87fea47af8dd870d89623c7ba44e
```

```
cape run 47KVugdSrbeAJ3QPTfqhwS -f input.mortgage.json

Congratulations! You qualify for a mortgage.
```