# from CLI import new_todo
from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("输入 to-do")
input_box: sg.Input = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("添加")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("编辑")

layout = [[label], [input_box, add_button], [list_box, edit_button]]

window = sg.Window("My Todo App",
                   layout=layout,
                   font=("helvetica", 18))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "添加":
            if values["todo"] == "" or values["todo"] == "\n":
                print("Invalid")
            else:
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()
                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
        case "编辑":
            try:
                if values["todo"] == "" or values["todo"] == "\n":
                    print("Invalid")
                else:
                    todo_to_edit = values["todos"][0]
                    new_todo = values["todo"] + "\n"
                    todos = functions.get_todos()
                    #print(todos)
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    #todos = functions.get_todos()
                    #print(todos)
                    window["todos"].update(values=todos)
            except IndexError:
                print("No selection")
                continue
            except ValueError:
                print("Invalid input")
                continue
        case "todos":
            try:
                #window["todo"].update(value=values["todos"][0])
                True
            except IndexError:
                print("Void")
                continue
        case sg.WIN_CLOSED:
            break

window.close()
