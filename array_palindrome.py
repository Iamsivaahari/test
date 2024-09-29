size=int(input("Enter size of array: "))
l=[]
r=[]

for i in range(size):
    n = int(input("Enter any number: "))
    l.append(n)

for num in l:
    res = 0
    check = num
    while num != 0:
        k = num % 10
        res = res * 10 + k
        num = num // 10
    if check == res:
        r.append("Palindrome")
    else:
        r.append("Not Palindrome")

print(r)        
