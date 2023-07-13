import spacy 
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["Time flies like an arrow.", #creates list for garden path sentences
                       "The man who hunts ducks out on weekends.",
                       "The sour drink from the ocean."]

additional_sentences = ["Mary gave the child a Band-Aid.",
                        "That Jill is never here hurts.",
                        "The cotton clothing is made of grows in Mississippi."]

gardenpathSentences.extend(additional_sentences) #combines lists togther 

for sentence in gardenpathSentences: #iterates through each list and prints sentence, its tokens and named entities 
    doc = nlp(sentence)
    tokens = [token.text for token in doc]
    entities = [(entity.text, entity.label_) for entity in doc.ents] # https://notebook.community/rishuatgithub/MLPy/nlp/UPDATED_NLP_COURSE/02-Parts-of-Speech-Tagging/02-NER-Named-Entity-Recognition 
    print("Sentence:", sentence)
    print("Tokens:", tokens)
    print("Entities:", entities)
    for entity, label in entities:
        explanation = spacy.explain(label)
        print("Entity:", entity)
        print("Explanation:", explanation)
        print()
    
print(spacy.explain("GPE"))
print(spacy.explain("PERSON"))


# https://spacy.io/usage/spacy-101
#GPE is a category for states, countries and cities. This makes sense because Mississipi is a governed state in USA
#PERSON is a category for people including, fictional. This makes sense as the names in the list  