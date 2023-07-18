from data import *
from question_model import *
from quiz_brain import *

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
    
