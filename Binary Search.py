def binary_search(key, array, LB, UB):
    """This function returns the key index using a recursive binary search algorithm"
    """
    
    if UB < LB:
        return -1
    else:
        MP=(LB+UB)/2
        MP=round(MP)

        
    if array[MP] < key:
        return binary_search(key,array, MP+1, UB)
    elif array[MP] > key:
        return binary_search(key,array,LB, MP-1)
    else:
        return MP

#tests
test_array=["Aardvark", "Badger", "Cat", "Dog", "Eagle", "Frog", "Gecko", "Honey Badger",
            "Iguanua", "Jackal", "Kid", "Llama", "Monkey", "Narwhal", "Ostrich", "Penguin",
            "Quail", "Rhino", "Snake", "Tapir", "Upupa", "Viper", "Whale", "Xenon",
            "Yellow Mongoose", "Zebra"]

test_cases= ["Viper", "Buffalo", "Hedgehog", "Jackal", "Kid", "Seahorse", "Penguin"]
for case in test_cases:
    position = binary_search(case, test_array, 0, len(test_array)-1) + 1
    if position > 0:
        print (case, "is found at position", position)
    else:
        print (case, "not found in the array")
