import deep_fmc as df
import points_database as pd
import interface as inf
from time import sleep

print(f"{df.y()}Starting FMC....{df.d()}")
print(f"Accessing GPS....")
i = 0
pnt = 0
gps = df.parse_json_gps(df.get_gps())
print(f"{df.g()}GPS DONE")
bold_s = df.colorizer("bold")
thc_origin = input(f"{df.d()}ENTER AIRPORT ORIGIN > {bold_s}{df.y()}").upper()
print(df.colorizer("style_default"))
thc_destination = input(f"{df.d()}ENTER AIRPORT DESTINATION > {bold_s}{df.y()}").upper()
print(df.colorizer("style_default"))
print(f"{df.y()}Calculating course....{df.d()}")
course = df.get_the_course(thc_origin, thc_destination)
print(f"{df.g()}Course calculated!{df.d()}")
landing_mode = False

while True:

    # Проверка наличия точек в маршруте
    if pnt != len(course) - 1:
        current_point = course[pnt]  # Take the point with NUM PNT from course
        current_point = pd.POINTS[current_point]  # Get the coordinates
        landing_mode = False  # Do not set the landing mode
    else:
        # Точек нет, посадочный режим
        current_point = thc_destination  # Since no points, take the THC as a point
        if not landing_mode:  # If we hadn't TTS
            df.tts(f"AIRCRAFT LANDING MODE, LANDING POINT IS {current_point}")
        landing_mode = True

    if i > 20:
        i = 0
        gps = df.parse_json_gps(df.get_gps())
    df.cls()

    if df.toFixed(gps["latitude"], 3) == current_point[0]:
        if df.toFixed(gps["longitude"], 3) == current_point[1]:  # If lat and lon equal each other
            if not landing_mode:  # Just pass the point with craft
                print(f"APPROACHED POINT {course[pnt]}")
                df.tts(f"APPROACHED POINT {course[pnt]}")
                pnt += 1
                sleep(5)
            if landing_mode:  # We are on the THC, TTS for the crew to stop
                df.tts(f"RETARD")
                sleep(10)
                exit()

    if not landing_mode:
        up_params = f"{thc_origin} - {thc_destination} | {df.g()}{i}/20{df.d()} | POINT {df.r()}{course[pnt]}{df.d()}"
        inf.aero_cross(up_params, gps["altitude"], gps["speed"])  # Set a default cross
        inf.bottom_nav_panel(course[pnt], gps["latitude"], gps["longitude"])
    else:
        up_params = f"{thc_origin} - {thc_destination} | {df.g()}{i}/20{df.d()} |" \
                    f" {df.y()}LANDING {df.r()}{current_point}{df.d()}"  # Set the landing cross
        altitude = gps["altitude"]  # We have to be on an estimated altitude
        altitude_est = pd.HUBS[thc_destination][2]
        ils = pd.HUBS[thc_destination][3]  # Check whether we have ILS
        inf.aero_cross(up_params, f"{altitude}|^|{altitude_est}", gps["speed"], ils)
        inf.bottom_nav_panel(thc_destination, gps["latitude"], gps["longitude"])

    status, recommendations = df.GTS(gps, landing_mode, current_point)
    inf.GTS_interface(status, recommendations)

    sleep(1)
    i += 1
