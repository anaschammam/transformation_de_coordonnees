def dms_to_dd(D,M,S):
    dd=D+(M/60)+(S/3600)
    return dd
    
def dd_to_dms(dd):
    D=int(dd)
    M=int((dd-D)*60)
    S=((dd-D)-(M/60))*3600
    return D,M,S

