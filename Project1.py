import string
import random
print("                                                        Word Puzzle Game                                     \n")
print("  Game Rules and Description : ")
print("1. You have to to form the correct word out of a given set of characters ")
print("2. You have to solve this puzzle for 5 words, one at a time")
print("3. For each correct answer +1 score will be rewared ")
print("4. For each wrong answer -1 score will be rewared ")
print()
while True:
    print("1. Enter '1' to Start the Game \n2. Enter '0' to Exit the Game ")
    x=int(input())
    match x:
        case 1:
            sum=0
            n=5
            set={'MOTHER','ELECTRICITY','MONKEY','EARTH','FRIEND','BUILDING','POTATO','TOMATO','THREE','EVERY','MORNING','NIGHT','GHOST','HUMAN','PICTURE','CLASS','SOMEONE'}

            for i in set:
                    print("Arrange the letters to form a valid word: \n")
                    print(''.join(random.sample(i,len(i))))
                    y=input()
                    y=y.upper()
                    if(i==y):
                        sum+=1
                    else:
                        sum-=1
                    n-=1
                    if n==0:
                        break
        case 0:
            print("Exit!")
            break
        case _:
            print("Invalid option")

    print("Your score :",sum)
    print()
