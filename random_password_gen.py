import random
import string
import os

def main():
  os.system('cls')
  alphaNumeric = list(string.ascii_letters+"1234567890")
  password = ""
  passLen = input("Enter Password Size: ") 
  for i in range(int(passLen)):
      password += random.choice(alphaNumeric)
  print(password)

if __name__ == '__main__':
    main()