import RPi.GPIO as GPIO
import time

#********** robot configuration *************
r=1
Limit_angels = [90,90] #degree
Orgin       = [90,90] #[angel_1, angel_2]
Micro_Step  = 800
CCW_Dir   = GPIO.HIGH
CW_Dir    = GPIO.LOW
Laser_Off = GPIO.LOW
Laser_On  = GPIO.HIGH
laser_frequency= 1000
#********** pin configuration ***************
Pull_1 = 26 #PWM
Dir_1  = 19 #OUTPUT

Pull_2 = 6  #PWM
Dir_2  = 5  #OUTPUT

Laser  = 22 #PWM

Relay_1 = 9  #OUTPUT
Relay_2 = 10 #OUTPUT

#*********** PWM global variables **************
Laser_PWM  = 0

#*********** system global variables ************
motor_1_PullNum = 0
motor_2_PullNum = 0
Current_Angels  = [0,0] #[motor1 , motor2]
#*********** functions implimintation **************
def Pin_init():
    global Pull_1,Dir_1,Pull_2,Dir_2,Laser,Relay_1,Relay_2
    
    GPIO.setmode (GPIO.BCM)
    
    GPIO.setup (Dir_1,GPIO.OUT)
    GPIO.setup (Dir_2,GPIO.OUT)
    GPIO.setup (Pull_1,GPIO.OUT)
    GPIO.setup (Pull_2,GPIO.OUT)
    GPIO.setup (Relay_1,GPIO.OUT)
    GPIO.setup (Relay_2,GPIO.OUT)
    GPIO.setup (Laser,GPIO.OUT)

def System_init():
    global Relay_1,Relay_2,Current_Angels
    Pin_init()
    GPIO.output(Relay_1, GPIO.LOW)
    GPIO.output(Relay_2, GPIO.LOW)
           
def Init_End():
    global Relay_1,Relay_2,Current_Angels
    GPIO.output(Relay_1, GPIO.HIGH)
    GPIO.output(Relay_2, GPIO.HIGH)
          
    Current_Angels = Limit_angels

def Motors_Pulse(M,F):
    global motor_1_PullNum,motor_2_PullNum
    if M ==1:
        GPIO.output(Pull_1, GPIO.HIGH)
    elif M ==2:
        GPIO.output(Pull_2, GPIO.HIGH)
    t = 1/(F*2)
    time.sleep(t)
    if M==1:
        GPIO.output(Pull_1, GPIO.LOW)
    elif M==2:
        GPIO.output(Pull_2, GPIO.LOW)
    time.sleep(t)
    if M==1:
        motor_1_PullNum =  motor_1_PullNum + 1
    elif M ==2:
        motor_2_PullNum =  motor_2_PullNum + 1
    
    

def Stepper_Move(angel_1 , angel_2 ,freq ):
    global frequency , Micro_Step , motor_1_PullNum , motor_2_PullNum , Current_Angels , r , Pull_1,Dir_1,Feed_1,Pull_2,Dir_2,Feed_2,CCW_Dir,CW_Dir,Pull_1_PWM,Pull_2_PWM
    
    if angel_1 < 0:
        angel_1 = 360 + angel_1
    if angel_2 < 0:
        angel_2 = 360 + angel_2
    b_angel_1 = (angel_1 - Current_Angels[0]) * r
    b_angel_2 = (angel_2 - Current_Angels[1]) * r
    
    Pull_1_Num = (abs(b_angel_1) * Micro_Step)/360
    Pull_2_Num = (abs(b_angel_2) * Micro_Step)/360
    while 1:
        
        if motor_1_PullNum < Pull_1_Num :
            Motors_Pulse(1,freq)
        if motor_2_PullNum < Pull_2_Num :
            Motors_Pulse(2,freq)
            
        if motor_1_PullNum >= Pull_1_Num :
            if motor_1_PullNum >= Pull_1_Num :
                break
        if b_angel_1 <0:
            GPIO.output(Dir_1, CW_Dir)
        else:
            GPIO.output(Dir_1, CCW_Dir)
        if b_angel_2 <0:
            GPIO.output(Dir_2, CW_Dir)
        else:
            GPIO.output(Dir_2, CCW_Dir)
            
    motor_2_PullNum = 0     
    motor_1_PullNum = 0 
    Current_Angels [0] =  angel_1
    Current_Angels [1] =  angel_2
            
    

def laser_state(x):
    global Laser
    if x != '0' :
        GPIO.output(Laser, GPIO.HIGH)
    else:
        GPIO.output(Laser, GPIO.LOW)

    

    
    
