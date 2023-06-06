import nltk


###Tokenization(Bölütleme)
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
text = """
    Susmayın! 
    Saat 16'da Kadiköy’de buluşalım. 
    Şiddet cahillik göstergesinin en üst sınırıdır.
    Ailede şiddet gelecegi karartır.
    Kadına şiddet, insanlığa ihanettir.
    Her sessiz kalınan şiddet bir gün sizi bulur.
    Sevgi insanlığın, siddet hayvanlığın kanunudur.
"""

sentences = sent_tokenize(text)
sentences = word_tokenize(text)

# for sentence in sentences:
#     print(sentence)


###Stemming(Gövdeleme)
#NLTK Porter(better for English)
from nltk.stem.porter import *
stemmer = PorterStemmer()

word = 'civilization'

#print(stemmer.stem(word))

#'civilization' -->> 'civil'

#Snowball Stemmer
#(For all Languages)
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
word = 'civilization'
#print(stemmer.stem(word))

from snowballstemmer import TurkishStemmer
turkishStem=TurkishStemmer()
# print(turkishStem.stemWord("ekmekler")) #ekmek
# print(turkishStem.stemWord("çiçeklik")) #çiçeklik
#snowball returns only lemmas for Turkish

###Lemmatization(Baş Sözcük Çıkarma)
#Spacy
import spacy
nlp = spacy.load('en_core_web_sm')
word = nlp ('civilization')

# for token in word:
#     print(token.lemma_) #civilization

##PostTagging
#NLTK
tokens = nltk.word_tokenize("Can you buy me a red chili pepper from a grocery?")

#print("Part of Speech:", nltk.pos_tag(tokens))
#Spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("I want an early upgrade")
# for token in doc:
#     print(token.text, token.pos_)

##NAME ENTITY RECOGNATION(NER)(VARLIK İSMİ TANIMA)
#nltk
from nltk import ne_chunk
sentence = "Legendary scientist Albert Eİnstein is born in Ulm, Germany."
tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged_tokens)
#print(entities)
#spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")
sentence = nlp("Micheal Jordan is a professor at Berkeley")
print([(X.text,X.label_) for X in sentence.ents])