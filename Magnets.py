total=int(input())-1
count=1
tmp=int(input())
for _ in range(total):
    current = int(input())
    if(tmp!=current):
        count+=1
        tmp=current
print(count)