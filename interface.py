import deep_fmc as df
import points_database as pd


def aero_cross(up_pars, altitude, speed, ils=f"{df.r()}N/A{df.d()}"):
    cross_page = \
        f"""
--------------------------------------
{up_pars}

                 ||
            <----------> 
                 ||

{df.y()}ALT {df.toFixed(altitude, 1)}{df.d()} SPD {df.toFixed(speed, 1)}          {ils}
--------------------------------------
        """
    print(cross_page)


def bottom_nav_panel(next_point, lat, lon):
    if len(next_point) == 3:
        panel = \
            f"""

NXT PNT {df.r()}{next_point}{df.d()}
ECS: ETA LAT {df.y()}{df.toFixed(abs(pd.POINTS[next_point][0] - lat) * 100, 3)}{df.d()}
     ETA LON {df.y()}{df.toFixed(abs(pd.POINTS[next_point][1] - lon) * 100, 3)}{df.d()}
--------------------------------------
            """
    else:
        panel = \
            f"""

{df.y()}LANDING {df.r()}{next_point}{df.d()}
ECS {df.r()}LANDMODE{df.d()}: ETA LAT {df.y()}{df.toFixed(abs(pd.HUBS[next_point][0] - lat) * 100, 3)}{df.d()}
             ETA LON {df.y()}{df.toFixed(abs(pd.HUBS[next_point][1] - lon) * 100, 3)}{df.d()}
--------------------------------------
                    """
    print(panel)


def GTS_interface(status, recommendations):
    panel = \
        f"""
GTS RECOMMENDATION SYSTEM
======================================
STATUS: {status}
{recommendations}
--------------------------------------
        """
    print(panel)


def ils_landing_system(altitude, eta_altitude, land_conditions):
    plus1 = plus2 = minus1 = minus2 = color_cross = df.d()
    delta = altitude - eta_altitude
    if delta > 3:
        minus1 = df.g()
        minus2 = df.y()
        if delta > 5:
            minus1 = df.y()
            minus2 = df.g()
    elif delta < -3:
        plus1 = df.g()
        plus2 = df.y()
        if delta < -5:
            plus1 = df.y()
            plus2 = df.g()
    else:
        plus1 = plus2 = minus1 = minus2 = df.d()
        color_cross = df.g()
    panel = \
        f"""
TARGET ALTITUDE {eta_altitude}
CONDITIONS {land_conditions}
======================================
                  {plus2}--- 
                 {plus1}-----{df.d()}
    {altitude}   -----<{color_cross}-|-{df.d()}>-----
                 {minus1}-----
                  {minus2}---{df.d()}
======================================
        """
    print(panel)


def interface_main(thc_origin, thc_destination, current_point, i, gps, is_landing_mode):
    if is_landing_mode:
        up_params = f"{thc_origin} - {thc_destination} | {df.g()}{i}/20{df.d()} |" \
                    f" {df.y()}LANDING {df.r()}{current_point}{df.d()}"  # Set the landing cross
        altitude = gps["altitude"]  # We have to be on an estimated altitude
        altitude_est = pd.HUBS[thc_destination][2]
        ils = pd.HUBS[thc_destination][3]  # Check whether we have ILS
        aero_cross(up_params, f"{altitude}|^|{altitude_est}", gps["speed"], ils)
        bottom_nav_panel(thc_destination, gps["latitude"], gps["longitude"])
        ils_landing_system(altitude, altitude_est, ils)
    if not is_landing_mode:
        up_params = f"{thc_origin} - {thc_destination} | {df.g()}{i}/20{df.d()} | POINT {df.r()}{current_point}{df.d()}"
        aero_cross(up_params, gps["altitude"], gps["speed"])  # Set a default cross
        bottom_nav_panel(current_point, gps["latitude"], gps["longitude"])

    status, recommendations = df.GTS(gps, is_landing_mode, current_point)
    GTS_interface(status, recommendations)
