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
        image_content = image_file.read()

    image = vision.Image(content=image_content)

    response = vision_client.text_detection(image=image)
    texts = response.text_annotations
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return texts
