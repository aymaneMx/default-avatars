import random
import string
from io import BytesIO
from PIL import Image

from default_avatars import get_png_avatar_from_logo, COLORS

for color in COLORS:
    rawIO = BytesIO()
    filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    get_png_avatar_from_logo(rawIO, color)
    byteImg = Image.open(rawIO)
    byteImg.save(filename + '.png', 'PNG')
