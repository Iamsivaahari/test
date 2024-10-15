def passwd(pwd):
    ele=[i for i in pwd]
    cu,cl,ci=0,0,0
    if len(ele)>=8:
        for i in ele:
            if i.isupper()==True:
                cu=1
            elif i.islower()==True:
                cl=1
            elif ord(i)>48 and ord(i)<=57:
                ci=1
        if cu==1 and cl==1 and ci==1:
            print("Password Validated.") 
        else:
            print("not working")        
    else:
        print("Minimum of 8 characters required!")
        get_pass()
           
def get_pass():
    print("Password Validator:")
    pas=input("Enter Your Password: ")
    passwd(pas)

get_pass()    
