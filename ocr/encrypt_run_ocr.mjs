import {
    Cape
} from "@capeprivacy/cape-sdk";
import * as fs from "fs";
import * as crypto from "crypto";
import * as pkijs from "pkijs";


// If you run this script from a node environment
// set the engine to "nodeEngine"
const name = "nodeEngine";
pkijs.setEngine(
    name,
    new pkijs.CryptoEngine({
        name,
        crypto: crypto.webcrypto
    })
);

// Load your PDF
const pdf = fs.readFileSync("./Claude_Shannon.pdf");

// Get a personal access token from the UI or the CLI with
// cape token create --name ocr
const authToken = process.env.CAPE_AUTH_TOKEN;

// Instantiate a Cape object with your auth token and the URL 
// "wss://ocr.capeprivacy.com". Setting the URL to wss://ocr.capeprivacy.com"
// will guarantee the OCR model is deployed to larger instances with required 
// dependencies. 
const cape = new Cape({
    authToken,
    enclaveUrl: "wss://ocr.capeprivacy.com",
});

try {
    // Encrypt your PDF with cape.encrypt. When invoking this method, by default,
    // the SDK will retrieve the public encryption key associated with
    // your account
    const encryptedPdf = await cape.encrypt(pdf);

    // Invoke the OCR service on your encrypted PDF by setting the function ID to
    // "capedocs/ocr-doctr-onnx-1.0"
    const result = await cape.run({
        id: "capedocs/ocr-doctr-onnx-1.0",
        data: encryptedPdf,
    });

    // Print OCR transcript
    console.log(JSON.parse(result).ocr_transcript);

} catch (error) {
    console.error("Something went wrong", error);
}