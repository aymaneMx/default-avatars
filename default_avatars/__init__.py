# BUILT-IN
import random

# PIP
from cairosvg import svg2png
from xml.sax.saxutils import escape as xml_escape

from default_avatars.config import COLORS, INITIALS_SVG_TEMPLATE, LOGO_SVG_TEMPLATE


def get_png_avatar_from_initials(text, output_file):
    initials = ':)'

    text = text.strip()
    if text:
        split_text = text.split(' ')
        if len(split_text) > 1:
            initials = split_text[0][0] + split_text[-1][0]
        else:
            initials = split_text[0][0]

    random_color = random.choice(COLORS)
    svg_avatar = INITIALS_SVG_TEMPLATE.format(**{
        'color1': random_color[0],
        'color2': random_color[1],
        'text_color': random_color[2],
        'text': xml_escape(initials.upper()),
    }).replace('\n', '')

    svg2png(svg_avatar, write_to=output_file)


def get_png_avatar_from_logo(output_file, color):
    if color:
        random_color = color
    else:
        random_color = random.choice(COLORS)

    svg_avatar = LOGO_SVG_TEMPLATE.format(**{
        'color1': random_color[0],
        'logo_color': random_color[2],
    }).replace('\n', '')

    svg2png(svg_avatar, write_to=output_file)
