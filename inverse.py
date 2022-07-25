import math 
import numpy as np
import pandas as pd

lenth = 0.25 #lenth of all links in robot
lenth_6 = 0.2
Data= [0]

def Forward_Kinamatics(theta_1,theta_2):
    global lenth 
    X=0
    Y=0
    
    theta_1 = math.radians(theta_1)
    theta_2 = math.radians(theta_2)
    
    X_a = ((lenth * math.cos(theta_1)) - (lenth_6/2))
    Y_a = lenth* math.sin(theta_1)
    
    X_b = ((lenth * math.cos(theta_2)) + (lenth_6/2))
    Y_b = lenth* math.sin(theta_2)
    
    h= math.sqrt( ((Y_b - Y_a)**2) + ((X_b - X_a)**2) )
    
    pthay = math.atan2((Y_b-Y_a) , (X_b-X_a))
    if (h/(2*lenth)) < 1:
        alpha = math.acos(h/(2*lenth))
        gama = alpha + pthay 
    
        X = (X_a + (lenth*math.cos(gama)))*100 # cm 
        Y = (Y_a + (lenth*math.sin(gama)))*100
    return X,Y

def Inverse_Kinamatics_Solution_1(X,Y):
    global lenth,lenth_6
    theta_1=0 
    theta_2=0
    val=50 #initialization only
    X=X/100
    Y=Y/100
    K1 = math.sqrt(((X+(lenth_6/2))**2)+(Y**2))
    K2 = math.sqrt(((X-(lenth_6/2))**2)+(Y**2))
    
    if K1 != 0:
        if K2 !=0: 
            val= ((K1**2)/(2*lenth*K1))
            val_2= ((K2**2)/(2*lenth*K2))
    if val < 1:
        if val > -1:
            if val_2<1:
                if val_2>-1:
                    pthai_1 = math.acos((K1**2)/(2*lenth*K1))
                    pthai_2 = math.acos((K2**2)/(2*lenth*K2))
    
                    zeta_1 = math.atan2(Y,(X+(lenth_6/2)))
                    zeta_2 = math.atan2(Y,(X-(lenth_6/2)))
    
                    theta_1 = zeta_1 + pthai_1  
                    theta_2 = zeta_2 - pthai_2  
                    
    return math.degrees(theta_1) ,math.degrees(theta_2)
  

def Inverse_Kinamatics_Solution_3(X,Y):
    global lenth,lenth_6
    theta_1=0 
    theta_2=0
    val=50 #initialization only
    X=X/100
    Y=Y/100
    K1 = math.sqrt(((X+(lenth_6/2))**2)+(Y**2))
    K2 = math.sqrt(((X-(lenth_6/2))**2)+(Y**2))
    
    if K1 != 0:
        if K2 !=0: 
            val= ((K1**2)/(2*lenth*K1))
            val_2= ((K2**2)/(2*lenth*K2))
    if val < 1:
        if val > -1:
            if val_2<1:
                if val_2>-1:
                    pthai_1 = math.acos((K1**2)/(2*lenth*K1))
                    pthai_2 = -math.acos((K2**2)/(2*lenth*K2))
    
                    zeta_1 = math.atan2(Y,(X+(lenth_6/2)))
                    zeta_2 = math.atan2(Y,(X-(lenth_6/2)))
    
                    theta_1 = zeta_1 + pthai_1  
                    theta_2 = zeta_2 - pthai_2  
                    
    return math.degrees(theta_1) ,math.degrees(theta_2)


        
'''
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
'''