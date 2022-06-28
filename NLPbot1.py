import nltk
import random
import string
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings("ignore")


path = "computer_science.txt"
f = open(path, 'r', errors = 'ignore')
raw = f.read()
raw = raw.lower()

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

sentToken = sent_tokens[:4]
wordToken = word_tokens[:4]

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

#Vectorizing
def response(user_response):
  chatbot_response = ""
  sent_tokens.append(user_response)
  TfidfVec = TfidfVectorizer(tokenizer = lemNormalize, stop_words = "english")
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if req_tfidf == 0:
    chatbot_response = chatbot_response + " I am sorry I don\'t understand you\n"
    return chatbot_response
  else:
    chatbot_response = chatbot_response + sent_tokens[idx]
    return chatbot_response

#Execution and testing

if __name__ == '__main__':
  flag = True
  print("Hello there\nMy name is young\nI will answer your queries in relation to my field of training\nIf you want to exit: type Bye!\n")
  while flag:
    user_response = input()
    user_response = user_response.lower()
    if user_response != "bye":
      if user_response == "thanks" or user_response == "thank you" or user_response == "thank you very much":
        flag = False
        print("Young: You are welcome!\n")
      else:
        if greetings(user_response) != None:
          print("Young:" + greetings(user_response))
          print("\n ")
        else:
          print("Young: ", end = '')
          print(response(user_response))
          print(" \n")
          sent_tokens.remove(user_response)
    else:
      flag = False
      print("Young: Bye! Have a great time!\n")
        

