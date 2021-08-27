import os


# COLORING
def r():
    return "\u001b[31m"


def g():
    return "\u001b[32m"


def d():
    return "\u001b[39m"


def y():
    return "\u001b[33m"


def colorizer(code):
    color_codes = {
        "bd": "\u001b[49m",
        "br": "\u001b[41m",
        "blink": "\u001b[5m",
        "style_default": "\u001b[0m",
        "bold": "\u001b[1m",
        "lc": "\u001b[106m"
    }
    return color_codes[code]
# COLORING


# GET GPS
def get_gps():
    json_back = os.system("termux-location -p passive -r once")
    print(json_back)  # DEBUG
