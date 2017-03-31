import random
import time
def speed_mph(time1, time2, distance):
    time_taken=time2-time1
    speed=distance/time_taken
    speed=speed*60
    return (str(round(speed)) +"mph.")

"""while True:
    time.sleep(0.5)
    camera1=1400
    time_to_add=random.uniform(0.6,1.5)
    camera2=camera1+time_to_add
    print ("The car was travelling at", speed_mph(camera1,camera2,1))"""



def validate_plates(numb_plate,index):
    try:
        int_value = int(numb_plate[index])
    except ValueError:
        count=0
    else:
        return ("Not Valid")
    try:
        int_value = int(numb_plate[index+1])
    except ValueError:
        count=0
    else:
        return ("Not Valid")
    try:
        int_value = int(numb_plate[index+2])
    except ValueError:
        return ("Not Valid")
    else:
        count=0
    try:
        int_value = int(numb_plate[index+3])
    except ValueError:
        return ("Not Valid")
    else:
        count=0
    try:
        int_value = int(numb_plate[index+4])
    except ValueError:
        count=0
    else:
        return ("Not Valid")
    try:
        int_value = int(numb_plate[index+5])
    except ValueError:
        count=0
    else:
        return ("Not Valid")
    try:
        int_value = int(numb_plate[index+6])
    except ValueError:
        count=0
    else:
        return ("Not Valid")
    return ("Valid")
        
    


numb_plate = "GG76HHH"
print (validate_plates(numb_plate, 0))

numb_plate= "SA54LAM"
print (validate_plates(numb_plate, 0))
numb_plate= "G766HER"
print (validate_plates(numb_plate, 0))
numb_plate="KI8IRLL"
print (validate_plates(numb_plate, 0))
numb_plate="LU43KAM"
print (validate_plates(numb_plate, 0))
numb_plate="65LAM42"
print (validate_plates(numb_plate, 0))
