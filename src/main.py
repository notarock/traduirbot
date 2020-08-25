"""
Entry point for the CLi implementation of traduirbot
"""

import sys

from file_detection import detect
from image_translator import write_on_image

if __name__ == '__main__':
    path = sys.argv[1]
    target_lang = sys.argv[2]
    api_result = detect(path)

    write_on_image(path, api_result, target_lang, 'out.png')

    print('fini')

    sys.exit(0)
