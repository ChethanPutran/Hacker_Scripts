#Importing neccessary modules
import hashlib

#Taking hashed password input from the user
passHash = input("Enter md5 hash: ")
#Taking filename from the user
wordList = input("File name: ")
flag = 0

#Checking the presence of file
try:
    passFile = open(wordList,"r")
except:
    print("No file found")
    quit()    
#Comparing with the available/known hashed password
for word in passFile:
    encodedWord = word.encode('utf-8')
    digest = hashlib.md5(encodedWord.strip()).hexdigest()
    
    if digest == passHash:
        flag = 1 
        print("Password found :)")
        print("Password is :"+word)
        break
   
if flag == 0:
    print("Password/passphrase is not present in the list")    