n=int(input())
x=[]
for i in range(n):
    a= input().split(",")
    b=0
    for j in a:
        if j.islower()==True:
            b+=1
        if b==len(a):
            x.append(tuple(a))
    print(x)