#!/usr/bin/env python3

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image

from translator import translate_to

def write_on_image(filename, detected_text, target_lang, output_file):
    with Image(filename=filename) as img:
        texts = detected_text
        print("before")
        print(texts)
        texts.pop(0)
        print("after")
        print(texts)

        for text in texts:
            translated = translate_to(text.description, target_lang)

            print('\n"{}"'.format(text.description))
            vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])
            print('bounds: {}'.format(','.join(vertices)))

            x_1 = text.bounding_poly.vertices[0].x
            x_2 = text.bounding_poly.vertices[2].x
            y_1 = text.bounding_poly.vertices[0].y
            y_2 = text.bounding_poly.vertices[2].y

            with Drawing() as draw:
                draw.stroke_color = Color('white')
                draw.fill_color = Color('white')
                draw.rectangle(left=x_1, top=y_1, right=x_2, bottom=y_2)
                draw(img)

            with Drawing() as draw:
                draw.font = 'wandtests/assets/League_Gothic.otf'
                font_size = 20
                draw.font_size = font_size
                draw.text(x_1, y_2, translated)
                draw.draw(img)

        img.save(filename=output_file)
