# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""label_image for tflite."""

import argparse
import time

import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite
from io import BytesIO

def load_labels(filename):
  with open(filename, 'r') as f:
    return [line.strip() for line in f.readlines()]

def run_inference(img):
  model_file = "mobilenet_v1_1.0_224.tflite"
  label_file = "labels.txt"

  ext_delegate = None
  num_threads = None
  input_mean = 127.5
  input_std = 127.5

  interpreter = tflite.Interpreter(
      model_path=model_file,
      experimental_delegates=ext_delegate,
      num_threads=num_threads)
  interpreter.allocate_tensors()

  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  # check the type of the input tensor
  floating_model = input_details[0]['dtype'] == np.float32

  # NxHxWxC, H:1, W:2
  height = input_details[0]['shape'][1]
  width = input_details[0]['shape'][2]
  img = img.resize((width, height))

  # add N dim
  input_data = np.expand_dims(img, axis=0)

  if floating_model:
    input_data = (np.float32(input_data) - input_mean) / input_std

  interpreter.set_tensor(input_details[0]['index'], input_data)

  start_time = time.time()
  interpreter.invoke()
  stop_time = time.time()

  output_data = interpreter.get_tensor(output_details[0]['index'])
  results = np.squeeze(output_data)

  top_k = results.argsort()[-5:][::-1]
  labels = load_labels(label_file)
  #for i in top_k:
    #print("i", i)
    #if floating_model:
      #print('{:08.6f}: {}'.format(float(results[i]), labels[i]))
    #lse:
      #print('{:08.6f}: {}'.format(float(results[i] / 255.0), labels[i]))

  #print('time: {:.3f}ms'.format((stop_time - start_time) * 1000))

  top = top_k[0]
  output = '{:08.6f}: {}'.format(float(results[top]), labels[top])

  return output


def cape_handler(img_buffer):
    img = Image.open(BytesIO(img_buffer))
    #img = Image.frombuffer("L", (4, 4), img_buffer, 'raw', "L", 0, 1)
    output = run_inference(img)
    print("output", output)
    return output

if __name__ == '__main__':
  image = "cat.bmp"
  img = Image.open(image)
  output = run_inference(img)
  print("output", output)
