#!/usr/bin/env python3

from google.cloud import translate_v2 as translate


def translate_to(source_text, target_lang):
    """
    Translate text to a target langage using auto-detection.
    """
    translate_client = translate.Client()
    result = translate_client.translate(
        source_text, target_language=target_lang)
    return result['translatedText']
