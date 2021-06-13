n=int(input())
for x in range(n):
    day,moth,year,t_year=map(int,input().split())
    adder=0
    if(moth==2 and day==29):
        y = year
        while(y<=t_year):
            if((y%4==0 and y%100!=0) or y%400==0):
                adder+=1
            y+=4
        print("Case "+str(x+1)+": "+str(adder-1))
    else:
        print("Case "+str(x+1)+": "+str(t_year-year))
