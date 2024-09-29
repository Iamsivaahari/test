a=int(input("enter a number : "))
check=a
res=0
s=a
count=0
while s!=0:
    s=s//10
    count=count+1
while a!=0:
    rem=a%10
    res=res+(rem**count)
    a=a//10
if res==check:
    print("number is an armstrong number")
else:
    print("number is not an armstrong number")
