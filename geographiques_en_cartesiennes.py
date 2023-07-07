import math as m
from dms_dd import *
def geographiques_en_cartesiennes(D1,M1,S1,D2,M2,S2,h):
    longitude=dms_to_dd(D1,M1,S1)
    latitude=dms_to_dd(D2,M2,S2)
    a=6378249.2
    b=6356515
    e2=(pow(a,2)-pow(b,2))/(pow(a,2))
    latitude=m.radians(latitude)
    longitude=m.radians(longitude)
    N=a/(m.sqrt(1-(e2*(m.sin(latitude)**2))))
    X=(N+h)*m.cos(longitude)*m.cos(latitude)
    Y=(N+h)*m.sin(longitude)*m.cos(latitude)
    Z=(N*(1-e2)+h)*m.sin(latitude)
    maliste=[]
    maliste.append(X)
    maliste.append(Y)
    maliste.append(Z)

    return maliste
