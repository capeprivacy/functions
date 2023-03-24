import os
import json

from pycape import Cape


auth_token_env = os.environ.get("CAPE_AUTH_TOKEN")
user_name_env = os.environ.get("USERNAME")

# Load your PDF
with open("Claude_Shannon.pdf", "rb") as f:
    pdf = f.read()

# Instantiate a Cape object with the URL "wss://ocr.capeprivacy.com".
# Setting the URL to "wss://ocr.capeprivacy.com" will guarantee the OCR model is
# deployed to larger instances with required dependencies.
cape = Cape(url="wss://ocr.capeprivacy.com")

# Get a personal access token from the UI or the CLI with
# cape token create --name ocr
t = cape.token(auth_token_env)

# Encrypt your PDF with cape.encrypt. When invoking this method, by default,
# the SDK will retrieve the public encryption key associated with
# your account
encrypted_pdf = cape.encrypt(pdf)

# Select the Cape function you would like to invoke.
# Since we want invoke the ocr service, set the function ID
# to "capedocs/ocr-doctr-onnx-1.0"
f = cape.function("capedocs/ocr-doctr-onnx-1.0")

# Invoke the OCR service
result = cape.run(f, t, encrypted_pdf)

# Print the transcript
print(f"OCR transcript: {json.loads(result)['ocr_transcript']}")

# Print the bounding boxes
print(f"OCR records: {json.loads(result)['ocr_records']}")
