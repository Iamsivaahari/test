a=int(input("enter the number:"))
res=0
check=a
while a!=0:
    rem = a%10
    res=(res*10)+rem
    a=a//10

if check==res:
    print(res, "it is a palindrom")
else:
    print(res,"is not a palindrom")
