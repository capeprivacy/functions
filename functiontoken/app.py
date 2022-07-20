import os
from dotenv import load_dotenv
import jwt

def validate_function_token(token):
    decoded = jwt.decode(token, os.getenv('CAPE_FUNCTION_TOKEN_PUBLIC_KEY'), algorithms=["RS256"])
    return decoded['sub'] == os.getenv('CAPE_FUNCTION_ID')

def cape_handler(n):
    load_dotenv()
    valid_token = validate_function_token(n)

    if valid_token:
        return "Authorization success."
    else:
        return "Token is invalid."
