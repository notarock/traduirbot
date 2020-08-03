#!/usr/bin/env python3

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


def write_on_image(filename, translation_result, output_file):
    x_1 = translation_result.vertices[0].x
    y_1 = translation_result.vertices[0].y
    x_2 = translation_result.vertices[2].x
    y_2 = translation_result.vertices[2].y

    with Image(filename=filename) as img:
        with Drawing() as draw:
            draw.stroke_color = Color('white')
            draw.fill_color = Color('white')
            draw.rectangle(left=x_1, top=y_1, right=x_2, bottom=y_2)
            draw(img)

        with Drawing() as draw:
            draw.font = 'wandtests/assets/League_Gothic.otf'
            draw.font_size = 20
            draw.text(x_1, y_1, translation_result.description)
            draw.draw(img)

        img.save(filename=output_file)
