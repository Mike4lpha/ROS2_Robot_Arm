import math

def rad_deg(rad):
    deg=(rad*180.0)/math.pi
    return deg

cos=math.cos
sin=math.sin
tan=math.tan

x=-2.04903811
y=3.54903811
z= 8.09807621
a1=5
a2=3
a3=3
a4=1
phi=-90
phi=(phi/180.0)*math.pi

z=z-a4*sin(phi)
r=a4*cos(phi)
if r<0:
    r=-r
T1=math.atan2(y,x)
x=x-r*cos(T1)
y=y-r*sin(T1)
r1=math.sqrt((x**2)+(y**2))
r2=z-a1
phi2=math.atan2(r2,r1)
r3=math.sqrt((r1**2)+(r2**2))
cphi1=((a3**2)-(a2**2)-(r3**2))/(-2*a2*r3)
phi1=math.acos(cphi1)
T2=phi2-phi1
cphi3=((r3**2)-(a2**2)-(a3**2))/(-2*a2*a3)
phi3=math.acos(cphi3)
T3=3.14-phi3
T4=phi-T2-T3
T1=rad_deg(T1)
T2=rad_deg(T2)
T3=rad_deg(T3)
T4=rad_deg(T4)
print("elbow down:")
print(T1,T2,T3,T4)
T2=phi1+phi2
T3=-T3
T2=rad_deg(T2)
phi=rad_deg(phi)
T4=phi-T2-T3
print("elbow up:")
print(T1,T2,T3,T4)