# from CLI import new_todo
from modules import functions
import FreeSimpleGUI as sg
import time

sg.theme("LightBrown3")

clock = sg.Text("", key="clock")
label = sg.Text("输入 to-do")
input_box: sg.Input = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("添加", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("编辑")
complete_button = sg.Button("完成")
exit_button = sg.Button("退出")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window("My Todo App",
                   layout=layout,
                   font=("helvetica", 18))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "添加":
            if values["todo"] == "" or values["todo"] == "\n":
                sg.popup("Invalid", font=("helvetica", 16))
            else:
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()
                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
        case "编辑":
            try:
                if values["todo"] == "" or values["todo"] == "\n":
                    sg.popup("Invalid", font=("helvetica", 16))
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
                    window["todo"].update(value="")
            except IndexError:
                sg.popup("No selection", font=("helvetica", 16))
                continue
            except ValueError:
                sg.popup("Invalid input", font=("helvetica", 16))
                continue
        case "完成":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("No selection", font=("helvetica", 16))
                continue
        case "退出":
            break
        case "todos":
            try:
                #window["todo"].update(value=values["todos"][0])
                True
            except IndexError:
                sg.popup("Void", font=("helvetica", 16))
                continue
        case sg.WIN_CLOSED:
            break

window.close()
