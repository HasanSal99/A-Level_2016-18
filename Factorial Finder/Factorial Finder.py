#Factorial Finder
#Project by H. Salam
#01/12/2016 -

def iteration():
    print ("\n---Factorial Finder via iteration---")
    value=int(input("Input a value to find its factorials."))
    counter=value
    while counter!=1:
        counter-=1
        value=value*counter
    print (value)
    menu()


def recursion(value,counter):
    if counter!=1:
        counter-=1
        value=value*counter
        recursion(value,counter)
    else:
        menu()

def extras():
    print ("\nAbout this program")
    print ("\nProgram was created by H. Salam")
    print ("Task set by Mr. Gorman as the weekly coding challenge. \nThis program is built to find the factorial of a number in two methods, using iteration or using a recurrsive function. \nA factorial of a number, x, is all of the numbers up to x multiplied by each other. So for 4, it'd be 4*3*2*1=24.\nThe program was created to help explain recurssive functions.")
    print ("Updates:")
    print ("1/12/2016 - Program creation started.")
    print ("1/12/2016 - Iteration complete.")
    print ("1/12/2016 - About this program complete.")
    menu()


def menu():
    print ("\n---Menu---")
    print ("Below shows a list of actions and its corresponding number. Input an actions corresponding number to commit it.")
    print ("Factorial Finder via iteration - 1")
    print ("Factorial Finder via recursion - 2")
    print ("About this program - 99")
    option=int(input("What is your action?"))
    while option!=1 and option!=2 and option!=99:
        print ("\nInvalid option.")
        print ("Below will show a list of actions and it's corresponding number. Input the number of the action you would like to commit.")
        print ("Factorial Finder via iteration - 1")
        print ("Factorial Finder via recursion - 2")
        print ("About this program - 99")
        choice=int(input("What's your choice?"))        
    if option==1:
        iteration()
    elif option==2:
        ("\n---Factorial Finder via recursion---")
        value=int(input("Input a value to find its factorials."))
        counter=value
        recursion(value,counter)
    else:
        extras()

menu()

