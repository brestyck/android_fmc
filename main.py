import deep_fmc as df
from time import sleep

print(f"{df.y()}Starting FMC....{df.d()}")
print(f"Accessing GPS....")
i = 0
gps = df.parse_json_gps(df.get_gps())
print(f"{df.g()}GPS DONE")
bold_s = df.colorizer("bold")
thc_origin = input(f"{df.d()}ENTER AIRPORT ORIGIN > {bold_s}{df.y()}")
print(df.colorizer("style_default"))
thc_destination = input(f"{df.d()}ENTER AIRPORT DESTINATION > {bold_s}{df.y()}")
print(df.colorizer("style_default"))

while True:
    if i > 20:
        i = 0
        gps = df.parse_json_gps(df.get_gps())
    df.cls()
    df.aero_cross(f"{thc_origin} - {thc_destination} | {df.g()}{i}/20{df.d()}", gps["altitude"], gps["speed"])
    sleep(1)
    i += 1