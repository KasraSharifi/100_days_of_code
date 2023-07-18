from data import question_data

class QuizBrain():
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    
    def do_we_still_have_questions(self):
        """The purpose here is to make sure that we are not going above the number of questions
        that we have"""
        if self.question_number == len(self.question_list):
                print("We have no more questions to ask")
                return False
        else:
            return True
        
    
    
    def nex_question(self):
        ask_question = True
        while ask_question == True:
            current_question = self.question_list[self.question_number].text
            current_answer = self.question_list[self.question_number].answer
            self.question_number += 1
            answer = input(f"Q.{self.question_number}: {current_question} True/False ")
            
            #Checking to make sure that we are not going above the number of questions that we have
            ask_question = self.do_we_still_have_questions()