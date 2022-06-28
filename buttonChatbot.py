import json


f = "C:\\Developments\\port Projects\\chatbots\\file_data\\continentCode.json"
with open(f, encoding='utf-8-sig', errors='ignore') as json_data:
  data = json.load(json_data, strict=False)
  counter = 0  
  for code in data['continents']:
    print(counter+1, end=' ')
    print(code['Name'])
    counter += 1


def response(user_response):
  for name in data['continents']:
    if user_response == name['Name']: 
      return name['Code']
  return "continentBot: I dont understand you. Entered valid continent name"

#Execution and Testing
print("continentBot: Hi im trained to tell you the Continent code \nif you give me their name from the above list")
while True:
  user_input = input()
  if user_input != 'bye':
    res = response(user_input)
    print(res)
  else:
    print("continentBot: Bye! Stay safe!")
    break
