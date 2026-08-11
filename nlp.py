### nlp program
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize
text = "I love python. I am learning nlp"
words = word_tokenize(text)
print(words)
sentences = sent_tokenize(text)
print(sentences)
### nlp tokenzer
from textblob import TextBlob
text = "I love learning python and nlp."
blob = TextBlob(text)
print(blob.words)
print(blob.sentences)
### subjectivity
from textblob import TextBlob
text = "I really love this course."
blob = TextBlob(text)
print(blob.sentiment)