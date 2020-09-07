# The Easiest Way To Generate Fancy Avatars In Python

This a demo of my [article](https://aymanemx.com/posts/fancy-avatars-in-python) on how to generate cool avatars from a given string (email, username...) or from your logo using python.

## Run it locally 

```bash
pipenv shell 

python local_test.py 
```

## Django integration 

Create a file `utils/avatars.py` in your django project, paste this in it :point_down:

```python
# BUILT-IN
import random
import re
from io import BytesIO

# PIP
from cairosvg import svg2png
from xml.sax.saxutils import escape as xml_escape
from django.core.files.images import ImageFile


COLORS = [
    ['#DF7FD7', '#DF7FD7', '#591854'],
    ['#E3CAC8', '#DF8A82', '#5E3A37'],
    ['#E6845E', '#E05118', '#61230B'],
    ['#E0B050', '#E6CB97', '#614C23'],
    ['#9878AD', '#492661', '#C59BE0'],
    ['#787BAD', '#141961', '#9B9FE0'],
    ['#78A2AD', '#104F61', '#9BD1E0'],
    ['#78AD8A', '#0A6129', '#9BE0B3'],
]

INITIALS_SVG_TEMPLATE = """
<svg xmlns="http://www.w3.org/2000/svg" pointer-events="none" width="200" height="200">
  <defs>
    <linearGradient id="grad">
    <stop offset="0%" stop-color="{color1}" />
    <stop offset="100%" stop-color="{color2}" />
    </linearGradient>
  </defs>
  <rect width="200" height="200" rx="0" ry="0" fill="url(#grad)"></rect>
  <text text-anchor="middle" y="50%" x="50%" dy="0.35em"
        pointer-events="auto" fill="{text_color}" font-family="sans-serif"
        style="font-weight: 400; font-size: 80px">{text}</text>
</svg>
""".strip()
INITIALS_SVG_TEMPLATE = re.sub('(\s+|\n)', ' ', INITIALS_SVG_TEMPLATE)


def generate_avatar(text):
    """Generates a django ImageFile object based on an svg code with random
    color chosen from a list of defined colors"""

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

    stream = BytesIO()
    svg2png(svg_avatar, write_to=stream)

    return ImageFile(stream, name=text + '.png')
```
Now, the function `generate_avatar` is ready to be used in your project.

Enjoy!