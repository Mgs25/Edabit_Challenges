import os
import time
import tqdm

def timer(limit):
    os.system('cls')
    reverse = limit
    for i in tqdm.tqdm(range(limit)):
        print("\n")
        print("Time Remaining:",reverse,"s"+" "*120+"Time Elapsed:",i,"s")
        reverse -= 1
        time.sleep(1)
        os.system("cls")
    print("Time Remaining:",reverse,"s"+" "*120+"Time Elapsed:",i,"s")
    print(" "*60+"TIME UP!")
try:
    timer(int(input("Enter Time Limit: ")))
except ValueError:
    print("Please, Specify an Valid Time Limit.")