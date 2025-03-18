from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("输入 to-do")
input_box: sg.Input = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("添加")

window = sg.Window("My Todo App",
                   layout=[[label], [input_box, add_button]],
                   font=("helvetica", 18))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "添加":
            todo = values["todo"] + "\n"
            todos = functions.get_todos()
            todos.append(todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()

