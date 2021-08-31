import deep_fmc as df


def aero_cross(up_pars, altitude, speed):
    cross_page = \
        f"""
--------------------------------------
{up_pars}

                 ||
            <----------> 
                 ||

{df.y()}ALT {altitude}{df.d()} SPD {speed}
--------------------------------------
        """
    print(cross_page)