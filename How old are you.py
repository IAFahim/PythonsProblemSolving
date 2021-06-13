x=input()
while len(x)==0:
    x=input()
x=int(x)
for n in range(1,x+1):
    _=input()
    t_dd,t_mm,t_yyyy=map(int,input().split('/'))
    y_dd,y_mm,y_yyyy=map(int,input().split('/'))
    year = int(t_yyyy) - int(y_yyyy)
    month = int(t_mm) - int(y_mm)
    date = int(t_dd) - int(y_dd)
    if (month == 0 and date < 0):
        date = -1
    else:
        date = 0
    if (month >= 0):
        month = 0
    else:
        month = -1
    res = year + month + date
    if (res < 0):
        print("Case #" + str(n) + ":", "Invalid birth date")
    elif (res > 130):
        print("Case #" + str(n) + ":", "Check birth date")
    else:
        print("Case #" + str(n) + ":", res)
