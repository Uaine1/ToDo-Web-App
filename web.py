import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    ntodo = st.session_state["new_todo"] + "\n"
    todos.append(ntodo)
    functions.write_todos(todos)


st.title("Welcome!")
st.subheader("This is a ToDO app")
st.write("Add your list of task here")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter task here.....",
              on_change=add_todo, key='new_todo')
