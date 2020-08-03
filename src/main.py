#!/usr/bin/env python3

import sys

from google.cloud import translate_v2 as translate

from file_detection import detect
from image_edits import write_on_image


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
    translation_result = translate_to(api_result.description, target_lang)
    print("source text: " + translation_result.description)

    vertices = api_result.bounding_poly.vertices

    write_on_image(path, translation_result, 'out.png')

    print("um-k, sounds like im done.")
