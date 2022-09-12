# Image Recognition

This application performs secure image recognition using a tflite model

## Usage

### Prepare deployment folder with dependencies
```
sudo docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target ./deploy/
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
cape deploy ./deploy

Deploying function to Cape ...
Success! Deployed function to Cape
Function ID ➜ UCBjx2Q9j3sQb3f5ywJgZw
Function Hash ➜ 00f617b57eebfaa29b7f091b3dab104fc690b2173d0de8fa46dc5d426bf6a2e1
```

```
cape run UCBjx2Q9j3sQb3f5ywJgZw -f cat.jpg 

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