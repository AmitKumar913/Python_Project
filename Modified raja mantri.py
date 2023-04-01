import psycopg2
import random
connection=None
cur=None

Name=[]    #This Name list is use to store the name of the players
player1=[]   #This list is use to store the score of the player1
player2=[]   #This list is use to store the score of the player2
player3=[]   #This list is use to store the score of the player3
player4=[]   #This list is use to store the score of the player4

print("\n-> RULES OF THE GAME ")
print("  -> First Enter Four Names")
print("  -> Second Enter a Number you want to play ")
print("  -> Then Your have to press Enter that assign a random (RAJA,MANTRI,SIPAHI,CHOR) from the list \n")

print("Enter 'FOUR' Beautiful Names : ")
for i in range(4):
    print(i+1," ",end=" ")
    x=input()
    Name.append(x)
input(" -> Press 'Enter' to start the Game ")
print()

list1=['RAJA','MANTRI','SIPAHI','CHOR']
while(1):
    times=int(input(" -> Enter the number of times you want to play : "))

    for w in range(times):   #This loop is run how many time you want to play.
        count=1  #This is for assinging player number
        s1=list1.copy()     #This is for the purpose of removing element one by one to not assign same to other players randomly. 
        vari_mantri=0   #this varible is used to keep the player number who is mantri in each round.
        vari_chor=0     #this varible is used to keep the player number who is chor in each round.
        vari_sipahi=0  #this varible is used to keep the player number who is sipahi in each round.
        vari_raja=0    #this variable is used to keep the player number who is raja in each round.
        for e in range(4):    
            i=random.choice(s1)
            print()
            print("Player",count,"-> ( ",Name[count-1]," ) Press Enter :") 
            input() # it is only used to change the turn of the players.
            match i:
                case 'RAJA':
                    raja=1000
                    if count==1:
                        print(raja)
                        player1.append(raja)
                        vari_raja=count
                    elif count==2:
                        print(raja)
                        player2.append(raja)
                        vari_raja=count
                    elif count==3:
                        print(raja)
                        player3.append(raja)
                        vari_raja=count
                    elif count==4:
                        print(raja)
                        player4.append(raja)
                        vari_raja=count
                case 'MANTRI':
                    mantri=800
                    if count==1:
                        vari_mantri=count
                        player1.append(mantri)
                    elif count==2:
                        vari_mantri=count
                        player2.append(mantri)
                    elif count==3:
                        vari_mantri=count
                        player3.append(mantri)
                    elif count==4:
                        vari_mantri=count
                        player4.append(mantri)
                case 'SIPAHI':
                    sipahi=500
                    if count==1:
                        vari_sipahi=count
                        print(sipahi)
                        player1.append(sipahi)
                    elif count==2:
                        vari_sipahi=count
                        print(sipahi)
                        player2.append(sipahi)
                    elif count==3:
                        vari_sipahi=count
                        print(sipahi)
                        player3.append(sipahi)
                    elif count==4:
                        vari_sipahi=count
                        print(sipahi)
                        player4.append(sipahi)
                case 'CHOR':
                    chor=0
                    if count==1:
                        vari_chor=count
                        player1.append(chor)
                    elif count==2:
                        vari_chor=count
                        player2.append(chor)
                    elif count==3:
                        vari_chor=count
                        player3.append(chor)
                    elif count==4:
                        vari_chor=count
                        player4.append(chor)
            count+=1        
            s1.remove(i)

        print("Now Raja ("," Player -> ",vari_raja," ",Name[vari_raja-1]," ) odered to Sipahi ("," Player - > ",vari_sipahi," ",Name[vari_sipahi-1],") to find out Chor form the rest players")
        print()
        while 1:
            choose=int(input("Sipahi please choose the player who is chore from the rest players: "))
            match choose:
                case choose if choose==vari_mantri:
                    print("\nYou choose the wronge player ")
                    print("\nSo your Score is going to the chor \n")
                    if vari_sipahi==1:
                        player1.pop()
                        player1.append(0)
                        if vari_chor==2:
                            player2.pop()
                            player2.append(500)
                        elif vari_chor==3:
                            player3.pop()
                            player3.append(500)
                        elif vari_chor==4:
                            player4.pop()
                            player4.append(500)
                    elif vari_sipahi==2:
                        player2.pop()
                        player2.append(0)
                        if vari_chor==1:
                            player1.pop()
                            player1.append(500)
                        elif vari_chor==3:
                            player3.pop()
                            player3.append(500)
                        elif vari_chor==4:
                            player4.pop()
                            player4.append(500)
                    elif vari_sipahi==3:
                        player3.pop()
                        player3.append(0)
                        if vari_chor==1:
                            player1.pop()
                            player1.append(500)
                        elif vari_chor==2:
                            player2.pop()
                            player2.append(500)
                        elif vari_chor==4:
                            player4.pop()
                            player4.append(500)
                    elif vari_sipahi==4:
                        player4.pop()
                        player4.append(0)
                        if vari_chor==1:
                            player1.pop()
                            player1.append(500)
                        elif vari_chor==2:
                            player2.pop()
                            player2.append(500)
                        elif vari_chor==3:
                            player3.pop()
                            player3.append(500)
                    break
                case choose if choose==vari_chor:
                    print("\nYou choose the right Player")
                    break
                case _:
                    print("\nPlease Choose again from the rest players")
        
        print("\nRound ",w+1," is finished\n")
    print("\nAll rounds are finished -> ")
    print("\nYou want to play more rounds Press 1 ")
    print("\nFor Game Result Press 0 ")
    inp=int(input())
    match inp:
        case 1:
            pass
        case 0:
            break
        case _:
            print("Please choose the right option\n")
print("\nGame Result ->")
try:
    connection = psycopg2.connect(
    host = "127.0.0.1",
    port = "5432",
    database = "postgres",
    user="postgres",
    password="hunny"
    )
    cur=connection.cursor()

    cur.execute('DROP TABLE IF EXISTS game')

    create_table='''CREATE TABLE IF NOT EXISTS game(
    id      SERIAL PRIMARY KEY,
    name    varchar(40) NOT NULL,
    score   int[],
    total   int
    )'''
    cur.execute(create_table)
    insert_into_table='INSERT INTO game(name,score,total) VALUES (%s,%s,%s)'
    insert_values=[(Name[0],player1,sum(player1)),(Name[1],player2,sum(player2)),(Name[2],player3,sum(player3)),(Name[3],player4,sum(player4))]
    for i in insert_values:
        cur.execute(insert_into_table,i)
    connection.commit()
    cur.execute('SELECT * FROM game')  #Return the data and place into the cursor
    #print(cur.fetchall())   #view the return data use another mehtod fetchall()
    for record in cur.fetchall():
        print(record) 
        print()
except Exception as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
    if cur is not None:
        cur.close()
input()
