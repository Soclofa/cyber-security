#Data Security HW 2
#Abraham Soclof 674098915 & Eli Isaacs 569280954


#Macbook Pro – 120 MB/sec per core which is around 2^30 bytes per second. 
#AES has a block size of 16 bits so it can encrypt 2^(30-4) = 2^26 blocks per second which
#is also the amount it can try per second. The number of keys that can be searched in a year is about 2,117 trillion keys. 
# A brute force search requires 2^255 keys to be searched. The time it would take to perform the attack would take 2^255/2117 trillion = 2.7 x 10^61. 


from collections import Counter
import random

letter_frequencies = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
             'N': 6.75,  'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 
             'L': 4.03,  'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 
             'F': 2.23,  'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 
             'V': 0.98,  'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 
             'Z': 0.07}

def encrypt(message, key):

    """Encrypt a string using a Caeser Cipher"""

    #set entire string to lowercase
    message.lower()
    #set result to empty string
    result = ""

    #itterate through every character in the string
    for i in range(len(message)):
        #set variable to current char in string
        char = message[i]
        #add the key to the current char in the string
        if (char != ' '):
            result += chr((ord(char) + key - 97)%26 + 97)

    return result

def brute_force_decrypt(message): 
    """Decrypt a message encrypted in Caeser Cipher using Brute Force"""

    #set count to 1
    count = 1
    #set user input to empty string
    user = ""

    #while loop will run as long as the user does not enter 'n' 
    # or the count does not reach 26 (representing the number of letters in the alphabet)
    while (user != "n" or count >= 27): 
        #increments the key by -1 
        result = encrypt(message, count*-1)
        #prints the result
        print(result)
        #increments the count
        count += 1
        #Recieves user input on how to proceed
        user = input ("Enter 'n' to stop the loop. Enter 'y' to continue\n")

def frequency(message): 
    """Uses frequency analysis to attempt and solve an encrypted message """
    freq = {}

    #note the frequency of each letter
    for letter in message: 
        if letter in freq: 
            freq[letter] += 1
        else: 
            freq[letter] = 1

    #sort the dictionary 
    marklist = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    sortfreq = dict(marklist)

    sortfreq = list(sortfreq.keys())
    result = ""
    for i in range(len(sortfreq)):
        result += sortfreq[i]

    most_frequent = list(letter_frequencies.keys())
    for i in range(len(message)):
        letter = message[i]
        replace_letter = most_frequent[sortfreq.index(letter)]
        message = message.replace(letter,replace_letter,1)

    return message


#Main Program 
message = input("Enter a message:\n")

encrypted_message = (encrypt(message, random.randint(0,25)))

print(encrypted_message)

brute_force_decrypt(encrypted_message)

print(frequency(message))



