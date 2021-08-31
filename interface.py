def aero_cross(up_pars, altitude, speed):
    cross_page = \
        f"""
--------------------------------------
{up_pars}

                 ||
            <----------> 
                 ||

{y()}ALT {altitude}{d()} SPD {speed}
--------------------------------------
        """
    print(cross_page)