import streamlit as st
from datetime import datetime
from todo import TodoApp

my_list = TodoApp()
todo_items = my_list.todo
print(type(todo_items))


def add_todo():
    todo = st.session_state["new_todo"]
    my_list.todo = todo
    my_list.write_to_file()


def delete_todo():
    my_list.delete_todo(index)
    my_list.write_to_file()


st.title("A Todo App")
st.subheader("This is a simple application to help you plan your day")
day = datetime.now().day
day_str = datetime.now().strftime('%A')
month = datetime.now().month
year = datetime.now().year
st.write("Today is {0} ({1}/{2}/{3}).".format(day_str, day, month, year))

if isinstance(todo_items, dict):
    for index, item in todo_items.items():
        st.checkbox(item, on_change=delete_todo, key=index)
    st.info("Tick to complete a todo item")
else:
    st.success("Your list is empty")

st.text_input(label="", placeholder="Add an item to your list..", on_change=add_todo, key="new_todo")



# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
#
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

