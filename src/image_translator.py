#!/usr/bin/env python3

import sys
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from translator import translate_to


def write_on_image(filename, detected_text, target_lang, output_file):
    img = Image.open(filename)

    texts = detected_text
    texts.pop(0)

    for text in texts:
        translated = translate_to(text.description, target_lang)
        print(translated)

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        print('bounds: {}'.format(','.join(vertices)))

        x_1 = text.bounding_poly.vertices[0].x
        x_2 = text.bounding_poly.vertices[2].x
        y_1 = text.bounding_poly.vertices[0].y
        y_2 = text.bounding_poly.vertices[2].y

        scale = min(len(text.description) / len(translated), 1)
        font_size = round((y_2 - y_1) * scale)

        padding = 5

        rec_left = max(x_1 - padding, 0)
        rec_top = min(y_1 - padding, img.height)
        rec_right = min(x_2 + padding, img.width)
        rec_bottom = max(y_2 + padding, 0)

        try:
            box = (rec_left, rec_top, rec_right, rec_bottom)
            img_ctx = img.crop(box)
            # with the BLUR filter, you can blur a few
            # times to get the effect you're seeking
            for i in range(10):
                img_ctx = img_ctx.filter(ImageFilter.BLUR)
            img.paste(img_ctx, box)

            # get a font
            dirname = os.path.dirname(__file__)
            fontfile = os.path.join(dirname, '../resources/impact.ttf')
            fnt = ImageFont.truetype(fontfile, font_size)

            # get a drawing context
            d = ImageDraw.Draw(img)

            # draw multiline text
            d.multiline_text((rec_left, rec_top),
                             translated,
                             font=fnt,
                             fill=(255, 255, 255), stroke_width=1, stroke_fill=(0,0,0))

        except:
            print("Unexpected error:", sys.exc_info()[0])
            pass
    img.save(output_file, "PNG")
