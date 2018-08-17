
from RPIO import PWM
from time import sleep
roll = PWM.Servo(0,20000,10)
pitch = PWM.Servo(0,20000,10)
throttle = PWM.Servo(0,20000,10)
yaw = PWM.Servo(0,20000,10)
# start PWM on servo specific GPIO no, this is not the pin no but it is the GPIO no 
roll.set_servo(5,1520)# pin 29
pitch.set_servo(6,1500)# pin 31
throttle.set_servo(13,1150)# pin 33
yaw.set_servo(19,1510)# pin 35    #1505
min_throttle = 1150
max_yaw = 1900
min_yaw = 1100
max_roll = 1900
def arm_with_self_level_on():
    roll.set_servo(5,max_roll)  ## hold  aileron to right when arming or disarming.
    sleep(1)
    throttle.set_servo(13,min_throttle)  #set to zero
    yaw.set_servo(19,max_yaw)  # set to max  (full right yaw)
    ## others to minimum
    print 'SElf level on!!!'
    print 'Display Armed!!!!' 

def disarm_with_self_level_on():
    roll.set_servo(5,max_roll)  ## hold  aileron to right when arming or disarming.
    sleep(1)
    throttle.set_servo(13,min_throttle) # set to zero
    yaw.set_servo(19,min_yaw)  #set to min (full left yaw))
    print 'Display Disarmed!!!!'
try:
 x = raw_input('Are you ready: yes/no') 
 disarm_with_self_level_on() 
 print "Armed!!"
 print "Waiting!!!"
 sleep(1)
 yaw.set_servo(19,1520)
 roll.set_servo(5,1500)
#arm_with_self_level_on()
#print "Disarmed!!"
#except:
 while True:
    #roll.set_servo(5,1520)
    j = int(raw_input('Th: '))
    if(j<1900):
      throttle.set_servo(13,j)
    else: 
      pass
except:
 yaw.stop_servo(19)
 roll.stop_servo(5)
 pitch.stop_servo(6)
 throttle.stop_servo(13)
PWM.cleanup()       

