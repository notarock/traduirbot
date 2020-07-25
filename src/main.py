#!/usr/bin/env python3
from google.cloud import vision
import io
from os import environ

path = './memes/en/char-spag.png'

if __name__ == '__main__':
    vision_client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    # image = vision.types.Image(content=content)
    # response = client.text_detection(image=image)
    # texts = response.text_annotations

    # Make an authenticated API request
    print(environ.get('TARGET_LANG', 'sa marche pa'))
    print("y se passe rien ici dans le fond...")
