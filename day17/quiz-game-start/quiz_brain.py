class QuizBrain():
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    
    def nex_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question} True/False ")