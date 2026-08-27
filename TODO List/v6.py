tasks=[]

def show_tasks():
    for index,task in enumerate(tasks,start=1):
        print(f"{index}:{task['name']}-{task['status']}")


while True: 

    print("TO-DO List Menu")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Update Task Status")
    print("4) Remove Tasks")
    print("5) Exit")
    

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
            show_tasks()           
        else:
            print("TO-DO List is Empty for Now")

    elif choice==3:
        if len(tasks)>0:
            
            show_tasks()
            choice_update_task=int(input("Enter which task to update : ")) 
            if 1<=choice_update_task<=len(tasks):
                new_status=input("Enter status : ")
                tasks[choice_update_task-1]['status']=new_status
            else:
                 print("Invalid task number")
        else:
             print("TO-DO List is empty.Add Tasks first")

    elif choice==4:
        if len(tasks)==0:
            print("TO-DO List is Empty . Add Tasks First")
        else:
            show_tasks()
            remove_input=int(input("Choose which one to delete : "))
            tasks.pop(remove_input-1)
            print("Updated TO-DO List is here: ")
            for index,task in enumerate(tasks,start=1):
                            print(f"{index}:{task['name']}-{task['status']}")

    elif choice==5:
        print("Exited program")
        break
        
    else:
        print("Choose again")