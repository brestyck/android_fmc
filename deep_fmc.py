import os
import platform
import json
import points_database as pd


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


def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# COLORING


# GET GPS
def get_gps():
    json_gps = os.popen("termux-location").read()
    print(json_gps)  # DEBUG
    return json_gps


def get_gps_debug():
    # 55.789, 37.372
    json_gps = \
        """
    {
        "latitude": 55.789938333333335,
        "longitude": 37.372838333333334,
        "altitude": 161.9,
        "accuracy": 9.100000381469727,
        "vertical_accuracy": 0.0,
        "bearing": 0.0,
        "speed": 0.0,
        "elapsedMs": 7,
        "provider": "gps"
    }
"""
    return json_gps


# PARSING ALL THE GPS STUFF
def parse_json_gps(json_gps):
    gps_data = json.loads(json_gps)
    return gps_data


def get_the_course(thc_origin, thc_destination):
    # origin_params = pd.HUBS[thc_origin]
    # destination_params = pd.HUBS[thc_destination]
    try:
        current_way = pd.WAYS[f"{thc_origin}-{thc_destination}"]
    except KeyError:
        current_way = pd.WAYS[f"{thc_destination}-{thc_origin}"]
        current_way.reverse()
    return current_way


def toFixed(num_object, digits):
    no_str = str(num_object)[:digits+3]
    return float(no_str)


def tts(text):
    if platform.system() == "Linux":
        os.system(f"termux-tts-speak -l eng -p 0.7 -s ALARM -r 0.9 {text}")
