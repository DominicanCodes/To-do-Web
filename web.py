import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ''

st.title("My To-Do App")
st.subheader("What's next?")
st.write("Directions: Enter a to-do in the textbox and press enter.")

for index, todo in enumerate(todos):
    unique_key = "todo " + str(index)
    checkbox = st.checkbox(todo, key=unique_key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[unique_key]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new to-do...",
                on_change=add_todo, key="new_todo")

# st.session_state
# For server requirements: pip freeze > requirements.txt