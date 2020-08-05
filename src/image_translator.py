#!/usr/bin/env python3

from translator import translate_to
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image
import urllib.parse


def write_on_image(filename, detected_text, target_lang, output_file):
    with Image(filename=filename) as img:
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
                with Drawing() as draw:
                    draw.stroke_color = Color('white')
                    draw.fill_color = Color('white')
                    draw.rectangle(
                        left=rec_left,
                        top=rec_top,
                        right=rec_right,
                        bottom=rec_bottom)
                    draw(img)

                with Drawing() as draw:
                    draw.font = 'wandtests/assets/League_Gothic.otf'
                    draw.font_size = font_size
                    draw.text(x_1, y_2, translated)
                    draw.draw(img)
            except BaseException:
                pass

        img.save(filename=output_file)
