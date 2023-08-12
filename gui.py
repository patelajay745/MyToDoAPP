import functions
import PySimpleGUI as sg



label=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="Enter todo",key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),key="list_todos",
                    enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")

window=sg.Window('My ToDo App',
                 layout=[[label],[input_box,add_button],[list_box,edit_button]],
                 font=("Lucida",22))

while True:
    event,values=window.read()
    match event:
        case "Add":
            todos=functions.get_todos()
            todos.append(values['todo']+"\n")
            functions.put_todos(todos)
            window['list_todos'].update(values=todos)
        case "Edit":
            print(values["list_todos"])
            todo_to_edit=values["list_todos"][0]
            new_todo=values['todo']
            todos=functions.get_todos()
            #search the todo using index and replace the new todo as the selected index
            print(todos)
            index=todos.index(todo_to_edit)
            todos[index]=new_todo+"\n"
            functions.put_todos(todos)

            window['list_todos'].update(values=todos)

        case "list_todos":
            window["todo"].update(value=values["list_todos"][0])

        case sg.WIN_CLOSED:
            break


window.close()



