def password():
    import re
    mistakes = 0
    Password = input("Enter your password: ")
    passlen = len(Password)
    for i in range(passlen):
        if passlen < 15:
            mistakes +=1
        elif not re.search("[A-Z]", Password):
            mistakes +=1
        elif not re.search("[a-z]", Password):
            mistakes +=1
        elif not re.search("[0-9]", Password):
            mistakes +=1
        elif not re.search("[!@:#;$'\-=%^>&*(/)<_+]", Password ):
            mistakes +=1
    if mistakes > 1:
        print("Your password is INVALID")
    elif mistakes == 0:
        print("Your password is VALID")
        
    


password()
