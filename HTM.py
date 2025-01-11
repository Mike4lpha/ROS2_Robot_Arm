import numpy as np

T1=120
T2=30
T3=30
T4=-150
a1=5
a2=3
a3=3
a4=1

T1=(T1/180.0)*np.pi
T2=(T2/180.0)*np.pi
T3=(T3/180.0)*np.pi
T4=(T4/180.0)*np.pi

R0_1=[[np.cos(T1),0,np.sin(T1)],[np.sin(T1),0,-np.cos(T1)],[0,1,0]]
R1_2=[[np.cos(T2),-np.sin(T2),0],[np.sin(T2),np.cos(T2),0],[0,0,1]]
R2_3=[[np.cos(T3),-np.sin(T3),0],[np.sin(T3),np.cos(T3),0],[0,0,1]]
R3_4=[[np.cos(T4),-np.sin(T4),0],[np.sin(T4),np.cos(T4),0],[0,0,1]]

R0_2=np.dot(R0_1,R1_2)
R2_4=np.dot(R2_3,R3_4)
R0_4=np.dot(R0_2,R2_4)
# print(np.matrix(R0_4))

d0_1=[[0],[0],[a1]]
d1_2=[[a2*np.cos(T2)],[a2*np.sin(T2)],[0]]
d2_3=[[a3*np.cos(T3)],[a3*np.sin(T3)],[0]]
d3_4=[[a4*np.cos(T4)],[a4*np.sin(T4)],[0]]

H0_1=np.concatenate((R0_1,d0_1),1)
new_row = np.array([0, 0, 0, 1]).reshape(1, -1)
H0_1=np.concatenate((H0_1,new_row),0)
H1_2=np.concatenate((R1_2,d1_2),1)
H1_2=np.concatenate((H1_2,new_row),0)
H2_3=np.concatenate((R2_3,d2_3),1)
H2_3=np.concatenate((H2_3,new_row),0)
H3_4=np.concatenate((R3_4,d3_4),1)
H3_4=np.concatenate((H3_4,new_row),0)

H0_2=np.dot(H0_1,H1_2)
H2_4=np.dot(H2_3,H3_4)
H0_4=np.dot(H0_2,H2_4)

print(np.matrix(H0_4))