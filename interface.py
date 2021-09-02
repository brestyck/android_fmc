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

{df.y()}ALT {altitude}{df.d()} SPD {speed}          {ils}
--------------------------------------
        """
    print(cross_page)


def bottom_nav_panel(next_point, lat, lon):
    panel = \
        f"""

NXT PNT {df.r()}{next_point}{df.d()}
ECS: ETA LAT {df.y()}{abs(pd.POINTS[next_point][0]-lat)}{df.d()}
     ETA LON {df.y()}{abs(pd.POINTS[next_point][1]-lon)}{df.d()}
--------------------------------------
        """
    print(panel)
