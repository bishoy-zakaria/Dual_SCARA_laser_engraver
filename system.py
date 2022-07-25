G_CO=[0,0,0,0]
Data=[0]
int_data=[0]
float_data=[0]
detect=0
sign_detect=0
G90_CO=0
G91_CO=0
G0_act=0
G1_act=0


import math 
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

lenth = 0.20 #upper links
lenth_2 = 0.25 #motor links
motor_distance=0.20
Data_1= [0]
Data_2= [0]
Data_3= [0]
Data_4= [0]
Data_ideal=[0]

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
    
        X = (X_a + (lenth*math.cos(gama)))*1000 # mm 
        Y = (Y_a + (lenth*math.sin(gama)))*1000
    
    return X,Y

def Inverse_Kinamatics_Solution_1(X,Y): #the best
    global lenth,lenth_2,motor_distance
    theta_1=0 
    theta_2=0
    X=X/1000
    Y=Y/1000
    K1 = math.sqrt(((X+(motor_distance/2))**2)+(Y**2))
    K2 = math.sqrt(((X-(motor_distance/2))**2)+(Y**2))
    
    if K1 != 0:
        if K2 !=0: 

            if ((lenth_2**2)+(K1**2)-(lenth**2)) <= (2*lenth_2*K1): 
                        
                pthai_1 = math.acos(((lenth_2**2)+(K1**2)-(lenth**2))/(2*lenth_2*K1))
                        
                if ((lenth_2**2)+(K2**2)-(lenth**2)) <= (2*lenth_2*K2):    
                    pthai_2 = math.acos(((lenth_2**2)+(K2**2)-(lenth**2))/(2*lenth_2*K2))
    
                    zeta_1 = math.atan2(Y,(X+(motor_distance/2)))
                    zeta_2 = math.atan2(Y,(X-(motor_distance/2)))
    
                    theta_1 = zeta_1 + pthai_1  
                    theta_2 = zeta_2 - pthai_2  
                    
    return math.degrees(theta_1) ,math.degrees(theta_2)
  
def Inverse_Kinamatics_Solution_2(X,Y): #the best
    global lenth,lenth_2,motor_distance
    theta_1=0 
    theta_2=0
    X=X/1000
    Y=Y/1000
    K1 = math.sqrt(((X+(motor_distance/2))**2)+(Y**2))
    K2 = math.sqrt(((X-(motor_distance/2))**2)+(Y**2))
    
    if K1 != 0:
        if K2 !=0: 

            if ((lenth_2**2)+(K1**2)-(lenth**2)) <= (2*lenth_2*K1): 
                        
                pthai_1 = (math.acos(((lenth_2**2)+(K1**2)-(lenth**2))/(2*lenth_2*K1)))*(-1)
                        
                if ((lenth_2**2)+(K2**2)-(lenth**2)) <= (2*lenth_2*K2):    
                    pthai_2 = math.acos(((lenth_2**2)+(K2**2)-(lenth**2))/(2*lenth_2*K2))
    
                    zeta_1 = math.atan2(Y,(X+(motor_distance/2)))
                    zeta_2 = math.atan2(Y,(X-(motor_distance/2)))
    
                    theta_1 = zeta_1 + pthai_1  
                    theta_2 = zeta_2 - pthai_2  
                    
    return math.degrees(theta_1) ,math.degrees(theta_2)

def Inverse_Kinamatics_Solution_3(X,Y): #the best
    global lenth,lenth_2,motor_distance
    theta_1=0 
    theta_2=0
    X=X/1000
    Y=Y/1000
    K1 = math.sqrt(((X+(motor_distance/2))**2)+(Y**2))
    K2 = math.sqrt(((X-(motor_distance/2))**2)+(Y**2))
    
    if K1 != 0:
        if K2 !=0: 

            if ((lenth_2**2)+(K1**2)-(lenth**2)) <= (2*lenth_2*K1): 
                        
                pthai_1 = math.acos(((lenth_2**2)+(K1**2)-(lenth**2))/(2*lenth_2*K1))
                        
                if ((lenth_2**2)+(K2**2)-(lenth**2)) <= (2*lenth_2*K2):    
                    pthai_2 = (math.acos(((lenth_2**2)+(K2**2)-(lenth**2))/(2*lenth_2*K2)))*(-1)
    
                    zeta_1 = math.atan2(Y,(X+(motor_distance/2)))
                    zeta_2 = math.atan2(Y,(X-(motor_distance/2)))
    
                    theta_1 = zeta_1 + pthai_1  
                    theta_2 = zeta_2 - pthai_2  
                    
    return math.degrees(theta_1) ,math.degrees(theta_2)

