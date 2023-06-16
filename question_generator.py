from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline



def generate_qn(context_list):
    questions = []

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
    for context in context_list:
        questions.append(q_chain.run(context).split("<sep>"))

    questions_flattened = [q for q_list in questions for q in q_list if q]
    # remove duplicates next
    return questions_flattened


#print(generate_qn(['As vitamin K2 is found in lower concentrations than other interfering lipid-soluble vitamins, (Langenberg & Tjaden, 1984) a variable wavelength detector does not have sufficient sensitivity and selectivity for its quantification. Instead, a fluorescent detector is used, which excites the analyte molecules and detects the light emitted by the analyte at a longer wavelength. However, vitamin K2 does not natively exhibit fluorescence. Hence, it needs to be reduced to its fluorophore-containing hydroquinone form before entering the detector (Langenberg & Tjaden, 1984). This is achieved using a post-column containing zinc powder (Haroon et al., 1987), as shown in the diagram below.', 'Moving on to the events of the fortnight, I encountered multiple challenging iodide samples which were consistently out of specification. On one occasion, my colleague and I repeated the analysis on the composite, top, middle, bottom and retention samples to no avail. Trial and error with diethylenetriamine pentaacetate (DTPA) and nitric acid appeared fruitless.', 'How did I react to a bad / disappointment day? How had I overcome it? During one day I found disheartening, my colleague and I had completed all of the outstanding analyses by the late afternoon and had started on housekeeping duties. It was one of the few times we did not encounter any problematic iodide samples and I found it satisfying to have no backlog. Much to our dismay, new samples were logged in shortly afterwards. Resuming analysis, we came across several challenging iodide samples and ended up finishing late. As a result, the other interns had to help me with my housekeeping duties.', 'I found this disappointing as what once felt like a smooth-sailing day quickly took a turn for the worse. Furthermore, I felt guilty for having burdened the other interns. Looking back, I believe it was not a sound decision to continue analysis. Instead, I should have concluded analysis after facing difficulty and pushed the remaining samples to the next day, as they still had a relatively long deadline.', 'What would I do differently if I were to approach the same problem again? In future, I will plan my time better and learn when to ‘say no’ and move the outstanding samples to the next day. This lesson is also applicable to tasks within my school and personal life.', 'Were my expectations for the internship realistic? Why or why not? Firstly, my expectations for my performance in the internship was not realistic. Initially, I had lofty expectations for the speed and accuracy of my techniques. In contrast, I made several mistakes throughout my internship and my efficiency left much to be desired. For example, the analysis of beta-carotene (as discussed in Week 5 and 6) took longer than expected in the beginning. This performance felt unsatisfactory, which gave me quite a lot of pressure to improve. After much reflection, I decided to tamper my expectations and commit to gradual improvement.', 'Next, the takeaways from the internship exceeded my expectations. Originally, I found the work at DSM to be somewhat menial and manual. As such, it would be possible to glide by without much understanding of the internal processes. Despite that, upon closer inspection, I realised that much of the experiences I gained at DSM could augment and build upon the concepts I learned in the classroom. Additionally, this internship also offers opportunities for introspection and growth on an interpersonal level.', 'What were the things that my industry supervisor/ colleagues did to help me to learn or overcome challenges? Firstly, my industry supervisors, trainers and colleagues were extremely patient and supportive. When I struggled to adapt to the fast-paced environment at the beginning of my internship, my trainers provided me with multiple opportunities to practice and hone my skills.', 'Lastly, my trainers and supervisors were approachable and forgiving. They held me accountable for my mistakes but did not dwell upon them. This made it easier for me to seek help when I encountered challenges.']))