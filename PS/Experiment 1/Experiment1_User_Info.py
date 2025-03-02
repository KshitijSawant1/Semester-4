def get_user_info():
    print ("=======================================")
    print ("Details Entry")
    print ("=======================================")
    print ()
    Name =  input ("Enter your Name     : ")
    Age  =  input ("Enter your Age      : ")
    email_entry = True 
    while email_entry :
        Email =  input ("Enter your Email    : ")
        if "@" not in Email or "." not in Email : 
            print ("Incorrect Email Format Occurred")
            print()
            email_entry = True
        else : 
            print ("Email Entered Succesfully")
            email_entry = False
    print ()
    print ("=======================================")
    print ("Details Dispaly")
    print ("=======================================")
    print ()
    print (f"Name of the User   :{Name}")
    print (f"Age of the User    :{Age}")
    print (f"Email of the User  :{Email}")
    print ()
    print ("=======================================")

print ()
print ()
get_user_info()