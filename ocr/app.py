import os
import pathlib
import ocrmypdf
import sys


deploy_dir = os.environ.get("DEPLOY_DIR") or pathlib.Path(__file__).parent
sys.stdout = open('/dev/null', 'w')
def cape_handler(pdf_bytes: bytes):
    with open("my_file.pdf", "wb") as binary_file:
        binary_file.write(pdf_bytes)
    # doc = doctr.io.DocumentFile.from_pdf(pdf_bytes)
    ocrmypdf.ocr(input_file="my_file.pdf", output_file='-', output_type='none', sidecar='output.txt', force_ocr=True)
    with open("output.txt", "rb") as f:
        result = f.read()
        return result


if __name__ == "__main__":
    with open("your.pdf", "rb") as f:
        result = f.read()
        output = cape_handler(result)
        print(output)

