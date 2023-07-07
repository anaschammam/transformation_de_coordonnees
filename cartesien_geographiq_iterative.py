import math as m
from dms_dd import dd_to_dms

def cartesien_geographiq_iterative(X, Y, Z):
    a=6378249.145
    b=6356515.0
    e2=(a**2-b**2)/(a**2)
    longitude=m.atan2(Y,X)
    latitude0=0.0
    latitude=m.atan((Z/m.sqrt(X**2+Y**2))*(1/(1-e2)))

    while abs(latitude-latitude0) > 0.0001:
        latitude0=latitude
        N=a/m.sqrt(1-e2*m.sin(latitude0)**2)
        latitude=m.atan((1+(e2*N*m.sin(latitude0))/Z)*(Z/m.sqrt(X**2+Y**2)))

    N=a/m.sqrt(1-e2*m.sin(latitude) ** 2)
    h=(Z/m.sin(latitude)) - N*(1-e2)
    longitude=m.degrees(longitude)
    latitude=m.degrees(latitude)
    latitude=dd_to_dms(latitude)
    longitude=dd_to_dms(longitude)
    malist=[]
    malist.append(longitude)
    malist.append(latitude)
    malist.append(h)

    return malist
