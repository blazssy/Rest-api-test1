todo_list=[]
print("Welcome to the To-Do List Application!")
print(" choose an option fromthe following:")
print ("1.add a task 2.view a task 3.delete a task 4. exit")
def add_task():
    task=input("enter the task you want to add:")
    todo_list.append(task)
    print("task added successfully!")
def view_tasks():
    if not todo_list:
        print("List is empty")
    else:
        print("Your tasks are:")
        for i,task in enumerate(todo_list, start=1):
            print(f'{i}.{task}')
def delete_task():
    view_tasks()
    try:
        index=int(input("Enter the task number you want to delete: ")) - 1
        removed_task= todo_list.pop(index)
        print(f'Task "{removed_task}" deleted successfully!')
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")

while True:
    choice =input("Enter your choice (1-4): ")
    print ("1.add a task 2.view a task 3.delete a task 4. exit")
    if choice =='1':
        add_task()
    elif choice=='2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice =='4':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")    
          
