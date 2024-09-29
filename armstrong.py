
n = int(input("Enter any number: "))
res = 0
check = n
count=0
te=n

while te!=0:
    te=te//10
    count+=1

if n < 1000 and n > 99:
    while n != 0:
        k = n % 10
        res = res + k * k * k
        n = n // 10

if check == res:
    print(" The number ",check," is an Armstrong number.")
else:
    print("The number ",check," is not an Armstrong number.")

