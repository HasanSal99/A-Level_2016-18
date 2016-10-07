CarLength=3

#Speed
def speed(DistanceToAddRT, Speed):
    DistanceToAdd=(Speed)/10
    DistanceToAdd = int(round(DistanceToAdd))
    DistanceToAdd = (DistanceToAdd)*(CarLength)
    DistanceToAdd = (Speed)*(DistanceToAddRT)
    return (DistanceToAdd)    

#Distance from front cause car
def vehicletype(VehicleType):
    if VehicleType==("Lorry"):
        DistanceToAddRT=(CarLength)*4
        return (DistanceToAddRT)
    else:
        return ("0")
        
    
#Calculates the distance between vehicles
def equidistant(FrontVehicle, BackVehicle):
    Target=(FrontVehicle+BackVehicle)/2
    return (Target)

#The main code.    
def main():
    FrontVehicle=int(input("In metres, how far from you is the vehicle in front?"))
    BackVehicle=int(input("In metres, how far from you is the vehicle behind?"))
    VehicleType=input("Is the vehicle infront a Car or a Lorry?")
    Target=equidistant(FrontVehicle, BackVehicle)
    print ("------")
    print ("Situation 1:")
    print ("Road Condition: Normal")
    print ("Vehicle type in front: Normal")
    print ("Vehicle Speed: 10mph")
    print ("------")
    print ("You should be inbetween", str(Target) + "m from both cars.")
    print ("------------------------------------------------------------")
    FrontVehicle=int(input("In metres, how far from you is the vehicle in front?"))
    BackVehicle=int(input("In metres, how far from you is the vehicle behind?"))
    VehicleType=input("Is the vehicle infront a Car or a Lorry?")
    DistanceToAddRT=vehicletype(VehicleType)
    Speed=int(input("How fast is your vehicle travelling?"))
    DistanceToAddRS=speed(DistanceToAddRT, Speed)
    FrontVehicle=(FrontVehicle)+(DistanceToAddRS)+(DistanceToAddRT)
    Target=equidistant(FrontVehicle, BackVehicle)
    print ("------")
    print ("Situation 2:")
    print ("Road Condition: Normal")
    print ("Vehicle type in front:", VehicleType)
    print ("Vehicle Speed:", Speed,"mph")
    print ("------")
    print ("You should be inbetween", str(Target) + "m from both cars.")
    print ("------------------------------------------------------------")
    
              
              
    
    
    

#while True:
if __name__ == "__main__":
        main()
