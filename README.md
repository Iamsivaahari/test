num=int(input("Enter a number :"))
res=0
check=num
while num!=0:
    rem=num%10
    res=(res*10)+rem
    num=num//10

if check==res:
    print(res, "is a palindrome.")
else:
    print(res, "is not a palindrome")
