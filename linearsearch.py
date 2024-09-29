n=int(input("Enter number of elements in array: "))
l=[ ]
found=0
pos=0

for i in range(0,n):
    val=int(input("Enter element: "))
    l.append(val)

tar=int(input("Enter target element: "))

for i in range(0,n):
    if l[i]==tar:
        found=1
        pos=i

if found==1:
    print("Element found @ ",pos," index.")
else:
    print("Element not found.")
