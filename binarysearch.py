
n=int(input("Enter number of elements in array: "))
l=[ ]

for i in range(0,n):
    val=int(input("Enter element: "))
    l.append(val)

for j in range(0,n):
    for i in range(0,n-1):
        if l[i]>l[i+1]:
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp

print("Sorted array:",l)

tar=int(input("Enter target element: "))

low=0
high=n-1
found=0

for i in range(0,n):
    mid=(high+low)//2
    if l[mid]==tar:
        found=1
        pos=mid
    else:    
        if tar>l[mid]:
            low=mid+1
        else:
            if tar<l[mid]:
                high=mid-1 

if found==1:
    print("Element ",tar," found @ index ",pos)    
else:
    print("Element not found.")   

