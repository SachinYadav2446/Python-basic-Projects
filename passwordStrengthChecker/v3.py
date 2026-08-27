user_input=input("Enter your password : ")

has_uppercase=False
has_lowercase=False
has_digit=False
has_character=False
count=0
special_characters="!@#$%^&*()"

for char in user_input:
    if char in special_characters:
        has_character=True
    if char.isupper():
        has_uppercase=True
    if char.islower():
        has_lowercase=True
    if char.isdigit():
        has_digit=True

if has_character:
    count+=1

if has_uppercase:
    count+=1

if has_lowercase:
    count+=1

if has_digit:
    count+=1

if count==4:
    print("Strong Password")

elif 1<count<4:
    print("Medium Password")

else:
    print("Weak Password")
