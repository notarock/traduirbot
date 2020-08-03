#!/usr/bin/env python3

import sys

from file_detection import detect
from wand.drawing import Drawing
from wand.color import Color
from google.cloud import translate_v2 as translate
from wand.image import Image


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
    target_lang = sys.argv[2]

    print("Translating " + path)

    api_result = detect(path)
    source_text = translate_to(api_result.description, target_lang)
    print("source text: " + source_text)

    vertices = api_result.bounding_poly.vertices

    print(vertices)

    x1 = vertices[0].x
    y1 = vertices[0].y
    x2 = vertices[2].x
    y2 = vertices[2].y

    with Image(filename=path) as img:
        with Drawing() as draw:
            draw.stroke_color = Color('white')
            draw.fill_color = Color('white')
            draw.rectangle(left=x1, top=y1, right=x2, bottom=y2)
            draw(img)

        with Drawing() as draw:
            draw.font = 'wandtests/assets/League_Gothic.otf'
            draw.font_size = 20
            draw.text(x1, y1, source_text)
            draw.draw(img)

        img.save(filename='test.png')

    print("um-k, sounds like im done.")
