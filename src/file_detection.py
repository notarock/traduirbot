#!/usr/bin/env python3

import io

from google.cloud import vision


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
