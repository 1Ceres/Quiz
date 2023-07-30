class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.point = 0

    def still_have_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):

        ans = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
        if ans == self.question_list[self.question_number].answer:
            print("You got it right!")
            self.point += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {self.question_list[self.question_number].answer}.")
        self.question_number += 1
        print(f"Your current score is: {self.point}/{self.question_number}.")
