row1=int(input("Enter number of ROWS in MATRIX 1: "))
col1=int(input("Enter number of COLUMNS in MATRIX 1: "))
print(" ")
row2=int(input("Enter number of ROWS in MATRIX 2: "))
col2=int(input("Enter number of COLUMNS in MATRIX 2: "))

if row1==row2 and col1==col2:
    mat1=[]
    mat2=[]
    print(" ")
    print("Entering values of MATRIX 1.")
    for i in range(0,row1):
        temp=[]
        for j in range(0,col1):
            val=int(input("Enter value: "))
            temp.append(val)
        mat1.append(temp)

    print(" ")
    print("Entering values of MATRIX 2.")
    for i in range(0,row2):
        temp=[]
        for j in range(0,col2):
            val=int(input("Enter value: "))
            temp.append(val)
        mat2.append(temp)

    print(" ")
    print("MATRIX 1: ")
    for i in range(0,row1):
        te=mat1[i]
        print(te) 

    print(" ")
    print("MATRIX 2: ")
    for i in range(0,row2):
        te=mat2[i]
        print(te)        

    add=[]
    print(" ")
    print("MATRIX ADDITION: ")
    for i in range(0,row1):
        tes=[]
        for j in range(0,col1):
            sum=mat1[i][j]+mat2[i][j]
            tes.append(sum)
        add.append(tes)

    print(" ")
    print(" ")
    print("RESULTANT MATRIX: ")
    for i in range(0,row1):
        te=add[i]
        print(te)
