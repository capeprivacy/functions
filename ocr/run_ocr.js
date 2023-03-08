const { Cape } = require("@capeprivacy/cape-sdk");
import * as fs from 'fs';

// Load PDF
const pdf = fs.readFileSync('Claude_Shannon.pdf');

// Get a personal access token from the UI or the CLI with 
// cape token create --name ocr
const authToken = "";

//  Instantiate a Cape object with your auth token and the URL "wss://xlarge.capeprivacy.com"
const cape = new Cape({ authToken, enclaveUrl: "wss://xlarge.capeprivacy.com"});


// Encrypt your PDF with cape.encrypt using the retrieved key.
const encrypted_pdf = cape.encrypt(pdf)

// Invoke the OCR service on your encrypted PDF by setting the function ID to 
// "capedocs/ocr-doctr-onnx-1.0"
const result = cape.run({ id:"capedocs/ocr-doctr-onnx-1.0", data: pdf });
