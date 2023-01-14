import io
import ocrmypdf
import sys


sys.stdout = open('/dev/null', 'w')
def cape_handler(pdf_bytes: bytes):
    pdf = io.BytesIO(pdf_bytes)    
    ocrmypdf.ocr(input_file=pdf, output_file='-', output_type='none', sidecar='output.txt', force_ocr=True)
    with open("output.txt", "rb") as f:
        result = f.read()
        return result


if __name__ == "__main__":
    with open("your.pdf", "rb") as f:
        result = f.read()
        output = cape_handler(result)
        print(output)

