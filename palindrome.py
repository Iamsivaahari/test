
n = (input("Enter any number: "))
res = 0
check = n

while n != 0:
    k = n % 10
    res = (res * 10) + k
    n = n // 10
    
if check == res:
    print("The number given is a PALINDROME.")
else:
    print("The number given is a  NOT A PALINDROME.")

