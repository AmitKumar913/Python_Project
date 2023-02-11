import random
sum1=0  # it is the sum accumulator for player one
sum2=0  # it is the sum accumulator for player second
sum3=0  # it is the sum accumulator for player third
sum4=0  # it is the sum accumulator for player fourth
Name=[]  # it is for the name of the players
print("\n-> RULES OF THE GAME ")
print("  -> First Enter Four Names")
print("  -> Second Enter a Number you want to play ")
print("  -> Then Your have to choose or Enter a number form (1 to 4) that assign a random (RAJA,MANTRI,SIPAHI,CHOR) from the list \n")

print("Enter 'FOUR' Beautiful Names : ")
for i in range(4):
    print(i+1," ",end=" ")
    x=input()
    Name.append(x)
data={Name[0]:sum1,Name[1]:sum2,Name[2]:sum3,Name[3]:sum4}   # for which player score how much 
input(" -> Press 'Enter' to start the Game ")
print()
list1=['RAJA','MANTRI','SIPAHI','CHOR']
times=int(input(" -> Enter the number of times you want to play : "))
for w in range(times):
    count=1                                      # keeping the player number 
    s1=list1.copy()
    for e in range(4):
        i=random.choice(s1)
        print(count," Player Enter a number :") 
        input() #no use it is only for now your turn
        match i:
            case 'RAJA':
                raja=1000
                if count==1:
                    data[Name[0]]+=raja
                elif count==2:
                    data[Name[1]]+=raja
                elif count==3:
                    data[Name[2]]+=raja
                elif count==4:
                    data[Name[3]]+=raja
            case 'MANTRI':
                mantri=800
                if count==1:
                    data[Name[0]]+=mantri
                elif count==2:
                    data[Name[1]]+=mantri
                elif count==3:
                    data[Name[2]]+=mantri
                elif count==4:
                    data[Name[3]]+=mantri
            case 'SIPAHI':
                sipahi=500
                if count==1:
                    data[Name[0]]+=sipahi
                elif count==2:
                    data[Name[1]]+=sipahi
                elif count==3:
                    data[Name[2]]+=sipahi
                elif count==4:
                    data[Name[3]]+=sipahi
            case 'CHOR':
                chor=0
                if count==1:
                    data[Name[0]]+=chor
                elif count==2:
                    data[Name[1]]+=chor
                elif count==3:
                    data[Name[2]]+=chor
                elif count==4:
                    data[Name[3]]+=chor
        count+=1
        print(i)   #This prints the random assig one from the list for one round
        s1.remove(i)
        #print(s1)
        #print(list1)
    print("\nRound ",w+1," is finished\n")
print("\nFor Game Result Press 'Enter' ")
input()

for t in data:
    print(t,"->",data[t])

