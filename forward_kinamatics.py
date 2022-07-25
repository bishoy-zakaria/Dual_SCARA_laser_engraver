import math 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # A Great Package For Plotting and Visualization

lenth = 0.20 #upper links
lenth_2 = 0.25 #motor links
motor_distance=0.20
Data= [0]

def Forward_Kinamatics(theta_1,theta_2):
    global lenth , lenth_2 , motor_distance
    X=0
    Y=0
    
    theta_1 = math.radians(theta_1)
    theta_2 = math.radians(theta_2)
    
    X_a = ((lenth_2 * math.cos(theta_1)) - (motor_distance/2))
    Y_a = lenth_2 * math.sin(theta_1)
    
    X_b = ((lenth_2 * math.cos(theta_2)) + (motor_distance/2))
    Y_b = lenth_2* math.sin(theta_2)
    
    h= math.sqrt( ((Y_b - Y_a)**2) + ((X_b - X_a)**2) )
    
    pthay = math.atan2((Y_b-Y_a) , (X_b-X_a))
    if (h/(2*lenth)) < 1:
        alpha = math.acos(h/(2*lenth))
        gama = alpha + pthay 
    
        X = (X_a + (lenth*math.cos(gama)))*100 # cm 
        Y = (Y_a + (lenth*math.sin(gama)))*100
    
    return math.degrees(theta_1),math.degrees(theta_2),X,Y

for i in range (0,361,1):
    for x in range (0,361,1):
        Co=Forward_Kinamatics(i,x)
        Co=list(Co)
        if (i==0):
            if x==0:
                Data[0]=Co
            else:
                Data.append(Co)
        else:
            Data.append(Co)
    
Robot_Data=np.array(Data)
df= pd.DataFrame(Robot_Data)
writer=pd.ExcelWriter("robot_data.xlsx")
df.to_excel(writer)
writer.save()

print(df)