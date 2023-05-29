import streamlit as st
from streamlit_chat import message
from question_generator import generate_qn

st.set_page_config(
    page_title="Teach2U",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

if "questions" not in st.session_state:
    st.session_state["questions"] = []

if "answers" not in st.session_state:
    st.session_state["answers"] = []

if "context" not in st.session_state:
    st.session_state["context"] = ""


def question_generator():
    st.write(st.session_state["context"])


with st.sidebar:
    st.title("Teach2U")
    st.session_state["context"] = st.file_uploader("Upload your teaching materials", type=["pdf", "txt"], on_change=question_generator)
    st.write("---")
    st.button("Export")
    st.button("Reset")


response_container = st.container()
input_container = st.container()


def submit():
    st.session_state["answers"].append(st.session_state["input"])
    st.session_state["input"] = ""

    # Temporary Response
    st.session_state["questions"].append(
        "What is the difference between a list and a tuple?"
    )


with input_container:
    input = st.text_input(
        label="Input your answers",
        value="",
        key="input",
        label_visibility="collapsed",
        on_change=submit,
    )

with response_container:
    message("Hey there! I'm Teach2U, a teachable assistant. I will ask questions related to your content to help you review and reflect upon your learnings.")
    message("What subject would you like to teach me today?")
    for i in range(len(st.session_state["questions"])):
        message(
            st.session_state["answers"][i],
            is_user=True,
            key=str(i) + "_user",
            avatar_style="big-ears",
        )
        message(st.session_state["questions"][i], key=str(i))
