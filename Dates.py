import datetime
n=int(input())
for i in range(n):
    D,M,Y=map(str,input().split('-'))
    x=int(input())
    wow=datetime.datetime.strptime(M ,"%B")
    pd=datetime.date(int(D),wow.month,int(Y))
    pd+=datetime.timedelta(days=x)
    print("Case "+str(i+1)+": "+pd.strftime("%Y-%B-%d"))