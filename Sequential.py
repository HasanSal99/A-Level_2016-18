myList=[]
stopper=0
while stopper!="1":
    myList.append(input ("Input a letter."))
    stopper=(input("Anything to add 1 to continue."))

item=input("What is the letter you are looking for?")
pointer=0
listLength=len(myList)
while pointer<listLength and myList[pointer]!=item:
    pointer+=1
if pointer >=listLength:
    print ("Item is not in the list")
else:
    print ("It is indexed at location "+ str(pointer))
    print ("It is located at location "+ str(pointer + 1)
    


def linear_search(key, array, index):
    """ Function to return index of key in array using
        a recursive linear search
        """
    if index == len(array):#Checks if the whole list has been checked.
           #If no value found, -1 is returned
        return -1
    elif array[index] != key: #If the key does not equal the current index
        return linear_search(key, array, index + 1) #Recursive - Retuens the same, with an increased index
    else:
        return index #Returns the position when the value is found
