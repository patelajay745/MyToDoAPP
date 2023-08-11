from functions import get_todos,put_todos
import time

todos=[]

now=time.strftime("%b %d, %Y %H:%M:%S") 

print("Today is ",now)

while True:
    user_action=input("type add, show, edit, delete or exit: ").strip()
    
    if user_action.startswith('add'):
        
        todo = user_action[4:]
        todos.append(todo+"\n")

        put_todos(todos)

    elif user_action.startswith('show'):
        
        todos=get_todos()
        
        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip()}")

    elif user_action.startswith('edit'):
        try:
            number=int(user_action[5:]) - 1

            todos=get_todos()

            todos[number]=input("Enter new todo: ") +"\n"

            put_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue



    elif user_action.startswith('delete'):
        try:
            todos=get_todos()

            todos.pop(int(user_action[7:])-1) 

            put_todos(todos)

        except IndexError:
            print("There is no item with that number")  
            continue 

    elif user_action.startswith('exit'):
        break


        