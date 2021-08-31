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
thc_origin = input(f"{df.d()}ENTER AIRPORT ORIGIN > {bold_s}{df.y()}")
print(df.colorizer("style_default"))
thc_destination = input(f"{df.d()}ENTER AIRPORT DESTINATION > {bold_s}{df.y()}")
print(df.colorizer("style_default"))
print(f"{df.y()}Calculating course....{df.d()}")
course = df.get_the_course(thc_origin, thc_destination)
print(f"{df.g()}Course calculated!{df.d()}")


while True:
    current_point = course[pnt]
    current_point = pd.POINTS[current_point]
    if df.toFixed(gps["latitude"], 3) == current_point[0]:
        if df.toFixed(gps["longitude"], 3) == current_point[1]:
            print(f"APPROACHED POINT f{course[pnt]}")
            pnt += 1
    if i > 20:
        i = 0
        gps = df.parse_json_gps(df.get_gps())
    df.cls()
    up_params = f"{thc_origin} - {thc_destination} | {df.g()}{i}/20{df.d()} | POINT {df.r()}{course[pnt]}{df.d()}"
    inf.aero_cross(up_params, gps["altitude"], gps["speed"])
    sleep(1)
    i += 1