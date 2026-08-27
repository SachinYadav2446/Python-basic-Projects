user_input=input("Enter your password : ")

has_uppercase=False
has_lowercase=False
has_digit=False

for char in user_input:
    if char.isupper()==True:
        has_uppercase=True
    if char.islower()==True:
        has_lowercase=True
    if char.isdigit()==True:
        has_digit=True

if has_lowercase==True and has_uppercase==True and has_digit==True:
    print("strong password")

elif has_lowercase==False and has_uppercase==True and has_digit==True or has_lowercase==True and has_uppercase==True and has_digit==False or has_lowercase==True and has_uppercase==False and has_digit==True:
    print("Medium Password")

elif has_lowercase==False and has_uppercase==False and has_digit==True or has_lowercase==False and has_uppercase==True and has_digit==False or has_lowercase==True and has_uppercase==False and has_digit==False:
    print("Weak Password")

else :
    print("Invalid Password")