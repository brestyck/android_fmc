import deep_fmc as df
import points_database as pd
import interface as inf
from time import sleep

print(f"{df.y()}Starting FMC....{df.d()}")
print(f"Accessing GPS....")
i = 0
pnt = 0
gps = df.parse_json_gps(df.get_gps_debug())
print(f"{df.g()}GPS DONE")
bold_s = df.colorizer("bold")
thc_origin = input(f"{df.d()}ENTER AIRPORT ORIGIN > {bold_s}{df.y()}")
print(df.colorizer("style_default"))
thc_destination = input(f"{df.d()}ENTER AIRPORT DESTINATION > {bold_s}{df.y()}")
print(df.colorizer("style_default"))
print(f"{df.y()}Calculating course....{df.d()}")
course = df.get_the_course(thc_origin, thc_destination)
print(f"{df.g()}Course calculated!{df.d()}")


while True:

    if pnt != len(course) - 1:
        current_point = course[pnt]
        current_point = pd.POINTS[current_point]
        landing_mode = False
    else:
        current_point = thc_destination
        landing_mode = True

    if i > 20:
        i = 0
        gps = df.parse_json_gps(df.get_gps())
    df.cls()

    if df.toFixed(gps["latitude"], 3) == current_point[0]:
        if df.toFixed(gps["longitude"], 3) == current_point[1]:
            if not landing_mode:
                print(f"APPROACHED POINT {course[pnt]}")
                df.tts(f"APPROACHED POINT {course[pnt]}")
                pnt += 1
                sleep(5)
            if landing_mode:
                df.tts(f"RETARD")

    if not landing_mode:
        up_params = f"{thc_origin} - {thc_destination} | {df.g()}{i}/20{df.d()} | POINT {df.r()}{course[pnt]}{df.d()}"
        inf.aero_cross(up_params, gps["altitude"], gps["speed"])
    else:
        up_params = f"{thc_origin} - {thc_destination} | {df.g()}{i}/20{df.d()} |" \
                    f" {df.y()}LANDING {df.r()}{course[pnt]}{df.d()}"
        altitude = gps["altitude"]
        altitude_est = pd.HUBS[thc_destination][2]
        ils = pd.HUBS[thc_destination][3]
        inf.aero_cross(up_params, f"{altitude}|^|{altitude_est}", gps["speed"], ils)

    sleep(1)
    i += 1