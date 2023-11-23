import streamlit as st 
import functions as fct

st.title('My To-Do APP')
st.subheader('This is my Todo list')

Todos = fct.read_todos('Todos.txt')

for Todo in Todos:
    checked = st.checkbox(Todo, key=Todo)
    if checked:
        Todos.remove(Todo)
        fct.write_todos('Todos.txt', Todos)
        del st.session_state[Todo]
        st.experimental_rerun()
    
def add_todo():
    Todo = st.session_state["new_todo"] + '\n'
    Todos.append(Todo )
    fct.write_todos('Todos.txt',Todos)


    
st.text_input(label="",placeholder="Enter a new Todo...",
              on_change=add_todo,key='new_todo')