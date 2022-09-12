import numpy as np
from tflite_runtime.interpreter import Interpreter

def load_labels(path): # Read the labels from the text file as a Python list.
  with open(path, 'r') as f:
    return [line.strip() for i, line in enumerate(f.readlines())]

labels = load_labels('./labels.txt')

def load_vocab(path): # Read the labels from the text file as a Python list.
    vocabulary = {}
    with open(path, 'r') as f:
        for i, line in enumerate(f.readlines()):
            item = line.strip().split(' ')
            word = item[0]
            encoding = int(item[1])
            vocabulary[word] = encoding
    return vocabulary
    
vocabulary = load_vocab('./vocab.txt')

def vectorize_text(text, vocabulary, input_shape):
    encoded_text = []
    text = text.split(' ')
    for word in text:
        word_encoding = vocabulary[word]
        encoded_text.append(word_encoding)
    encoded_text = np.array(encoded_text, dtype=np.int32)
    encoded_text = np.pad(encoded_text, (0, input_shape[1] - len(encoded_text)), 'constant')
    encoded_text = np.reshape(encoded_text, (input_shape[0], input_shape[1]))
    return encoded_text

def cape_handler(text):
    text = text.decode("utf-8")
    # Load the TFLite model and allocate tensors.
    interpreter = Interpreter(model_path="./model.tflite")
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Predict
    input_shape = input_details[0]['shape']
    input_data = vectorize_text(text=text, vocabulary=vocabulary, input_shape=input_shape)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    output_result = np.argmax(output_data)
    # prob_negative = output_data[0] * 100
    # prob_positive = output_data[1] * 100
    if output_result == 1:
        result = "positive"
    else:
        result = "negative"
    return ("The sentiment is: ", result, " with a probability of ",  output_data[0][output_result] * 100, "%.")