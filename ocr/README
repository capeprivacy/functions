# Invoke Cape's Confidential OCR Service from SDKs

This folder shows you how you can run the [Cape's confidential optical character recognition service](https://docs.capeprivacy.com/cape-hosted/ocr)) from the SDKs: [cape-js](https://docs.capeprivacy.com/sdks/javascript-sdk) and [pycape](https://pydocs.capeprivacy.com/).

Before invoking the OCR service from one of the SDKs, you must [sign up](https://docs.capeprivacy.com/getting-started#sign-up-for-cape) with Cape and generate a [personal access token](https://docs.capeprivacy.com/reference/user-tokens).

For this example, we will run the OCR on the PDF `claude_shannon.pdf`.

## From cape-js

Before invoking the OCR, set the environment variable `CAPE_AUTH_TOKEN` to your [personal access token](https://docs.capeprivacy.com/reference/user-tokens). 
```
export CAPE_AUTH_TOKEN="your cape auth token"
```

To run the OCR from cape-js on the PDF, run:
```
node run_ocr.mjs
```

To encrypt the PDF with [cape.encrypt](https://docs.capeprivacy.com/tutorials/encrypting#cape-encrypt), then invoke the OCR on the encrypted PDF, run:
```
node encrypt_run_ocr.mjs
```

## From pycape

Before invoking the OCR, set the environment variable `CAPE_AUTH_TOKEN` to your [personal access token](https://docs.capeprivacy.com/reference/user-tokens). 

```
export CAPE_AUTH_TOKEN="your cape auth token"
```

To run the OCR from pycape on the PDF, run:
```
python run_ocr.py
```

To encrypt the PDF with [cape.encrypt](https://docs.capeprivacy.com/tutorials/encrypting#cape-encrypt), then invoke the OCR on the encrypted PDF, run:
```
python encrypt_run_ocr.py
```