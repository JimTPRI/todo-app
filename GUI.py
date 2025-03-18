from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("输入 to-do")
input_box: sg.Input = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("添加")

window = sg.Window("My Todo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

