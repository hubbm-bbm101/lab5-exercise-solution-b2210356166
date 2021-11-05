address=input("write e-mail")
if "@" in address:
        if '.' in address:
            print("it is a valid e-mail")
        else:
            print("it is not a valid e-mail")
else:
        print("it is not a valid e-mail")
