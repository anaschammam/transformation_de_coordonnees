from dms_dd import *
import math as m

def cartesien_geographiq_directe(X, Y, Z):
    a=6378249.145
    b=6356515.0
    f=(a-b)/a
    e2=(a**2-b**2)/(a**2)
    r=m.sqrt(pow(X,2)+pow(Y,2)+pow(Z,2))
    mu=m.atan((Z/(m.sqrt(pow(X,2)+pow(Y,2))))*((1-f) + (a*e2)/r))
    lamda=m.atan2(Y,X)
    phi=m.atan((Z*(1-f) + (a*e2*pow(m.sin(mu),3)))/((1-f)*((m.sqrt(pow(X,2) + pow(Y,2)))-(e2*a*pow(m.cos(mu),3)))))
    h=(m.sqrt(pow(X,2) + pow(Y,2))*m.cos(phi))+(Z*m.sin(phi)) - (a*m.sqrt(1-e2*pow(m.sin(phi),2)))
    lamda=m.degrees(lamda)
    phi=m.degrees(phi)
    lamda=dd_to_dms(lamda)
    phi=dd_to_dms(phi)
    malist=[]
    malist.append(lamda)
    malist.append(phi)
    malist.append(h)

    return malist