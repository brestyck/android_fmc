import low_lvl
import datetime
from time import sleep

# INITIAL START

s = " "
d = "-"
print(f"{low_lvl.d()}Starting...")
low_lvl.tts("Starting")
print(f"{low_lvl.y()}Getting initial position...")
gps_data = low_lvl.parse_json_gps(low_lvl.get_gps())
lat = low_lvl.toFixed(gps_data["latitude"], 6)
lon = low_lvl.toFixed(gps_data["longitude"], 6)
print(f"{low_lvl.g()}LAT {lat} LON {lon}")
low_lvl.tts("Position init")
low_lvl.cls()
input("\n\n\n\n\nPRESS ENTER TO CONTINUE")
# ROUTE ENTER
print(f"\n{low_lvl.d()}DEPARTURE | ARRIVAL | CALLSIGN")
arr_dep_call = input(f"{low_lvl.y()}").split()
departure_gate = arr_dep_call[0]
arrival_gate = arr_dep_call[1]
call_sign = arr_dep_call[2]
# DEPARTURE-ARRIVAL TIME
print(f"\n{low_lvl.y()}Departure-arrival time")
print(f"{low_lvl.d()}DEPARTURE TIME | ARRIVAL TIME | ETA DIST KM")
dep_time_arr_time = input().split()
departure_time = dep_time_arr_time[0]
arrival_time = dep_time_arr_time[1]
# QUERYING
print(f"{low_lvl.r()}Registration transition...")
query = low_lvl.url_query(f"https://navrr.herokuapp.com/fmc/register/{call_sign}/"
                          f"{departure_gate}/{arrival_gate}/"
                          f"{departure_time}/{arrival_time}/"
                          f"{lat}/{lon}")
print(f"{low_lvl.d()}Got answer: {low_lvl.g()}{query}")
low_lvl.tts("Access granted")
input("\n\n\n\n\nPRESS ENTER TO CONTINUE")
i = 0
# INITIAL START

# MAIN CYCLE
try:
    while True:
        low_lvl.cls()
        print(f"{low_lvl.c()}ACT FPLN")
        print(f"\n{low_lvl.c()}ORIGIN{20*s}DESTINATION")
        print(f"{low_lvl.d()}{2*s}{departure_gate}{20*s}{arrival_gate}")
        print(f"\n{low_lvl.c()}{22*s}TRN NO{low_lvl.d()}")
        print(f"{20*s}{call_sign}")
        print(f"\n{low_lvl.c()}POS INIT")
        print(f"{low_lvl.y()}{lat}{s}{lon}\n\n")
        print(f"{low_lvl.c()}{d*36}")
        # INFO PAGE
        if i == 10:
            print(f"{low_lvl.r()}Updating geo...{low_lvl.d()}")
            gps_data = low_lvl.parse_json_gps(low_lvl.get_gps())
            lat = low_lvl.toFixed(gps_data["latitude"], 6)
            lon = low_lvl.toFixed(gps_data["longitude"], 6)
            query = low_lvl.url_query(f"https://navrr.herokuapp.com/fmc/squawk/{call_sign}/{lat}/{lon}/INPROGRESS")
            i = 0
        else:
            sleep(10)
        i += 1
except KeyboardInterrupt:
    query = low_lvl.url_query(f"https://navrr.herokuapp.com/fmc/squawk/{call_sign}/{lat}/{lon}/ARRIVED")
    print(f"Got answer: {low_lvl.g()}{query}")
    print(f"{low_lvl.y()}Transition over{low_lvl.d()}")
    low_lvl.tts("Retard")
    sleep(5)
    exit()

# MAIN CYCLE
