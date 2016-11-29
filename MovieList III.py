#Movie List
#29/11/2016 -
#H. Salam                   

#---------------

def Film_Viewer():
    print ("\n ---Film Viewer---")
    File = open('MovieList.txt', 'r')
    print ("Below will show a menu of various actions and an associated code. Type the code to perform its respected action.")
    print ("View entire film list. - 1")
    print ("Select a film number to view. - 2")
    Users_Choice = (input("What would you like to do?"))
    File.close()
    if Users_Choice=="1":
        print ("\nThe entire film list is:\n" + File.read())
    else:
        with open('MovieList.txt') as File:
            Films = sum(1 for line in File if line.rstrip('\n'))
        print ("There are", Films, "films that have been watched.")
        Film_Number=int(input("What film number would you like to see?"))
        while Film_Number > Films:
            print ("This number is out of range.")
            Film_Number=int(input("What film number would you like to see?"))
        File = open('MovieList.txt', 'r')
        FilmNum=File.readlines()
        print ("\nThe", (Film_Number), "film viewed was", (FilmNum[Film_Number-1]))
    File.close()
    return ("\n")


def Input_Film():
    print ("\n---Add a film---")
    File=open('MovieList.txt', 'a')
    Film_Name=input("\nWhat's the name of the film you wish to add?")
    File.write(Film_Name+"\n")
    print ("The film '" + Film_Name +"' Has been added.")
    return ("\n")

def Extras():
    print ("\n---About this program---")
    print ("Program was created by H. Salam")
    print ("Program was intended to help the creator organise his films to a basic degree, whilst doing so enhancing his skills in programming with Python. Program will be updated should need be.")
    print ("Updates:")
    print ("29/11/2016 - Program Creation started.")
    print ("29/11/2016 - Program completed.")
    return ("\n")

def Menu():
    print ("--- Hasan's movie list program ---")
    print ("Below will show a menu of various different items and a code associated with it. Simply type the code-number of the item you wish to view.")
    print ("Show Films. - 1")
    print ("Add a Film. - 2")
    print ("About this Program - 3")
    Users_Choice = input("What would you like to do?")
    return (Users_Choice)

def Main():
    Users_Option=(Menu())
    if Users_Option=="1":
        print (Film_Viewer())
    elif Users_Option=="2":
        print (Input_Film())
    elif Users_Option=="3":
        print (Extras())
    return (Main())

print (Main())
