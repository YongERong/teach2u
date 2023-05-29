from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import textract


def generate_qn(context_path):
    # Convert different file types to text
    context = textract.process(context_path).decode("utf-8")

    # Generate questions
    question_model_id = "valhalla/t5-base-e2e-qg"
    tokenizer = AutoTokenizer.from_pretrained(question_model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(question_model_id)

    q_pipe = pipeline(
        "text2text-generation", model=model, tokenizer=tokenizer, max_length=100
    )
    question_model = HuggingFacePipeline(pipeline=q_pipe)
    q_template = "generate questions: {text} </s>"
    q_prompt = PromptTemplate(input_variables=["text"], template=q_template)
    q_chain = LLMChain(llm=question_model, prompt=q_prompt)
    questions = q_chain.run(context).split("<sep>")

    return questions
