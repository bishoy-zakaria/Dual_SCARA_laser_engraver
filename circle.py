import math 
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error

lenth = 0.25 #lenth of all links in robot
lenth_6 = 0.2
Data= [0]
current_point=[5,2]

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

def Inverse_Kinamatics_Solution_1(X,Y): #the best
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
  

def Inverse_Kinamatics_Solution_2(X,Y):
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

def G01(next_point):
    global current_point,Data
    slop=((next_point[1]-current_point[1])/(next_point[0]-current_point[0]))
    y_sec= (next_point[1])-(next_point[0]*slop)
    
    if current_point[0] < next_point[0]:
        for i in np.arange(current_point[0], next_point[0]+0.1, 0.1):
            via = (slop*i) + y_sec
            #Data.append(Inverse_Kinamatics_Solution_1(i,via)) 
            buffer=[i,via]
            if i==current_point[0]:
                Data[0]=buffer
            else:
                Data.append(buffer)
    else:
        for i in np.arange(next_point[0], current_point[0]+0.1, 0.1):
            via = (slop*i) + y_sec
            #Data.append(Inverse_Kinamatics_Solution_1(i,via)) 
            buffer=[i,via]
            if i==next_point[0]:
                Data[0]=buffer
            else:
                Data.append(buffer)
    
    current_point=next_point

    
def Circle(i,j):
    global current_point,Data
    
    Cx= current_point[0]+i
    Cy= current_point[1]+j
    r= math.sqrt((i**2)+(j**2))
    for i in np.arange(Cx-r, Cx+r+0.1, 0.1):
        p=((r**2)-(Cx**2)-(Cy**2))
        s=((i**2)-(2*Cx*i))
        t=p-s
    
        Detect= (((-2*Cy)**2)-(4*(-1*t)))
    
        if Detect>=0:
        
            via = ((2*Cy+math.sqrt(Detect))/2)
            #Data.append(Inverse_Kinamatics_Solution_1(i,via)) 
            buffer=[i,via]
            if i==Cx-r:
                Data[0]=buffer
            else:
                Data.append(buffer)
                
    for i in np.arange(Cx-r, Cx+r+0.1, 0.1):
        p=((r**2)-(Cx**2)-(Cy**2))
        s=((i**2)-(2*Cx*i))
        t=p-s
    
        Detect= (((-2*Cy)**2)-(4*(-1*t)))
    
        if Detect>=0:
        
            via = ((2*Cy-math.sqrt(Detect))/2)
            #Data.append(Inverse_Kinamatics_Solution_1(i,via)) 
            buffer=[i,via]
            if i==Cx-r:
                Data[0]=buffer
            else:
                Data.append(buffer)


Circle(5,2)
Robot_Data=np.array(Data) 
df= pd.DataFrame(Robot_Data)
print(df)
writer=pd.ExcelWriter("robot_data.xlsx")
df.to_excel(writer)

writer.save()

'''
X_True=[0]
Y_True=[0]

X_Train=[0]
Y_Train=[0]

for x in range(-30,31):
    for y in range(-30,31):
        
        X_True.append(x)
        Y_True.append(y)
        
        theta= list(Inverse_Kinamatics_Solution_1(x,y))
        
        Co=Forward_Kinamatics(theta[0],theta[1])
        Co=list(Co)
        
        X_Train.append(Co[0])
        Y_Train.append(Co[1])
        
print(mean_absolute_error(X_True, X_Train))        
print(mean_absolute_error(Y_True, Y_Train))

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
writer.save()'''

