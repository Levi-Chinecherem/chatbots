'''
This Chatbot is built to only answer queries related
to what its trained with, nothing more nothing less
--------
There are no downloads or libraries required for this
'''

statements = [
  ('hi', 'solutionz: Hey!\n'),
  ('how are you', 'solutionz: I\'m fine thanks!\n'),
  ('whats your name', 'solutionz: my name is solutionz im a bot trained to chat!\n'),
  ('bye', 'solutionz: Bye!\n'),
  ('what do i need to know about you', 'solutionz: i\'m a bot trained to chat!\n'),
  ('what do you do', 'solutionz: i\'m a bot trained to chat!\n')
]

def getResponse(user_input):
  for state in statements:
    if user_input == state[0]: 
      return state[1]
  return "solutionz: I dont understand you"

#Execution and Testing
print("solutionz: Hi welcome to solutionz bot ask me anything about me")
while True:
  user_input = input().lower()
  if user_input != 'bye':
    res = getResponse(user_input)
    print(res)
  else:
    print("solutionz: Bye! Stay safe!")
    break

