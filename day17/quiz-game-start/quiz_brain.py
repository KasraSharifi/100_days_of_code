from data import question_data

class QuizBrain():
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    
    def do_we_still_have_questions(self):
        """The purpose here is to make sure that we are not going above the number of questions
        that we have"""
        if self.question_number >= len(self.question_list):
                print("==" * 30)
                print("You have completed the quiz!!")
                print(f"Your final score is {self.score} / {self.question_number}")
                print("==" * 30)
                return False
        else:
            return True
        
    def check_answer(self, answer):
        """The purpose of this method is to check to see whether the answer to the questions is 
        right or not"""
        if answer.lower() == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print("you are right")
        else:
            print("The answer is wrong")
            
        print(f"Your score is {self.score} / {self.question_number + 1}")
        print(f"the right answer to the question {self.question_list[self.question_number].text} is {self.question_list[self.question_number].answer.lower()} and your answer was {answer.lower()}")
        
    
    def nex_question(self):
        """This method is the method that enables us to play the quiz game and calls other methods
        define under QuizBrain class.
        We use check_answer() and do_we_still_have_questions() methods here."""
        ask_question = True
        while ask_question:
            current_question = self.question_list[self.question_number].text
            current_answer = self.question_list[self.question_number].answer
            
            answer = input(f"Q.{self.question_number + 1}: {current_question} True/False ")
            
            ask_question = self.check_answer(answer)
            
            #Checking to make sure that we are not going above the number of questions that we have
            self.question_number += 1
            print("\n")
            ask_question = self.do_we_still_have_questions()