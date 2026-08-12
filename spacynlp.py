Install spaCy
!pip install spacy
!python -m spacy download en_core_web_sm
Basic spaCy NLP Program
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

text = "Apple is planning to open a new office in Hyderabad in 2026."

# Process the text
doc = nlp(text)

# Tokenization
print("TOKENS:")
for token in doc:
    print(token.text)

# Stopwords
print("\nSTOPWORDS:")
for token in doc:
    if token.is_stop:
        print(token.text)

# POS Tagging
print("\nPARTS OF SPEECH:")
for token in doc:
    print(token.text, "->", token.pos_)

# Named Entity Recognition
print("\nNAMED ENTITIES:")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)
spaCy Program for Lemmatization
import spacy

nlp = spacy.load("en_core_web_sm")

text = "The students are studying and playing games."

doc = nlp(text)

for token in doc:
    print(token.text, "->", token.lemma_)