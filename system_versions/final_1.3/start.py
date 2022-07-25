G_CO=[0,0,0,423] #[0,430]
Orgin=[0,423]
Data=[0]
int_data=[0]
float_data=[0]
detect=0
sign_detect_x=0
sign_detect_y=0
G90_CO=0
G91_CO=0
G0_act=0
G1_act=0

import math 
import numpy as np
from tqdm import tqdm
import Hard_Ware

lenth = 0.20 #upper links
lenth_2 = 0.25 #motor links
motor_distance=0.20
Data_1= [0]
Data_2= [0]
Data_3= [0]
Data_4= [0]
Data_ideal=[0]

progress=0

G00_freq = 4000#hz
G01_freq = 3000 #hz
resolution = 0.1 #resulolution of G00 and G01
offset = 375
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

def Inverse_Kinamatics_Solution_1(X,Y): 
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
                        
                pthai_1 = math.acos(((lenth_2**2)+(K1**2)-(lenth**2))/(2*lenth_2*K1))
                        
                if ((lenth_2**2)+(K2**2)-(lenth**2)) <= (2*lenth_2*K2):    
                    pthai_2 = (math.acos(((lenth_2**2)+(K2**2)-(lenth**2))/(2*lenth_2*K2)))*(-1)
    
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
                        
                pthai_1 = (math.acos(((lenth_2**2)+(K1**2)-(lenth**2))/(2*lenth_2*K1)))*(-1)
                        
                if ((lenth_2**2)+(K2**2)-(lenth**2)) <= (2*lenth_2*K2):    
                    pthai_2 = math.acos(((lenth_2**2)+(K2**2)-(lenth**2))/(2*lenth_2*K2))
    
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

