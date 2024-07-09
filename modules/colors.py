import random
import colorsys
import re

def random_color():
    h = random.random()
    s = 0.5 + random.random() / 2
    v = 0.7 + random.random() / 3
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    hex_color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255)).upper()

    hex_color = hex_color[:7]
    return hex_color

