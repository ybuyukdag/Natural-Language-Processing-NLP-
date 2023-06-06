##TOKENIZATION(Bölütleme)
import nltk
text = "Metin önişleme dil işleme modelleri için önemli bir adımdır."
print(nltk.word_tokenize(text))
'''
>>>['Metin', 'önişleme', 'dil', 'işleme', 'modelleri', 'için', 'önemli', 'bir', 'adımdır', '.']
'''

##TEXT CLEANING(Metin Temizleme)
import string
msg = 'Dil işlemede kullanılan kütüphaneler: nltk, spacy, scikit-learn vb.dir'
print(msg.translate(str.maketrans('','', string.punctuation))) #Noktalama temizleme
'''
>>>Dil işlemede kullanılan kütüphaneler nltk spacy scikitlearn vbdir
'''
stop_words = ["acaba", "ve", "bir", "birçok", "ama", "için"]
msg = "Acaba metindeki dolgu kelimelerini bulmak ve temizlemek için ne yapmalıyım?"
s1 = set(stop_words)
s2 = set(msg.lower().split())
print(s1.intersection(s2)) #önceden belirtilen Gereksiz sözcükleri temizleme
'''
>>>{'acaba', 've', 'için'}
'''

##TEXT NORMALIZATION(Metin Normalizasyonu)
msg = "Acaba metindeki dolgu kelimelerini bulmak ve temizlemek için ne yapmalıyım?"
print(msg.lower()) #Tekrarlardan kaçınmak için harfleri aynı boyuta getirmek, Küçük harf
'''
>>>acaba metindeki dolgu kelimelerini bulmak ve temizlemek için ne yapmalıyım?
'''

#Kuraldışı kelimelerin Düzeltilmesi(Conversion of non-canonical words)
#Yazım hataları(Spellcheck)

##STEMMING AND LEMMATIZATION(Gövdeleme ve Kök Bulma )
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
# choose some words to be stemmed
words = ["program", "programs", "programmer", "programming", "programmers"]
for w in words:
	print(w, " : ", ps.stem(w))
'''
>>>program  :  program
programs  :  program
programmer  :  programm
programming  :  program
programmers  :  programm
'''
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))
'''
>>>rocks : rock
corpora : corpus
better : good
'''
