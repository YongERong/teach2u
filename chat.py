import streamlit as st
from streamlit_chat import message
import question_gen

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
    st.session_state["context"] = None


with st.sidebar:
    st.title("Teach2U")
    st.session_state["context"] = st.file_uploader(
        "Upload your teaching materials", type=["pdf", "txt"]
    )
    if st.session_state["context"]:
        with open(st.session_state["context"].name, "wb") as f:
            f.write(st.session_state["context"].getbuffer())
        st.session_state["questions"] = question_gen.generate_qn(
            st.session_state["context"].name
        )
    st.write("---")
    st.button("Reset", on_click=lambda: st.session_state.clear())


response_container = st.container()
input_container = st.container()


def submit():
    st.session_state["answers"].append(st.session_state["input"])
    st.session_state["input"] = ""


with input_container:
    input = st.text_input(
        label="Input your answers",
        value="",
        key="input",
        label_visibility="collapsed",
        on_change=submit,
    )

with response_container:
    message(
        "Hey there! I'm Teach2U, a teachable assistant. I will ask questions related to your content to help you review and reflect upon your learnings."
    )
    message("What subject would you like to teach me today?")
    for i in range(len(st.session_state["answers"])):
        message(
            st.session_state["answers"][i],
            is_user=True,
            key=str(i) + "_user",
            avatar_style="big-ears",
        )
        message(st.session_state["questions"][i], key=str(i))
