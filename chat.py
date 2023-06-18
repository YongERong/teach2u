import streamlit as st
from streamlit_chat import message
import question_generator
import context_extraction
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx

st.set_page_config(
    page_title="Teach2U",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

if "session_id" not in st.session_state:
    st.session_state["session_id"] = get_script_run_ctx().session_id

if "questions" not in st.session_state:
    st.session_state["questions"] = []

if "answers" not in st.session_state:
    st.session_state["answers"] = []

if "context" not in st.session_state:
    st.session_state["context"] = None

if "file_uploader_key" not in st.session_state:
    st.session_state["file_uploader_key"] = 0


@st.cache_data(max_entries=5)
def get_questions(session_id):
    with open(st.session_state["context"].name, "wb") as f:
        f.write(st.session_state["context"].getbuffer())
    context = context_extraction.process_input(st.session_state["context"].name)
    q_chain = question_generator.question_chain()
    return question_generator.generate_qn(q_chain, context)

def reset():
    new_session_id = st.session_state["session_id"] + "e"
    new_uploader_key = st.session_state["file_uploader_key"] + 1
    st.session_state.clear()
    st.session_state["session_id"] = new_session_id
    st.session_state["file_uploader_key"] = new_uploader_key

def export_csv(questions, answers):
    if questions and answers:
        return "\n".join([f"{q}, {a}" for (q, a) in zip(questions, answers)])
    else:
        return ""

with st.sidebar:
    st.title("Teach2U")
    st.session_state["context"] = st.file_uploader(
        "Upload your teaching materials",
        type=["pdf", "txt"],
        key=st.session_state["file_uploader_key"],
    )
    if st.session_state["context"]:
        st.session_state["questions"] = get_questions(st.session_state["session_id"])
    st.write("---")
    st.button("Reset", on_click=reset)
    st.download_button(
        label="Export",
        data=export_csv(st.session_state["questions"], st.session_state["answers"][1:]),
        file_name="export.csv",
        help="Export conversation as csv file",
        mime="text/csv"
    )


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
        disabled=(not bool(st.session_state["context"])) or (len(st.session_state["answers"]) > len(st.session_state["questions"])),
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
            avatar_style="big-ears",
            key=str(i) + "user",
        )
        try:
            message(st.session_state["questions"][i], key=str(i) + "bot")
        except IndexError:
            message(
                "Thanks for chatting with me! I feel enlightened now. I hope this chat was insightful; click 'Export' on the side bar to download the chat, or 'Reset' to start a new one."
            )
