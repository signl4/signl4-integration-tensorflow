# Send alert via SIGNL4 (REST API)

import matplotlib.pyplot as plt
import numpy as np
import base64
from IPython.display import Image

# SIGNL4 API Key
apiKey = 'ENTER YOUR SIGNL4 API KEY HERE';

# Create sample diagram
x = np.arange(20)
y = [x_i + np.random.randn(1) for x_i in x]
a, b = np.polyfit(x, y, 1)
_ = plt.plot(x, y, 'o', np.arange(20), a*np.arange(20)+b, '-')

plt.savefig('plot1.png', bbox_inches='tight')
#display(Image('plot1.png'))

import requests
import tensorflow as tf
import sys

# Encode image as base64
with open('plot1.png', 'rb') as f:
    img_data = f.read()

base64Image = base64.b64encode(img_data)
base64Image = base64Image.decode('utf-8')

print('Bytes: %s' % (base64Image))

# Assemble header information for SIGNL4 webhook
headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + apiKey}

# Assemple SIGNL4 alert data
json = {
  "externalId": "1",
  "category": "none",
  "severity": 0,
  "attachments": [
    {
      "id": "0",
      "encoding": 1,
      "name": "image",
      "contentType": "image/png",
      "content": base64Image
    }
  ],
  "parameters": [
    {
      "name": "Big Data",
      "type": 0,
      "value": "Stack overflow detected by TensorFlow."
    }
  ],
  "title": "TensorFlow",
  "text": "TensorFlow Alert",
  "flags": 0
}

# Send request to SIGNL4 webhook
r = requests.post('https://connect.signl4.com/api/alerts', headers=headers, json=json)
print(r.status_code)
print(r.headers)
#print(r.headers['content-type'])
print(r.text)
