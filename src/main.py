#!/usr/bin/env python3

import io
import sys

from google.cloud import translate_v2 as translate
from google.cloud import vision

PATH = './memes/en/char-spag.png'


def detect(path):
    """
    Uses Google's vision API to get the text
    that is written in the image and its position.
    """
    vision_client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = vision_client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    # for text in texts:
    #     print('\n"{}"'.format(text.description))
    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #         for vertex in text.bounding_poly.vertices])
    #     print('bounds: {}'.format(','.join(vertices)))
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return texts[0].description


def translate_to(source_text, target_lang):
    """
    Translate text to a target langage using auto-detection.
    """
    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    translate_client = translate.Client()

    result = translate_client.translate(
        source_text, target_language=target_lang)

    return result['translatedText']


if __name__ == '__main__':
    path = sys.argv[1]

    print("Translating " + path)

    text = detect(PATH)
    print('source: ' + text)
    print('en :' + translate_to(text, 'fr'))
    print('es :' + translate_to(text, 'es'))
