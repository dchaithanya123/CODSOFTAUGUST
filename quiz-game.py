class QuizQuestion:
    def _init_(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

class QuizGame:
    def _init_(self, questions):
        self.questions = questions
        self.score = 0
    
    def display_question(self, question_obj):
        print(question_obj.question)
        for i, choice in enumerate(question_obj.choices, start=1):
            print(f"{i}. {choice}")
    
    def play(self):
        print("Welcome to the Quiz Game!")
        print("Rules: Select the correct answer for each question.")
        print("-------------------------")
        
        for question_obj in self.questions:
            self.display_question(question_obj)
            user_answer = input("Your answer: ")
            
            if user_answer.isdigit():
                user_answer = int(user_answer) - 1
                if 0 <= user_answer < len(question_obj.choices):
                    if question_obj.choices[user_answer] == question_obj.correct_answer:
                        print("Correct!")
                        self.score += 1
                    else:
                        print("Incorrect!")
                        print(f"The correct answer is: {question_obj.correct_answer}")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid input.")
            print("-------------------------")
        
        print("Quiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

# Define quiz questions
questions = [
    QuizQuestion("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),
    QuizQuestion("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "Mars"),
    QuizQuestion("What is the largest mammal?", ["Elephant", "Giraffe", "Blue Whale", "Lion"], "Blue Whale")
]

# Create and play the quiz game
quiz_game = QuizGame(questions)
quiz_game.play()