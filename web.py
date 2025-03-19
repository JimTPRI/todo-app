import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("这是一个待办事项应用")
st.write("提高自己的生产力吧")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="添加待办事项", on_change=add_todo,
              key="new_todo")
