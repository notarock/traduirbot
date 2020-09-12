"""
Entry point for the CLi implementation of traduirbot
"""

import sys
import facebook
from config import Config

from file_detection import detect
from image_translator import write_on_image

if __name__ == '__main__':
    fb_token = Config.get_instance().get_config('FB_ACCES_TOKEN')
    user_token = Config.get_instance().get_config('FB_USER_TOKEN')
    page_id = Config.get_instance().get_config('FB_PAGE_ID')

    graph = facebook.GraphAPI(access_token=user_token, version="3.0")

    target_lang = "fr"
    path = sys.argv[1]
    api_result = detect(path)

    write_on_image(path, api_result, target_lang, 'out.png')

    graph.put_photo(parent_object=page_id,
                    access_token=fb_token,
                    image=open('out.png', 'rb'),
                    message='Mon premier meme traduit par bot')

    print('fini')

    sys.exit(0)
