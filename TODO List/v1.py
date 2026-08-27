tasks=[]

while True: 

    
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Exit")

    choice=int(input("Enter your choice : "))

    if choice==1:
        add_task=input("Enter your TO DO here : ")
        tasks.append(add_task)

        
    elif choice==2:
        print(f"Your To DO List : {tasks}")
        print("Choose operation again")

    elif choice==3:
        print("Exited program")
        break
        
    else:
        print("Choose again")