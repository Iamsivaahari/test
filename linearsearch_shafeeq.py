def linearsearch():
  l=[]
  n=int(input("enter the number of elements to be added in the list :"))
  for i in range(0,n):
     a=int(input("enter a number :"))
     l.append(a)
 
  print(l)
  ser=int(input("enter the number to search:"))
  found=0
  for i in range(0,n):
    if l[i]==ser:
      found=1
      b=i
    
    
  
  if found==1:
     print("the element is in ",b,"position")
   
  else:
    print("element not found")
    
linearsearch()

print("press 1 do the program again")
print("press 2 to exit")
c=int(input("enter your choice :"))

while c==1:
   linearsearch()
   
   print("press 1 do the program again")
   print("press 2 to exit")
   c=int(input("enter your choice :"))
   if c==2:
    print("thank you")
    break
   
   
