tasks=[]

while True: 

    print("TO-DO List Menu")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Remove Tasks")
    print("4) Exit")
    

    choice=int(input("Enter your choice : "))

    if choice==1:
        add_task_name=input("Task Name : ")
        add_task_status=input("Status : ")
        sub_task={
             "name":add_task_name,
             "status":add_task_status
        }
        
        tasks.append(sub_task)

 
    elif choice==2:
        if len(tasks)>0:
            for index,task in enumerate(tasks,start=1):
                print(f"{index}:{task['name']}-{task['status']}")
                
        else:
            print("TO-DO List is Empty for Now")

    elif choice==3:
        if len(tasks)==0:
            print("TO-DO List is Empty . Add Tasks First")
        else:
            for index,task in enumerate(tasks,start=1):
                print(f"{index}:{task['name']}-{task['status']}")
            remove_input=int(input("Choose which one to delete : "))
            tasks.pop(remove_input-1)
            print("Updated TO-DO List is here: ")
            for index,task in enumerate(tasks,start=1):
                            print(f"{index}:{task['name']}-{task['status']}")

    elif choice==4:
        print("Exited program")
        break
        
    else:
        print("Choose again")