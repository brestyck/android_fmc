import multiprocessing
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


def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# COLORING


# GET GPS
def get_gps():
    json_gps = os.popen("termux-location -p network").read()
    if json_gps == "":
        print(f"{r()}PASSIVE GPS EMPTY, EMULATING FATAL!{d()}")
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


def tts_legal(text):
    if platform.system() == "Linux":
        os.popen(f"termux-tts-speak -l eng -p 0.7 -s ALARM -r 0.9 {text}")


def tts(text):
    if platform.system() == "Linux":
        p = multiprocessing.Process(target=tts_legal(text))
        p.start()


def GTS(gps, is_landing_mode, point):
    recommendations = ""
    status = ""
    if is_landing_mode:
        landing_parameters = pd.HUBS[point]
        delta_lat = abs(landing_parameters[0] - gps["latitude"])
        delta_lon = abs(landing_parameters[1] - gps["longitude"])
        if delta_lon < 0.04 or delta_lat < 0.04:
            recommendations += f"{y()}LANDING SOON{d()}\n"
            status = f"{g()}LANDING{d()}"
        if landing_parameters[2] != 0.0:
            if gps["altitude"]-landing_parameters[2] < 20:
                recommendations += f"{r()}TOO LOW{d()}\n"
                tts("PULL UP TERRAIN AHEAD")
                status = f"{r()}LANDING CONFIGURATION FAULT{d()}"
            elif gps["altitude"]-landing_parameters[2] > 20:
                recommendations += f"{r()}TOO HIGH{d()}\n"
                tts("PULL DOWN YOU ARE OUT OF A GLIDE PATH")
                status = f"{r()}LANDING CONFIGURATION FAULT{d()}"
    else:
        status = f"{g()}ACTIVE{d()}"
    if gps["speed"] == 0.0:
        recommendations += f"{y()}SPEED ZERO{d()}\n"
    if gps["provider"] == "gps":
        recommendations += f"{g()}GPS TURNED ON{d()}\n"
    if gps["speed"] > 90:
        recommendations += f"{r()}SLOW DOWN!{d()}\n"
        tts("SLOW DOWN")
    return status, recommendations
