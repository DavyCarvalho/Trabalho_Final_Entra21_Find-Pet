import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleVisionApiKey.json'

client = vision_v1.ImageAnnotatorClient()

file_name = 'iconedog.png'
image_path = f'.\projeto_findpet\core\static\imgs\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()
    
image = vision_v1.types.Image(content=content)

response = client.image_properties(image=image)

objects = client.object_localization(image=image).localized_object_annotations

print(objects)