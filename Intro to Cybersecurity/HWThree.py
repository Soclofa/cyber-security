# Data Security HW 3
#Abraham Soclof 674098915
#Eli Isaacs 569280954


from base64 import urlsafe_b64encode, urlsafe_b64decode 
from Crypto.Cipher import AES

from Crypto import Random

from Crypto.Util.Padding import pad, unpad 

#A list of possible Car brands
brands = [
  "Abarth", "Audi","Bentley","Bmw",
  "Bugatti","Cadillac","Chevrolet","Chrysler", "Citroen","Dacia","Daewoo",
  "Daihatsu", "Dodge","Donkervoort","DS","Ferrari","Fiat","Fisker","Ford","Honda",
  "Hummer", "Hyundai","Infiniti", "Iveco", "Jaguar","Jeep","Kia", "KTM","Lada",
  "Lamborghini","Lancia","Landwind","Lexus","Lotus","Maserati", "Maybach",
  "Mazda","McLaren","Mercedes-Benz","MG","Mini","Mitsubishi","Morgan","Nissan","Opel",
  "Peugeot","Porsche","Renault","Rover","Saab","Seat","Skoda","Smart",
  "SsangYong","Subaru","Suzuki","Tesla","Toyota","Volkswagen","Volvo"
]

##############################################################
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
base64pad = lambda s: s + '=' * (4 - len(s) % 4)
base64unpad = lambda s: s.rstrip("=")
##############################################################


def getKey(key):
    """Returns a key in the format 'BranddnarBJCTjct'"""
    reversed = key[::-1]
    key += reversed
    key += "JCTjct"
    return key


def decrypt(encrypted_message, key):
    #pads and sets the message in bytes
    encrypted_message = urlsafe_b64decode(base64pad(encrypted_message))
    #The first 16 bytes of the message represent the IV
    iv = encrypted_message[:16]
    #create a new cipher with the key and iv
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=AES.block_size * 8)
    #unpad and return the decrypted message 
    return  unpad(cipher.decrypt(encrypted_message[16:]))




message = "YZmWUTcEvGi_5pa-GJBT97nXBQumS8Vd617_xK_LNzSmTudgmWN41Hd_QS_tRv8d"

#for loop itterates through the entire list of brands and attempts to decrypt the message
#all wrong keys will cause a runtime error. The try statement allows for the code to continue to 
# to itterate through the loop until the correct key is found and input. 

for brand in brands: 
    try:
        key = bytes(getKey(brand), 'utf-8')
        decrypted_message = decrypt(message,key)
    except:
        continue

print(f"Key: {key.decode()} Message: {decrypted_message.decode()}")

#Output

#Key: VolvoovloVJCTjct Message: Hello Cyber Course 2020
