import numpy as np
import os

msg = "Roll a dice!"
print(msg)

print(np.random.randint(1,9))


key = os.environ["CONTENT_SAFETY_KEY"]
endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

print("key: %s, url: %s"  % (key, endpoint))
# image_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "./sample_data/image.jpg"))
