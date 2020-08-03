#!/usr/bin/env python3

import sys

from google.cloud import translate_v2 as translate
from file_detection import detect

PATH = './memes/en/char-spag.png'

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
