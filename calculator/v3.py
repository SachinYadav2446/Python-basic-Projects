




def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

count=1

while count==1:
    print("Lets do some computation")
    print("Choose your expression among these options")
    print("1)Addition")
    print("2)Subtraction")
    print("3)Multiplication")
    print("4)Division")

    choice=input("Enter your choice among options : ")
    num1=float(input("Enter your first number : "))
    num2=float(input("Enter your second number : "))
    
    if choice=="1":
        ans=addition(num1,num2)
        print(f"Output :{ans} ")

    elif choice=="2":
        ans=subtraction(num1,num2)
        print(f"Output :{ans} ")

    elif choice=="3":
        ans=multiplication(num1,num2)
        print(f"Output :{ans} ")

    elif choice=="4":
        if num2!=0:
            ans=division(num1,num2)
            print(f"Output :{ans} ")
        else:
            print("Can not divide by zero")

    else :
        print("Choose right expression above")

    count=0
    change_count=int(input("Enter 0 if wanna exit or 1 to compute again : "))
    if change_count==1:
        count=1
    else:
        count=0
