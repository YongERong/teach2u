# **🎓Teach2U**
_Learning Through Teaching_

## **Goal**
To provide a platform for students to identify misconceptions and gaps in their knowledge through teaching teachable agents. To then turn these interactions into condensed, reflective and easy to review materials.

## **Installation**
Install the necessary dependencies into a virtual environment using pip.

`pip install venv`

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`streamlit run chat.py`

## **Limitations**
As Streamlit reloads the page each time a component is updated, it can get quite laggy.
## **Future**
- [ ] More models, more efficient
- [ ] Better user response validation
- [ ] Export conversations as flashcards and mindmaps
## **Credit & Citations**
We stand upon the shoulders of giants. This project would not be possible without the following open-source libaries and resources.

[LangChain](https://github.com/hwchase17/langchain) by Harrison Chase and contributers.
> Chase, H. (2022). LangChain [Computer software]. https://github.com/hwchase17/langchain

[Streamlit](https://github.com/streamlit/streamlit) by Adrien Treuille, Amanda Kelly, Thiago Teixeira and its contributers.
> Treuille, A., Kelly, A., & Teixeira T. (2018). Streamlit [Computer software].

[t5-base-e2e-qg](https://huggingface.co/valhalla/t5-base-e2e-qg) which contains contributions by Suraj Patil, Patrick von Platen and Julien Chaumond.

[textract](https://github.com/deanmalmgren/textract) by Dean Malmgren and contributers.
> Dean, M. (2014). textract [Computer software]. https://github.com/deanmalmgren/textract 