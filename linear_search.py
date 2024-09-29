n = int(input("enter the size of your array: "))
arr1 = []
found=0
c=0
for i in range(0,n):
    s=int(input("enter the values: "))
    arr1.append(s)
num=int(input("enter the number you want to find: "))
target=num
for i in range(0,n):
    if arr1[i]==target:
        found=1
        c=i
    
if found==1:
    print("element found in ",c+1,)
else:
    print("target not found")