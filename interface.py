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
