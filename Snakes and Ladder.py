import random
counter=100
iteration=-1
x=1
p1=0
p2=0
snakes1=[8,18,26,39,51,54,56,60,75,83,85,90,92,97,99]
snakes2=[4,1,10,5,6,36,1,23,28,45,59,48,25,87,63]
ladder1=[3,6,11,15,17,22,38,49,57,61,73,81,88]
ladder2=[20,14,28,34,74,37,59,67,76,78,86,98,91]
print()
print("\t\t\t\t\t\t\t\t","Welcome To Snake And Ladder Game\n")
print("---------------------------------------------------------------------------Game Board----------------------------------------------------------------------------------");
print("\t\t\t\t\t",end='')
while (counter > 0):
            if (counter%10 == 0 and counter != 100):
                if(iteration==-1):
                    counter-=9
                    iteration=1
                    print();
                else:
                    print(counter,"\t",end='')
                    counter-=10
                    iteration=-1
                    print()
                if(counter!=0):
                    print("\n","\t\t\t\t\t",counter,"\t",end='')          
            else:
                print(counter,"\t",end='')
            counter+=iteration;
print("");
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------");
while(p1<100 and p2<100):
        t=input("Enter")
        if(x%2==0):
            n=random.randint(1,6)
            if (p1+n>=100):
                print("Player 1 Wins")
                break
            else:
                p1=p1+n
                for i in snakes1:
                    if(p1==i):
                        q=snakes1.index(i)
                        p1=snakes2[q]
                for a in ladder1:
                    if(p1==a):
                        o=ladder1.index(a)
                        p1=ladder2[o]
                print("Player 1:",p1)
                x=x+1
        else:
            n=random.randint(1,6)
            if (p2+n>=100):
                print("Player 2 Wins")
                break
            else:
                p2=p2+n
                for x in snakes1:
                    if(p2==x):
                        s=snakes1.index(x)
                        p2=snakes2[s]
                for b in ladder1:
                    if(p2==b):
                        n=ladder1.index(b)
                        p2=ladder2[n]
                print("Player 2:",p2)
                x=x+1
            
