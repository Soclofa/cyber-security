# Data Security Hw 4
# Abraham Soclof 674098915 & Eli Isaacs 569280954


#Question 1 - There is no way to crack a Hash unless you know the method of a Hash, 
#the length of bits, the method it was encoded. And even then you are still trying to 
# decrypt either 128 or 256 bits of data which is nearly impossible.
# 
# Question 2  
# a) I will use hashing to protect all data and a https protocol to transfer the data securely. 
# b) MAC or Mandatory Access Control can be used to limit access control to anyone attempting
# to access or manupilate transferred data. 

import hashlib

def hash_encrypt(msg):
    "returns an encrypted hash"

    #set msg to byte value in utf-8
    msg = msg.encode('utf-8')

    #ctor for sha256
    hash_msg = hashlib.sha256()

    #Update the hash object with the object in bytes.
    hash_msg.update(msg)
 
    #return the hash in hexadecimal value
    return hash_msg.hexdigest()

def getPasswords(): 
    "Sets username and password and stores in a dictionary"

    profile = {}

    username = input("Enter your username:")

    password = input("Enter a password:")

    password = hash_encrypt(password)

    profile[username] = password
    
getPasswords()


