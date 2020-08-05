#!/usr/bin/env python3

import sys

from file_detection import detect
from image_translator import write_on_image

if __name__ == '__main__':
    path = sys.argv[1]
    target_lang = sys.argv[2]
    api_result = detect(path)

    write_on_image(path, api_result, 'fr', 'out.png')

    print("um-k, sounds like im done.")
    sys.exit(0)
