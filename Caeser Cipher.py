#Ceaser Cipher              |
#Project by Hasan Salam     |
#20/11/2016                 |
#----------------------------
users_word=input("Please type in the word you would like to get ciphered.")
cipher_amount=int(input("Please input the number of shifts you would like your Caeser Cipher to contain."))
users_wordlist=list(users_word) #Changes the users word into a list.
text = [] #Creates an empty list
for i in users_word: #Iteratres through the word and adds each letter's ASCII form into the list.
    text.append(int(ord(i)))
index=0 #Sets a counter to 0.
for i in text: #This loop will cipher the phrase...
    text[index]=text[index]+(cipher_amount) #Will add the shift amount to the index.
    if users_wordlist[index].isupper(): #If the respected letter is uppercase...
        while text[index]>90: #While the shift amount exceedes Capital Z (90)
            number_to_add=(text[index])-90 #Minus 90 from the Index's Value and store as the remaining shift amount.
            text[index]=65 #Set the Index's value to 65 (A)
            text[index]=text[index]+(number_to_add) #Add the remaining shift amount. Will loop if it is again exceeding capial Z (90)
    else: #If the respected letter is lowercase...
        while text[index]>122: #If the shift amount exceeds lower z (122)
            number_to_add=(text[index])-122 #Minus the Index's Value by 122 and store as the remaining shift amount.
            text[index]=97 #Set the indexes value to 97 (a)
            text[index]=text[index]+(number_to_add) #Add the remaining shift amonut. Will loop if it is again exceeding lower a (97)
    index+=1 #Adds one to the index, to go to the next letter.
index=0 #Resets the counter
ciphered_word=[] #Creates an empty list to store the ciphered word.
for i in text: #Goes through each ordinal value and converts it into a character, then adding it to the list.
    ciphered_word.append(chr(text[index]))
    index+=1
string_format="".join(ciphered_word) #Will convert the ciphered word into a string.
print (string_format)#Finally prints the ciphered word.
