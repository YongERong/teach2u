import streamlit as st
from streamlit_chat import message
import question_generator
import context_extraction
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx

session_id = get_script_run_ctx().session_id

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

@st.cache_data(max_entries=5)
def get_questions(session_id):
        with open(st.session_state["context"].name, "wb") as f:
            f.write(st.session_state["context"].getbuffer())
        context = context_extraction.process_input(st.session_state["context"].name)
        q_chain = question_generator.question_chain()
        return question_generator.generate_qn(q_chain, context)

with st.sidebar:
    st.title("Teach2U")
    st.session_state["context"] = st.file_uploader(
        "Upload your teaching materials", type=["pdf", "txt"]
    )
    if st.session_state["context"]:
        st.session_state["questions"] = get_questions(session_id)
    st.write("---")
    st.button("Reset", on_click=lambda: st.session_state.clear())


response_container = st.container()
input_container = st.container()


def submit():
    st.session_state["answers"].append(st.session_state["input"])
    st.session_state["input"] = ""


with input_container:
    if not st.session_state["context"]:
        st.info("Upload your teaching materials to begin.")
    input = st.text_input(
        label="Input your answers",
        value="",
        key="input",
        label_visibility="collapsed",
        on_change=submit,
        disabled=not bool(st.session_state["context"]),
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
