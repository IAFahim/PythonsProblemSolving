import itertools
import re
#commands
var="var"
terminate="exit"
plot="plot"
AND="and"
OR="or"
NOT="not"
VAR=[]
while(True):
    arr=input().lower()

    # declare var
    if(var in arr):
        if (len(arr)==3):#auto declare
            VAR.append(chr(len(VAR)+65))
        if(len(arr)==5):#add Cap Char remove if same
            hold=arr[len(arr) - 1].upper()
            VAR.append(hold);
            for i in range(len(VAR)-1):#add and pop 2
                if hold==VAR[i]:
                    VAR.pop(i)
                    VAR.pop(i-1)
                    break
     #plots
    elif(plot in arr and len(VAR)!=0):
        table = list(itertools.product([True, False], repeat=len(VAR)))# binary plot
        print("NO.\t",end='')
        print(*VAR,sep='\t\t')
        for no,i in enumerate(table,1):
            print(no,end='\t')
            print(*i,sep='\t')

    #exit
    elif(terminate in arr):# exit
        exit()
    #it says down
    #at end print all var
    if(0<len(VAR)):
        print("\t\t\t\t\t\t\tvariables")
    for i in VAR:
        print("\t\t\t\t\t\t\t"+i)

    # p and q
    logic_found=0
    header_kill=False
    if (AND in arr):
        arr= arr.replace(' and ',')&(')
        logic_found+=1
    if (OR in arr):
        arr= arr.replace(' or ',')|(')
        logic_found+=1
    if (NOT in arr):
        arr= arr.replace(' cannot ','!(');
        logic_found+=1
    if (NOT in arr):
        arr= arr.replace('not ','!(');
        logic_found+=1
    if(arr[0]!='(' and arr[1]!='(' and not(header_kill)):
        arr='('+arr
    if(arr[len(arr)-1]!=')'):
        for i in range(logic_found):
            arr+=')'
    if(0<logic_found):
        print(arr)
    #arr="alpha.Customer (cus_Y4o9qMEZAugtnW) ..."
    txt = re.search("\(.*?\)", arr)

    print (txt.group())
    #logic
