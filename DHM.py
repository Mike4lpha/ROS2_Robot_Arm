import numpy as np

T1=60
T2=-30
T3=60
T4=0
a1=5
a2=3
a3=3
a4=0

T1=(T1/180.0)*np.pi
T2=(T2/180.0)*np.pi
T3=(T3/180.0)*np.pi
T4=(T4/180.0)*np.pi

PT=[[T1,(90/180)*np.pi,0,a1],[T2,0,a2,0],[T3,0,a3,0],[T4,0,a4,0]]

i=0
H0_1=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][0]),PT[i][2]*np.cos(PT[i][0])],[np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],[0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],[0,0,0,1]]

i=1
H1_2=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][0]),PT[i][2]*np.cos(PT[i][0])],[np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],[0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],[0,0,0,1]]

i=2
H2_3=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][0]),PT[i][2]*np.cos(PT[i][0])],[np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],[0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],[0,0,0,1]]

i=3
H3_4=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][0]),PT[i][2]*np.cos(PT[i][0])],[np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],[0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],[0,0,0,1]]

H0_2=np.dot(H0_1,H1_2)
H2_4=np.dot(H2_3,H3_4)
H0_4=np.dot(H0_2,H2_4)
print(np.matrix(H0_4))