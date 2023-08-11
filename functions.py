def get_todos():
    with open('todo.txt',"r") as file:
            todos=file.readlines()
    return todos

def put_todos(todos):
    with open('todo.txt','w') as file:
            file.writelines(todos)
    