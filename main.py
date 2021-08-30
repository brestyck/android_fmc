import deep_fmc as df
from time import sleep

print(f"{df.y()}Starting FMC....{df.d()}")
print(f"Accessing GPS....")
debug_val = df.parse_json_gps(df.get_gps_debug())["altitude"]
print(f"Current altitude: {df.g()}{debug_val}{df.d()}")

while True:
    df.cls()
    df.aero_cross("TEST MODE ACTIVE", "N/S")
    sleep(20)