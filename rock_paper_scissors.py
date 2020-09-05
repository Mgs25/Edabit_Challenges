import random
import time
import os
import msvcrt

def RPS():
    banner()
    gameOptions = ["rock","paper","scissor"]
    wins = [("rock","scissor"),("paper","rock"),("scissor","paper")]
    userCall = input("Rock, Paper or Scissor? ")
    botCall = random.choice(gameOptions)
    if userCall not in gameOptions:
        print("Invalid Option!")
        exit()
    print("\n******GAME RESULTS*******")
    print("Player\t| Computer")
    print(userCall.capitalize()+"\t| "+botCall.capitalize())
    print("*************************")
    if userCall != botCall:
        if (userCall,botCall) in wins:
            return "p1"
        else:
            return "p2"
    else:
        return "Draw"

def banner():
    print("*********ROCK PAPER SCISSORS*********")

def wait():
    msvcrt.getch()

def getchoice():
    banner()
    print("""1.Single Match
2.BestOfX""")
    choice = int(input("Enter Game Choice(1,2): "))
    return choice

def getResult(roundNumber):
    os.system('cls')
    pScore,cScore = 0,0
    for i in range(roundNumber):
        print("\nCURRENT ROUND:"+str(i+1))
        currentRound = RPS()
        if currentRound == "p1":
            print("\tYOU WON!")
            pScore += 1
        elif currentRound == "p2":
            print("\tYOU LOSE!")
            cScore += 1
        else:
            print("IT'S A DRAW!")
        print("\n*****CURRENT SCORE*****")
        print("Player:"+str(pScore),"\tBot:"+str(cScore))
        if(i+1 != roundNumber):
            print("\nPress any key to continue...")
            wait()
        else:
            print("\nGame End! Press any key to view the results..")
            wait()
        os.system('cls')

    if pScore == cScore:
        return "Draw"
    elif pScore > cScore:
        return "p1"
    elif pScore < cScore:
        return "p2"

def main():
    userChoice = getchoice()
    if userChoice == 1:
        getResult()
    elif userChoice == 2:
        roundNumber = int(input("Enter Number of Rounds: "))
        boXresults = getResult(roundNumber)
        if boXresults == "p1":
            print("You Won Computer!")
        elif boXresults == "p2":
            print("You Lost To Computer!")
        else:
            print("The Game Draw!")

if __name__ == '__main__':
        main()