import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

def process(p):
    switcher = {
        "CC": "Coordinating Conjunction",
        "CD": "Number",
        "DT": "Determiner",
        "EX": "Existential There",
        "IN": "Preposition",
        "JJ": "Adjective",
        "JJR": "Comparative Adjective",
        "JJS": "Superlative Adjective",
        "MD": "Modal Verb",
        "NN": "Noun",
        "NNS": "Noun",
        "NNP": "Proper Noun",
        "NNPS": "Proper Noun",
        "PDT": "Predeterminer",
        "POS": "Possessive",
        "PRP": "Personal Pronoun",
        "PRP$": "Possessive Pronoun",
        "RB": "Adverb",
        "RBR": "Adverb",
        "RBS": "Adverb",
        "TO": "Preposition",
        "UH": "Interjection",
        "VB": "Verb",
        "VBD": "Verb",
        "VBG": "Verb",
        "VBN": "Verb",
        "VBP":"Verb",
        "VBZ": "Verb",
        "WDT": "WH Determiner",
        "WP": "WH Pronoun",
        "WP$": "WH Possessive Pronoun",
        "WRB": "WH Adverb",
    }
    return switcher.get(p, p)

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

stop_words = set(stopwords.words('english')) 
print("Starting ...")
#Reading From Input
output = open("output.txt", "w")
input = open('input.txt', "r")
lines=input.readlines()
for line in lines:
    output.write("\n"+line)
    words=nltk.word_tokenize(line)
    tagged = nltk.pos_tag(words) 
    for tag in tagged:
        if(tag[0]!="." and tag[0]!="," and tag[0]!="!" and tag[0]!="?"  and tag[0]!=":" and tag[0]!="(" and tag[0]!=")" and tag[0]!="-"):
            if(tag[0]=="'re"):
                output.write("%s %s %s\n" % ("are",":",process(tag[1])))
            elif(tag[0]=="'s"):
                output.write("%s %s %s\n" % ("is",":",process(tag[1])))
            else:
                output.write("%s %s %s\n" % (tag[0],":",process(tag[1])))
output.close()
input.close()
print("Done!")