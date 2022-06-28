"""
This chat bot is rule based and its trained
using the nltk library
"""
from nltk.chat.util import Chat, reflections

pairs = [
  ['hi', ['Talent: hey how are you doing?']],
  ['how are you', ['Talent: i am fine thank you']],
  ['I need help', ['Talent: ask your friends']],
  ['Sleeping', ['Talent: It\'s the best thing to do']],
  ['Solar taxis', ['Talent: It is a wonderful thing']]
]

print("Talent: Im Talent how may i be of help?")
bot = Chat(pairs, reflections)
bot.converse()
