import os
import json

from pycape import Cape


auth_token_env = os.environ.get("TOKEN")
user_name_env = os.environ.get("USERNAME")

# Load your PDF
with open("Claude_Shannon.pdf", "rb") as f:
    pdf = f.read()

# Instantiate a Cape object with the URL "wss://xlarge.capeprivacy.com".
# Setting the URL to wss://xlarge.capeprivacy.com will guarantee the OCR model is
# deployed to larger instances with required dependencies.
cape = Cape(url="wss://xlarge.capeprivacy.com")

# Get a personal access token from the UI or the CLI with
# cape token create --name ocr
t = cape.token(auth_token_env)

# Retrieve your key with cape.key associated with your username.
# This key will be used to encrypt your data.
cape_key = cape.key(username=user_name_env)

# Encrypt your PDF with cape.encrypt using the retrieved key.
encrypted_pdf = cape.encrypt(pdf, key=cape_key)

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
