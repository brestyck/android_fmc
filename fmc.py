import low_lvl
from time import sleep

# INITIAL START

print(f"{low_lvl.d()}Starting...")
low_lvl.tts("Starting")
print(f"{low_lvl.y()}Getting initial position...")
gps_data = low_lvl.parse_json_gps(low_lvl.get_gps())
lat = gps_data["latitude"]
lon = gps_data["longitude"]
print(f"{low_lvl.g()}LAT {lat} LON {lon}")
low_lvl.tts("Gps on")
low_lvl.cls()
sleep(2)
# ROUTE ENTER
print(f"\n{low_lvl.d()}DEPARTURE | ARRIVAL | CALLSIGN")
arr_dep_call = input(f"{low_lvl.y()}").split()
departure_gate = arr_dep_call[0]
arrival_gate = arr_dep_call[1]
call_sign = arr_dep_call[2]
# DEPARTURE-ARRIVAL TIME
print(f"\n{low_lvl.y()}Departure-arrival time")
print(f"{low_lvl.d()}DEPARTURE TIME | ARRIVAL TIME")
dep_time_arr_time = input().split()
departure_time = dep_time_arr_time[0]
arrival_time = dep_time_arr_time[1]
# QUERYING
print(f"{low_lvl.r()}Registration transition...")
query = low_lvl.url_query(f"https://navrr.herokuapp.com/fmc/register/{call_sign}/"
                          f"{departure_gate}/{arrival_gate}/"
                          f"{departure_time}/{arrival_time}")
print(f"{low_lvl.d()}Got answer: {low_lvl.g()}{query}")

# INITIAL START
