from builtins import int
till=0
till=input()
for i in range(int(till)):
    x=input()
    candy=[int(num) for num in input().split()]
    Bob_total=0
    Alice=candy[0]
    Alice_total=candy[0]
    candy.pop(0)
    step=1
    Bob=0
    Bob_active=0
    go=0
    while(len(candy)):
        if(go==0):
            while(Bob<=Alice and len(candy)):
                Bob+=candy[len(candy)-1]
                candy.pop()
            Bob_total+=Bob
            Alice=0
            go=1
            step+=1
        else:
            while (Bob >= Alice and len(candy)):
                Alice += candy[0]
                candy.pop(0)
            Alice_total += Alice
            Bob = 0
            go = 0
            step+=1
    print(str(step)+" "+str(Alice_total)+" "+ str(Bob_total))
