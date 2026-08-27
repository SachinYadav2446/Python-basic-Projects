user_input=input("Enter your password : ")

if len(user_input)<6:
    print("Weak Password")

elif len(user_input)>=6 and len(user_input)<10:
    print("Medium Password")

else :
    print("Strong Password")