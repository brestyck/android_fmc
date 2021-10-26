import os
import platform
import multiprocessing
import json
from urllib.request import urlopen


def r():
    return "\u001b[31m"


def g():
    return "\u001b[32m"


def d():
    return "\u001b[39m"


def y():
    return "\u001b[33m"


def c():
    return "\u001b[36m"


def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def tts_legal(text):
    if platform.system() == "Linux":
        os.popen(f"termux-tts-speak -l eng -p 0.7 -s ALARM -r 0.9 {text}")


def tts(text):
    if platform.system() == "Linux":
        p = multiprocessing.Process(target=tts_legal(text))
        p.start()


def get_gps():
    json_gps = os.popen("termux-location -p network").read()
    if json_gps == "":
        print(f"{r()}PASSIVE GPS EMPTY, EMULATING FATAL!{d()}")
        json_gps = os.popen("termux-location").read()
    print(json_gps)  # DEBUG
    return json_gps


def parse_json_gps(json_gps):
    gps_data = json.loads(json_gps)
    return gps_data


def url_query(dat_url):
    hnd = urlopen(dat_url)
    return hnd.read().decode("utf-8")
