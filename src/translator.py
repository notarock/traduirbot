#!/usr/bin/env python3

from google.cloud import translate_v2 as translate

from dictionnary_builder import get_spreadsheet_content

WORDS_DICTIONNARY = get_spreadsheet_content()

def translate_to(source_text, target_lang):
    """
    Translate text to a target langage using auto-detection.
    """
    found = WORDS_DICTIONNARY.get(source_text.lower())
    if (found is not None):
        print("Found word "+ source_text
              + ', manualy translate to ' + found)
        return found

    translate_client = translate.Client()
    result = translate_client.translate(
        source_text, target_language=target_lang)

    return result['translatedText'].replace("&#39;", "'").replace("&quot;", '"')
