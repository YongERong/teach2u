import re
from unstructured.partition.auto import partition
from unstructured.partition.text_type import sentence_count
import unstructured.documents.elements

def process_input(path):
    elements = partition(path)
    remove_citations = lambda text: re.sub("\[\d{1,3}\]", "", text)
    for e in elements:
        e.apply(remove_citations)
    narrative_elements = [e.text for e in elements if (type(e) is unstructured.documents.elements.NarrativeText) and sentence_count(e.text, min_length=5) > 2]

    return narrative_elements