def Inverse_Kinamatics_Solution_4(X,Y): #the best
    global lenth,lenth_2,motor_distance
    theta_1=0 
    theta_2=0
    X=X/1000
    Y=Y/1000
    K1 = math.sqrt(((X+(motor_distance/2))**2)+(Y**2))
    K2 = math.sqrt(((X-(motor_distance/2))**2)+(Y**2))
    
    if K1 != 0:
        if K2 !=0: 

            if ((lenth_2**2)+(K1**2)-(lenth**2)) <= (2*lenth_2*K1): 
                        
                pthai_1 = (math.acos(((lenth_2**2)+(K1**2)-(lenth**2))/(2*lenth_2*K1)))*(-1)
                        
                if ((lenth_2**2)+(K2**2)-(lenth**2)) <= (2*lenth_2*K2):    
                    pthai_2 = (math.acos(((lenth_2**2)+(K2**2)-(lenth**2))/(2*lenth_2*K2)))*(-1)
    
                    zeta_1 = math.atan2(Y,(X+(motor_distance/2)))
                    zeta_2 = math.atan2(Y,(X-(motor_distance/2)))
    
                    theta_1 = zeta_1 + pthai_1  
                    theta_2 = zeta_2 - pthai_2  
                    
    return math.degrees(theta_1) ,math.degrees(theta_2)

def G01(current_point,next_point):
    global G0_act
    slop=0
    y_sec=0
    theta_inverse_1=[0,0]
    theta_inverse_2=[0,0]
    theta_inverse_3=[0,0]
    theta_inverse_4=[0,0]
    if next_point[0] != current_point[0]:
        slop=((next_point[1]-current_point[1])/(next_point[0]-current_point[0]))
        y_sec= (next_point[1])-(next_point[0]*slop)
    
    if current_point[0] < next_point[0]:
        for i in np.arange(current_point[0], next_point[0]+0.1, 0.1):
            via = (slop*i) + y_sec
            theta_inverse_1=Inverse_Kinamatics_Solution_1(i,via) 
            theta_inverse_2=Inverse_Kinamatics_Solution_2(i,via) 
            theta_inverse_3=Inverse_Kinamatics_Solution_3(i,via) 
            theta_inverse_4=Inverse_Kinamatics_Solution_4(i,via) 
            buffer_1=list(Forward_Kinamatics(theta_inverse_1[0],theta_inverse_1[1])) #for simulation
            buffer_2=list(Forward_Kinamatics(theta_inverse_2[0],theta_inverse_2[1])) #for simulation
            buffer_3=list(Forward_Kinamatics(theta_inverse_3[0],theta_inverse_3[1])) #for simulation
            buffer_4=list(Forward_Kinamatics(theta_inverse_4[0],theta_inverse_4[1])) #for simulation
            if i==current_point[0]:
                if G0_act != 1:
                    Data_ideal[0]=[i,via]
                    Data_1[0]=buffer_1
                    Data_2[0]=buffer_2
                    Data_3[0]=buffer_3
                    Data_4[0]=buffer_4
            else:
                if G0_act != 1:
                    Data_1.append(buffer_1)
                    Data_2.append(buffer_2)
                    Data_3.append(buffer_3)
                    Data_4.append(buffer_4)
                    Data_ideal.append([i,via])
    else:
        for i in np.arange(next_point[0], current_point[0]+0.1, 0.1):
            via = (slop*i) + y_sec
            theta_inverse_1=Inverse_Kinamatics_Solution_1(i,via) 
            theta_inverse_2=Inverse_Kinamatics_Solution_2(i,via) 
            theta_inverse_3=Inverse_Kinamatics_Solution_3(i,via) 
            theta_inverse_4=Inverse_Kinamatics_Solution_4(i,via) 
            buffer_1=list(Forward_Kinamatics(theta_inverse_1[0],theta_inverse_1[1])) #for simulation
            buffer_2=list(Forward_Kinamatics(theta_inverse_2[0],theta_inverse_2[1])) #for simulation
            buffer_3=list(Forward_Kinamatics(theta_inverse_3[0],theta_inverse_3[1])) #for simulation
            buffer_4=list(Forward_Kinamatics(theta_inverse_4[0],theta_inverse_4[1])) #for simulation
            if i==next_point[0]:
                if G0_act != 1:
                    Data_ideal[0]=[i,via]
                    Data_1[0]=buffer_1
                    Data_2[0]=buffer_2
                    Data_3[0]=buffer_3
                    Data_4[0]=buffer_4
            else:
                if G0_act != 1:
                    Data_1.append(buffer_1)
                    Data_2.append(buffer_2)
                    Data_3.append(buffer_3)
                    Data_4.append(buffer_4)
                    Data_ideal.append([i,via])
    return next_point
    
    

