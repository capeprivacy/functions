from tflite_runtime.interpreter import Interpreter
from PIL import Image
import numpy as np
import time
import io


def load_labels(path):  # Read the labels from the text file as a Python list.
    with open(path, "r") as f:
        return [line.strip() for i, line in enumerate(f.readlines())]


def set_input_tensor(interpreter, image):
    tensor_index = interpreter.get_input_details()[0]["index"]
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image


def classify_image(interpreter, image, top_k=1):
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    output_details = interpreter.get_output_details()[0]
    output = np.squeeze(interpreter.get_tensor(output_details["index"]))
    scale, zero_point = output_details["quantization"]
    output = scale * (output - zero_point)
    ordered = np.argpartition(-output, 1)
    return [(i, output[i]) for i in ordered[:top_k]][0]


def cape_handler(image_bytes):
    data_folder = "./"

    model_path = data_folder + "model.tflite"
    label_path = data_folder + "labels.txt"

    interpreter = Interpreter(model_path)

    interpreter.allocate_tensors()
    _, height, width, _ = interpreter.get_input_details()[0]["shape"]

    # Load an image to be classified.
    image = Image.open(io.BytesIO(image_bytes))
    image.save(data_folder + "img.jpg")
    image = Image.open(data_folder + "img.jpg").convert("RGB").resize((width, height))

    # Classify the image.
    label_id, prob = classify_image(interpreter, image)

    # Read class labels.
    labels = load_labels(label_path)

    # Return the classification label of the image.
    classification_label = labels[label_id]
    return (
        "Image Label is :",
        classification_label,
        ", with Accuracy :",
        np.round(prob * 100, 2),
        "%.",
    )
