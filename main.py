import deep_fmc as df
import points_database as pd
import interface as inf
from time import sleep

# Introduce variables
i = 0
pnt = 0
gps = df.parse_json_gps(df.get_gps_debug())
landing_mode = False

# Get the course and tell user about it
print(f"{df.y()}Starting FMC....{df.d()}")
df.tts("Starting FMC")
print(f"Accessing GPS....")
print(f"{df.g()}GPS DONE")
thc_origin = input(f"{df.d()}ENTER AIRPORT ORIGIN > {df.y()}").upper()
thc_destination = input(f"{df.d()}ENTER AIRPORT DESTINATION > {df.y()}").upper()
print(f"{df.y()}Calculating course....{df.d()}")
course = df.get_the_course(thc_origin, thc_destination)
print(f"{df.g()}Course calculated!{df.d()}")

while True:
    # Проверка наличия точек в маршруте
    if pnt != len(course):
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

    lat_eq = df.toFixed(gps["latitude"], 3) == current_point[0]
    lon_eq = df.toFixed(gps["longitude"], 3) == current_point[1]
    if lat_eq and lon_eq:  # If lat and lon equal each other
        if not landing_mode:  # Just pass the point with craft
            print(f"APPROACHED POINT {course[pnt]}")
            df.tts(f"APPROACHED POINT {course[pnt]}")
            pnt += 1
        if landing_mode:  # We are on the THC, TTS for the crew to stop
            df.tts(f"RETARD")
            sleep(10)
            exit()

    if not landing_mode:
        inf.interface_main(thc_origin, thc_destination, course[pnt], i, gps, landing_mode)
    else:
        inf.interface_main(thc_origin, thc_destination, current_point, i, gps, landing_mode)

    sleep(1)
    i += 1
