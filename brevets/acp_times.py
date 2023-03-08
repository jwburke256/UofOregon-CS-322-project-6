"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow 


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


#speed array of tuples
maxSpeeds = [(200,34), (200,32), (200,30), (400,28), (300,26)]
minSpeeds = [(600,15), (400,11.428), (300,13.33)]

brevetStartTimes = {200:5.53, 300:9, 400:12.08, 600:18.48, 1000:33.05 }
brevetEndTimes = {200:13.5, 300:20, 400:27, 600:40, 1000:75, 1200:90, 1400:116.4, 2200:220}

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    
    if control_dist_km == 0:
        return brevet_start_time
    if control_dist_km >= brevet_dist_km:
        return_time = brevetStartTimes[brevet_dist_km]
        hours = return_time
        hours = int(hours)
        mins = return_time - hours
        mins = mins * 100
        brevet_start_time = brevet_start_time.shift(hours = hours) 
        brevet_start_time = brevet_start_time.shift(minutes = mins) 
        return brevet_start_time
    for speeds in maxSpeeds:
        dist, time = speeds
        if (control_dist_km > dist):
            return_time = dist / time
            hours = return_time
            hours = int(hours)
            mins = return_time - hours
            mins = mins * 60
            mins = round(mins)
            brevet_start_time = brevet_start_time.shift(hours=+hours)
            brevet_start_time = brevet_start_time.shift(minutes=+mins)
            control_dist_km -= dist
        else:
            return_time = control_dist_km / time
            hours = return_time
            hours = int(hours)
            mins = return_time - hours
            mins = mins * 60
            mins = round(mins)
            brevet_start_time = brevet_start_time.shift(hours=+hours)
            brevet_start_time = brevet_start_time.shift(minutes=+mins)
            return brevet_start_time


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    original_cntrl_dist = control_dist_km
    if control_dist_km == 0:
        return brevet_start_time.shift(hours=+1)
    # if control is greater than final brevet dist, we need to just return final brevet calc
    if control_dist_km >= brevet_dist_km:
        return_time = brevetEndTimes[brevet_dist_km]
        hours = return_time
        hours = int(hours)
        mins = return_time - hours            
        mins = mins * 60
        mins = round(mins)
        brevet_start_time = brevet_start_time.shift(hours = hours) 
        brevet_start_time = brevet_start_time.shift(minutes = mins) 
        return brevet_start_time
    for speeds in minSpeeds:
        dist, time = speeds
        if (control_dist_km > dist):
            return_time = dist / time
            hours = return_time
            hours = int(hours)
            mins = return_time - hours            
            mins = mins * 60
            mins = round(mins)
            brevet_start_time = brevet_start_time.shift(hours = hours)
            brevet_start_time = brevet_start_time.shift(minutes = mins)
            control_dist_km -= dist
        else:
            # account for control points under 60km
            if (original_cntrl_dist <= 60):
                return_time = control_dist_km / 20
                hours = return_time
                hours = int(hours)
                mins = return_time - hours            
                mins = mins * 60
                mins = round(mins)
                brevet_start_time = brevet_start_time.shift(hours = hours)
                brevet_start_time = brevet_start_time.shift(minutes = mins)
                brevet_start_time = brevet_start_time.shift(hours=+1)
                return brevet_start_time
            # control points above 60km's
            return_time = control_dist_km / time
            hours = return_time
            hours = int(hours)
            mins = return_time - hours            
            mins = mins * 60
            mins = round(mins)
            brevet_start_time = brevet_start_time.shift(hours = hours)
            brevet_start_time = brevet_start_time.shift(minutes = mins)
            return brevet_start_time
            
