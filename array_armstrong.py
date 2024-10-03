val=[]
result=[]
size=int(input("Enter size of list: "))
for i in range(0,size):
    num=int(input("Enter the number: "))
    val.append(num)

for i in val:
    rem=0
    check=i
    count=0
    reck=i
    while i!=0:
        i=i//10
        count=count+1

    while reck!=0:
        res=reck%10
        rem=(res**count)+rem
        reck=reck//10
    if check==rem:
        result.append("Yep")
    else:
        result.append("Nope")

print(result)
