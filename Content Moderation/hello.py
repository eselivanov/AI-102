import os

key = os.environ["CONTENT_SAFETY_KEY"]
endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

print("key: %s, url: %s"  % (key, endpoint))

image_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "./sample_data/image.jpg"))
print(image_path)

image_size = os.path.getsize(image_path)
print( "%d Bytes" % (image_size))