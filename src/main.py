"""
Entry point for the CLi implementation of traduirbot
"""
import sys
import facebook
import os
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


def post_on_facebook():
    fb_token = os.environ['FB_ACCESS_TOKEN']
    user_token = os.environ['FB_USER_TOKEN']
    page_id = os.environ['FB_PAGE_ID']

    graph = facebook.GraphAPI(access_token=user_token, version="3.1")

    print(output_path)

    graph.put_photo(parent_object=page_id,
                    access_token=fb_token,
                    connection_name="feed",
                    image=open(output_path, 'rb'))

if __name__ == '__main__':
    main()
    sys.exit(0)
