# Send alert via SIGNL4 (Simple Webhook)

# Send a SIGNL4 alert from TensorFlow
import requests
#import tensorflow as tf
import sys

# SIGNL4 URL with team secret
urlSIGNL4 = 'https://connect.signl4.com/webhook/<team-secret>'

# Send request to SIGNL4 webhook
r = requests.post(urlSIGNL4, "{'Alert': 'TensorFlow', 'Description': 'Abnormal behavior detected.'}")
print(r.status_code)
print(r.headers)
#print(r.headers['content-type'])
print(r.text)
