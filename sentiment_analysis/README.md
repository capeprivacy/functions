# Sentiment Analysis

This application performs secure sentiment analysis using a tflite model

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
Your access token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVkb21jZkdEejZKVGNId2k5a29WZSJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmNhcGVwcml2YWN5LmNvbS8iLCJzdWIiOiJnaXRodWJ8MjYzNjgyNDkiLCJhdWQiOlsiaHR0cHM6Ly9hcHAuY2FwZXByaXZhY3kuY29tL3YxLyIsImh0dHBzOi8vcHJvZC1jYXBlLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjMwMDQzNTEsImV4cCI6MTY2NTU5NjM1MSwiYXpwIjoib1hJVHhwQ2RqdlJZU0RKdGFNZXljdnZlcUU5cWFkVVMiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIn0.UpH_u4CMULMeeD1-5WgMWM7scPdNI8Q4oIVZQTnCy8-21aHcO2U9cz1QD939Glt5Zgmcrjb5W0FyMml9OBpcS7eN6ecmLAAJbC8G-XkyTj8y2tlLasscO65DKBb4jFLQaZxpiErUDZQJBdpkH7isRK3Ii5LV_n5ranJEhIR7Q79uwBwiJAWHAr70PM5p62-Yx5dGTn43bOcJtW7ZNfuymKitsn-dkFKunOKjIhb_XQ91YSym2_NWEu3uRWXMeaDsOrY4Q-E3LdS1IH1okRpVMraEJYdmE48aqB5lRBhU8EjhMtRiWrG5ip7FI_XLW-RR9ITcWXPPj0vFBqbNQB27kA 
```

```
cape deploy ./app

Deploying function to Cape ...
Success! Deployed function to Cape
Function ID ➜ 6YQzxVnaoCAaQ3aruwGKvS
Function Hash ➜ 2561178ff5125454f54391d3869fcaa4e46af77dee4a6c0d8fb370f429dd849c
```

```
cape run 6YQzxVnaoCAaQ3aruwGKvS -f input.pos.data

('The sentiment is: ', 'positive', ' with a probability of ', 78.08290123939514, '%.')
```

```
cape run 6YQzxVnaoCAaQ3aruwGKvS -f input.neg.data

('The sentiment is: ', 'negative', ' with a probability of ', 86.57390475273132, '%.')
```