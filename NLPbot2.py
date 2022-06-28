import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import string
import warnings
import numpy as np
warnings.filterwarnings("ignore")

#https://www.medicalnewstoday.com/articles/159283#summary
f = open("HBP.txt", "r", errors="ignore")
raw = f.read()
raw = raw.lower()

#get word and sentence list
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

#processing (lemmatization)
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct),None)for punct in string.punctuation)
def lemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#Greetings
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what\'s up", "hey")
GREETING_RESPONSES = ["hello", "hi", "greetings", "hi there", "i am glad you are talking to me", "nods", "hey"]

def greetings(sentence):
  for word in sentence.split():
    if word.lower() in GREETING_INPUTS:
      return random.choice(GREETING_RESPONSES)

#Generating Resposes
def response(user_response):
  bot_response = ""
  sent_tokens.append(user_response)
  TfidfVec = TfidfVectorizer(tokenizer = lemNormalize, stop_words = "english")
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if req_tfidf == 0:
    bot_response = bot_response + " I am sorry I don\'t understand you\n"
    return bot_response
  else:
    bot_response = bot_response + sent_tokens[idx]
    return bot_response

#Execution and testing
flag = True
print("Mimi: My name is mimi\nI will answer your queries related to hypertension\nIf you want to exit: type Bye!\n")
while flag == True:
  user_response = input().lower()
  if user_response != "bye":
    if user_response == "thanks" or user_response == "thank you" or user_response == "thank you very much":
      flag = False
      print("Mimi: You are welcome!\n")
    else:
      if greetings(user_response) != None:
        print("Mimi:" + greetings(user_response))
        print("\n")
      else:
        print("Mimi: ", end = '')
        print(response(user_response))
        sent_tokens.remove(user_response)
        print("\n")
  else:
    flag = False
    print("Mimi: Bye! take care and stay safe!\n")
      