""" Functions for parallel processing """

# Import libraries
from numpy import isinf
from geopy.distance import vincenty


def data_denoising(sub_df, crt_speed=60):
    """ This function aims to identify noisy tweets. By the term noisy, we mean that the
    reported location for the tweet is noisy."""
    zipped_columns = sub_df.tolist()
    lst = list(zip(*zipped_columns))
    lat = lst[0]
    lng = lst[1]
    tw_time = lst[2]
    denoised = [True] * len(sub_df)
    points = list(zip(lat, lng))

    orig = points[0:-2]
    dest1 = points[1:-1]
    dest2 = points[2::]

    for index in range(len(orig)):
        d1 = vincenty(dest1[index], orig[index]).meters
        t1 = tw_time[index+1] - tw_time[index]
        t1 = t1.total_seconds()
        v1 = d1 / t1 if t1 else float('inf')

        d2 = vincenty(dest2[index], dest1[index]).meters
        t2 = tw_time[index+2] - tw_time[index+1]
        t2 = t2.total_seconds()
        v2 = d2 / t2 if t2 else float('inf')

        d3 = vincenty(dest2[index], orig[index]).meters
        t3 = tw_time[index+2] - tw_time[index]
        t3 = t3.total_seconds()
        v3 = d3 / t3 if t3 else float('inf')

        if isinf(v1) | isinf(v2) | isinf(v3):
            denoised = [False] * len(denoised)
            break
        if (v1 > crt_speed) & (v2 > crt_speed):
            if v3 <= crt_speed:
                denoised[index+1] = False
            else:
                denoised[index] = False
                denoised[index+1] = False
                if index == len(orig) - 1:
                    denoised[index+2] = False
        if (v1 > crt_speed) & (v2 <= crt_speed):
            denoised[index] = False

    return denoised
