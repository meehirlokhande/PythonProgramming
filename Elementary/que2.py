<<<<<<< HEAD
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
=======
n=int(input())
x=[]
for i in range(n):
    a= inpt().split(",")
    b=0
    for j in a:
        if j.islower()==True:
            b+=1
        if b==len(a):
            x.append(tuple(a))
>>>>>>> b261723a7a3d494711e40d3daea2069ebb6acbad
    print(x)