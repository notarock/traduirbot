"""
Entry point for the CLi implementation of traduirbot
"""

import sys
import facebook
from config import Config

from file_detection import detect
from image_translator import write_on_image

output_path = "/tmp/out.png"
post = False

def main():
    path = sys.argv[1]
    api_result = detect(path)
    target_lang = Config.get_instance().get_config('TARGET_LANG')

    write_on_image(path, api_result, target_lang, output_path)

    # post = sys.argv[2]
    # post_on_facebook(output_path)

    print('fini')


def post_on_facebook(file_path):
    fb_token = Config.get_instance().get_config('FB_ACCES_TOKEN')
    user_token = Config.get_instance().get_config('FB_USER_TOKEN')
    page_id = Config.get_instance().get_config('FB_PAGE_ID')
    target_lang = os.environ["TARGET_LANG"]

    graph = facebook.GraphAPI(access_token=user_token, version="3.0")

    graph.put_photo(parent_object=page_id,
                    access_token=fb_token,
                    image=open(output_path, 'rb'),
                    message='meme de test')


if __name__ == '__main__':
    main()
    sys.exit(0)
