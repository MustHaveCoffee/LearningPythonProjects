
import random
import time

responses = ['Not Today' , 'Negative' , 'Why did you even ask ?' , 'No' , 'Outlook is positive' , 'Looks like a yes' , 'Absolutly Not' , 'You can do it']

def answerquery():
    question = input("Ask and you shall recive. \n")
    print('Let me guess an answer you want to see')
    time.sleep(2)
    print("Give me a minute trying to waste your time")
    time.sleep(2)
    print(random.choice(responses))
    print("\n")

answerquery()

secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
while secondQuestion == str("Y"):
    answerQuery()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
else:
    print(input("Press any key to exit"))