file = open("cnc.txt",'r') 
x = list(file.readlines())
file_len = len(x) 
for a in tqdm(range(file_len)):
    for b in range(0,(len(x[a]))): #line by line 
        buffer_x=0
        buffer_y=0
        if x[a][b] == 'G': #G90 & G91 & G0 & G1
            if x[a][b+1] == '9':
                if x[a][b+2] == '0':
                    G90_CO=1
                    G91_CO=0
                elif x[a][b+2] == '1':
                    G91_CO=1
                    G90_CO=0
            
            elif x[a][b+1] == '0':
                G0_act = 1
                G1_act = 0
                
            elif x[a][b+1] == '1':
                G0_act = 0
                G1_act = 1
        
        elif x[a][b] == 'X': #coordinations:
            if G0_act == 1:
                for c in range(1,10):
                    if x[a][b+c] != ' ':
                        Data.append(x[a][b+c])
                    else:
                        break
                for d in range(1,len(Data)):
                    if Data[d] != '.':
                        if Data[d] == '-':
                            sign_detect=1
                            continue
                        if detect==0:
                            int_data.append(Data[d])
                        elif detect==1:
                            float_data=Data[d]
                    elif Data[d] == '.':
                        detect=1
                detect=0
                for f in range(1,len(int_data)):
                    buffer_x=buffer_x+(int(int_data[f])*(10**(len(int_data)-f-1)))

                buffer_x= int(buffer_x)+ (int(float_data[0])/(10))
                if sign_detect == 1:
                    buffer_x = buffer_x *(-1)
                    
                G_CO[0]=buffer_x #pug
                int_data=[0]
                float_data=[0]
                Data=[0]
                sign_detect=0
                        
            elif G1_act == 1:
                for c in range(1,10):
                    if x[a][b+c] != ' ':
                        Data.append(x[a][b+c])
                    else:
                        break
                for d in range(1,len(Data)):
                    if Data[d] != '.':
                        if Data[d] == '-':
                            sign_detect=1
                            continue
                        if detect==0:
                            int_data.append(Data[d])
                        elif detect==1:
                            float_data=Data[d]
                    elif Data[d] == '.':
                        detect=1
                detect=0
                
                for f in range(1,len(int_data)):
                    buffer_x=buffer_x+(int(int_data[f])*(10**(len(int_data)-f-1)))

                buffer_x= int(buffer_x)+ (int(float_data[0])/(10))
                if sign_detect == 1:
                    buffer_x = buffer_x *(-1)
                    
                G_CO[0]=buffer_x
                int_data=[0]
                float_data=[0]
                Data=[0]
                sign_detect=0       
                 
        
        elif x[a][b] == 'Y': #coordinations:
            if G0_act == 1:
                for c in range(1,10):
                    if x[a][b+c] != ' ':
                        Data.append(x[a][b+c])
                    else:
                        break
                for d in range(1,len(Data)):
                    if Data[d] != '.':
                        if detect==0:
                            int_data.append(Data[d])
                        elif detect==1:
                            float_data=Data[d]
                    elif Data[d] == '.':
                        detect=1
                detect=0
                
                for f in range(1,len(int_data)):
                    buffer_y=buffer_y+(int(int_data[f])*(10**(len(int_data)-f-1)))

                buffer_y= int(buffer_y)+ (int(float_data[0])/(10))
                    
                G_CO[1]=buffer_y
                int_data=[0]
                float_data=[0]
                Data=[0]
                        
            elif G1_act == 1:
                
                for c in range(1,10):
                    if x[a][b+c] != ' ':
                        Data.append(x[a][b+c])
                    else:
                        break
                for d in range(1,len(Data)):
                    if Data[d] != '.':
                        if detect==0:
                            int_data.append(Data[d])
                        elif detect==1:
                            float_data=Data[d]
                    elif Data[d] == '.':
                        detect=1
                detect=0
                
                for f in range(1,len(int_data)):
                    buffer_y=buffer_y+(int(int_data[f])*(10**(len(int_data)-f-1)))

                buffer_y= int(buffer_y)+ (int(float_data[0])/(10))
                    
                G_CO[1]=buffer_y
                int_data=[0]
                float_data=[0]
                Data=[0]
    #if G90_CO == 1:
        #print("absolute coordination")
    #if G91_CO == 1:
        #print("increamental coordination")    
        
    if G0_act == 1:   
        #print("progress: " , int((a*100)/file_len) , "%")         
        G_CO[2:]=G01(G_CO[2:],G_CO[0:2])       
        Robot_Data=np.array(Data_3) 
        df= pd.DataFrame(Robot_Data)
        writer=pd.ExcelWriter("robot_data.xlsx")
        df.to_excel(writer)
        writer.save()

    if G1_act == 1:
       # print("progress: " , int((a*100)/file_len) , "%")   
        G_CO[2:]=G01(G_CO[2:],G_CO[0:2])       
        Robot_Data=np.array(Data_3) 
        df= pd.DataFrame(Robot_Data)
        writer=pd.ExcelWriter("robot_data.xlsx")
        df.to_excel(writer)
        writer.save()


file.close()

print("e1: ",mean_absolute_error(Data_ideal, Data_1))
print("e2: ",mean_absolute_error(Data_ideal, Data_2))
print("e3: ",mean_absolute_error(Data_ideal, Data_3))
print("e4: ",mean_absolute_error(Data_ideal, Data_4))
plt.plot(Data_3)
plt.show()