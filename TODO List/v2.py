tasks=[]

while True: 

    print("TO-DO List Menu")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Exit")

    choice=int(input("Enter your choice : "))

    if choice==1:
        add_task=input("Enter your TO DO here : ")
        tasks.append(add_task)

        
    elif choice==2:
        if len(tasks)>0:
            for index,task in enumerate(tasks,start=1):
                print(f"Index:{index},{task}")
                print("Choose operation again")
        else:
            print("TO-DO List is Empty for Now")

    elif choice==3:
        print("Exited program")
        break
        
    else:
        print("Choose again")