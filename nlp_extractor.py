import spacy

nlp = spacy.load("en_core_web_sm")

def nlp_extraction(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text) 
    return entities