def G00(current_point,next_point , solution):
    global G0_act, G00_freq,resolution
    angel= [0,0]
    slop=0
    y_sec=0
    coo=[0,0]
    itterator=0
    if next_point[0] != current_point[0]:
        slop=((next_point[1]-current_point[1])/(next_point[0]-current_point[0]))
        y_sec= (next_point[1])-(next_point[0]*slop)
        
        if next_point[0] > current_point[0]:
            itterator = current_point[0]
            while itterator <= next_point[0]:
                via = (slop*itterator) + y_sec
                if solution == 1:
                    angel = list(Inverse_Kinamatics_Solution_1(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                
                elif solution == 2:
                    angel = list(Inverse_Kinamatics_Solution_2(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                elif solution == 3:
                    angel = list(Inverse_Kinamatics_Solution_3(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                elif solution == 4:
                    angel = list(Inverse_Kinamatics_Solution_4(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                            
                itterator = itterator + resolution
                
            itterator=0 #initialize the itterator
            
        elif next_point[0] < current_point[0]:
            itterator = current_point[0]
            while itterator >= next_point[0]:
                via = (slop*itterator) + y_sec
                if solution == 1:
                    angel = list(Inverse_Kinamatics_Solution_1(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                
                elif solution == 2:
                    angel = list(Inverse_Kinamatics_Solution_2(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                elif solution == 3:
                    angel = list(Inverse_Kinamatics_Solution_3(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                elif solution == 4:
                    angel = list(Inverse_Kinamatics_Solution_4(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                            
                itterator = itterator - resolution
                
            itterator=0 #initialize the itterator 
        
    elif next_point[0] == current_point[0]:
        if next_point[1] < current_point[1]:
            itterator = current_point[1]
            while itterator >= next_point[1]:
                if solution == 1:
                    angel = list(Inverse_Kinamatics_Solution_1(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                
                elif solution == 2:
                    angel = list(Inverse_Kinamatics_Solution_2(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                elif solution == 3:
                    angel = list(Inverse_Kinamatics_Solution_3(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                elif solution == 4:
                    angel = list(Inverse_Kinamatics_Solution_4(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                            
                itterator = itterator - resolution
                
            itterator=0 #initialize the itterator               
        elif next_point[1] > current_point[1]:
            itterator = current_point[1]
            while itterator <= next_point[1]:
                if solution == 1:
                    angel = list(Inverse_Kinamatics_Solution_1(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                
                elif solution == 2:
                    angel = list(Inverse_Kinamatics_Solution_2(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                elif solution == 3:
                    angel = list(Inverse_Kinamatics_Solution_3(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                elif solution == 4:
                    angel = list(Inverse_Kinamatics_Solution_4(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G00_freq )
                            
                itterator = itterator + resolution
                
            itterator=0 #initialize the itterator 
     
    return next_point
    
def G01(current_point,next_point , solution):
    
    global G0_act, G01_freq,resolution
    angel= [0,0]
    slop=0
    y_sec=0
    coo=[0,0]
    itterator=0
    if next_point[0] != current_point[0]:
        slop=((next_point[1]-current_point[1])/(next_point[0]-current_point[0]))
        y_sec= (next_point[1])-(next_point[0]*slop)
        
        if next_point[0] > current_point[0]:
            itterator = current_point[0]
            while itterator <= next_point[0]:
                via = (slop*itterator) + y_sec
                if solution == 1:
                    angel = list(Inverse_Kinamatics_Solution_1(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                
                elif solution == 2:
                    angel = list(Inverse_Kinamatics_Solution_2(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                elif solution == 3:
                    angel = list(Inverse_Kinamatics_Solution_3(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                elif solution == 4:
                    angel = list(Inverse_Kinamatics_Solution_4(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                            
                itterator = itterator + resolution
                
            itterator=0 #initialize the itterator
            
        elif next_point[0] < current_point[0]:
            itterator = current_point[0]
            while itterator >= next_point[0]:
                via = (slop*itterator) + y_sec
                if solution == 1:
                    angel = list(Inverse_Kinamatics_Solution_1(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                
                elif solution == 2:
                    angel = list(Inverse_Kinamatics_Solution_2(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                elif solution == 3:
                    angel = list(Inverse_Kinamatics_Solution_3(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                elif solution == 4:
                    angel = list(Inverse_Kinamatics_Solution_4(itterator,via))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                            
                itterator = itterator - resolution
                
            itterator=0 #initialize the itterator 
        
    elif next_point[0] == current_point[0]:
        if next_point[1] < current_point[1]:
            itterator = current_point[1]
            while itterator >= next_point[1]:
                if solution == 1:
                    angel = list(Inverse_Kinamatics_Solution_1(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                
                elif solution == 2:
                    angel = list(Inverse_Kinamatics_Solution_2(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                elif solution == 3:
                    angel = list(Inverse_Kinamatics_Solution_3(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                elif solution == 4:
                    angel = list(Inverse_Kinamatics_Solution_4(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                            
                itterator = itterator - resolution
                
            itterator=0 #initialize the itterator               
        elif next_point[1] > current_point[1]:
            itterator = current_point[1]
            while itterator <= next_point[1]:
                if solution == 1:
                    angel = list(Inverse_Kinamatics_Solution_1(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                
                elif solution == 2:
                    angel = list(Inverse_Kinamatics_Solution_2(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                elif solution == 3:
                    angel = list(Inverse_Kinamatics_Solution_3(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                elif solution == 4:
                    angel = list(Inverse_Kinamatics_Solution_4(current_point[0],itterator))
                    coo=list(Forward_Kinamatics(angel[0],angel[1]))
                    if coo[0] != 0:
                        if coo[1] != 0:
                            Hard_Ware.Stepper_Move(angel[0] , angel[1] ,G01_freq )
                            
                itterator = itterator + resolution
                
            itterator=0 #initialize the itterator 
     
    return next_point
    

def System_Start(path,S):
    
    global G_CO,Data,int_data,float_data,detect,sign_detect_x,sign_detect_y,G90_CO,G91_CO,G0_act,G1_act,progress,offset
    file = open(path,'r') 
    x = list(file.readlines())
    file_len = len(x) 
    for a in tqdm(range(file_len)):
        progress = (a/file_len)*100
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
                    Hard_Ware.laser_state('0')
                    
                    
                elif x[a][b+1] == '1':
                    G0_act = 0
                    G1_act = 1
            
            elif x[a][b] == 'S':
                    Hard_Ware.laser_state(x[a][b+1])
            elif x[a][b] == 'M':
                if x[a][b+1] == '5':
                    Hard_Ware.laser_state('0')
            
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
                                sign_detect_x=1
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
                    if sign_detect_x == 1:
                        buffer_x = buffer_x *(-1)
                        
                    G_CO[0]=buffer_x #pug
                    int_data=[0]
                    float_data=[0]
                    Data=[0]
                    sign_detect_x=0
                            
                elif G1_act == 1:
                    for c in range(1,10):
                        if x[a][b+c] != ' ':
                            Data.append(x[a][b+c])
                        else:
                            break
                    for d in range(1,len(Data)):
                        if Data[d] != '.':
                            if Data[d] == '-':
                                sign_detect_x=1
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
                    if sign_detect_x == 1:
                        buffer_x = buffer_x *(-1)
                        
                    G_CO[0]=buffer_x
                    int_data=[0]
                    float_data=[0]
                    Data=[0]
                    sign_detect_x=0       
                     
            
            elif x[a][b] == 'Y': #coordinations:
                if G0_act == 1:
                    for c in range(1,10):
                        if x[a][b+c] != ' ':
                            Data.append(x[a][b+c])
                        else:
                            break
                    for d in range(1,len(Data)):
                        if Data[d] != '.':
                            if Data[d] == '-':
                                sign_detect_y=1
                                continue
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
                    if sign_detect_y == 1:
                        buffer_y = buffer_y *(-1)
                    G_CO[1]=buffer_y + offset
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
                            if Data[d] == '-':
                                sign_detect_y=1
                                continue
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
                    if sign_detect_y == 1:
                        buffer_y = buffer_y *(-1) 
                    G_CO[1]=buffer_y + offset
                    int_data=[0]
                    float_data=[0]
                    Data=[0]
                    sign_detect_y=0
                    
        #if G90_CO == 1:
            #print("absolute coordination")
        #if G91_CO == 1:
            #print("increamental coordination")    
            
        if G0_act == 1:           
            G_CO[2:]=G00(G_CO[2:] , G_CO[0:2] , S)       
           
    
        if G1_act == 1: 
            G_CO[2:]=G01(G_CO[2:] , G_CO[0:2] , S)
            
    file.close()
    G00(G_CO[2:] , Orgin , S) #back to orgin
    
#Hard_Ware.System_init()
#Hard_Ware.Init_End()
#G01([0,423],[100,423] , 1)
#print("R")
#G01([100,423],[100,300] , 1)
#print("D")
#G01([100,300],[0,300] , 1)
#print("L")
#G01([0,300],[0,423] , 1)
#print("U")