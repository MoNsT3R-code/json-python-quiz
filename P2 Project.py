import json
import random
import os

# Utility Functions
def load_data(file_name, default_data=None):
    """Load data from a JSON file, creating the file with default data if it doesn't exist."""
    if not os.path.exists(file_name):
        if default_data is not None:
            save_data(file_name, default_data)
        return default_data or {}
    with open(file_name, 'r') as file:
        return json.load(file)

def save_data(file_name, data):
    """Save data to a JSON file."""
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def initialize_questions():
    """Initialize default questions for all subjects and difficulties."""
    return {
        "maths": {
            "low": [
                {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4", "hint": "First even number."},
                {"question": "5 x 1 = ?", "options": ["1", "5", "10", "15"], "answer": "5", "hint": "Anything multiplied by 1 is itself."},
                {"question": "10 - 3 = ?", "options": ["6", "7", "8", "9"], "answer": "7", "hint": "Count backward."},
                {"question": "12 / 4 = ?", "options": ["2", "3", "4", "6"], "answer": "3", "hint": "Divide 12 into 4 equal parts."},
                {"question": "3 x 3 = ?", "options": ["6", "7", "8", "9"], "answer": "9", "hint": "Square of 3."}
            ]
        }
    }

# Student Class
class Student:
    def __init__(self, username, password, points=0):
        self.username = username
        self.password = password
        self.points = points

    def attempt_quiz(self, questions):
        """Allow the student to attempt a quiz with next/submit options."""
        score = 0
        total_questions = len(questions)
        question_index = 0

        while question_index < total_questions:
            q = questions[question_index]
            print(f"\nQuestion {question_index + 1}: {q['question']}")
            print("Options:")
            for i, option in enumerate(q['options'], start=1):
                print(f"{i}. {option}")
            answer = input("Enter the number of your choice: ").strip()

            try:
                if q['options'][int(answer) - 1] == q['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect! Hint: {q['hint']}")
            except (ValueError, IndexError):
                print("Invalid input. Moving to the next question.")
            
            if question_index < total_questions - 1:
                choice = input("Enter 'N' for Next Question or 'S' to Submit: ").strip().upper()
                if choice == 'S':
                    break
            question_index += 1

        print(f"\nQuiz Submitted! Your score: {score}/{total_questions}")
        return score

# Instructor Class
class Instructor:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Quiz System
class QuizSystem:
    def __init__(self):
        self.users = load_data("users.json", {})
        self.questions = load_data("questions.json", initialize_questions())
        self.performance = load_data("performance.json", {})

    def save_state(self):
        save_data("users.json", self.users)
        save_data("questions.json", self.questions)
        save_data("performance.json", self.performance)

    def register_user(self, role):
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()
        if username in self.users:
            print("Username already exists!")
        else:
            self.users[username] = {"password": password, "role": role, "points": 0}
            print("User registered successfully!")
            self.save_state()

    def login_user(self):
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        if username in self.users and self.users[username]["password"] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password.")
            return None

    def run(self):
        print("=== Welcome to the Quiz System! ===")
        while True:
            action = input("Choose an action: R (Register), L (Login), E (Exit): ").strip().upper()
            if action == "R":
                role = input("Register as S (Student) or I (Instructor): ").strip().upper()
                if role == "S":
                    self.register_user("student")
                elif role == "I":
                    self.register_user("instructor")
                else:
                    print("Invalid role.")
            elif action == "L":
                username = self.login_user()
                if username:
                    role = self.users[username]["role"]
                    if role == "student":
                        self.student_menu(username)
                    elif role == "instructor":
                        self.instructor_menu(username)
            elif action == "E":
                print("Goodbye!")
                break
            else:
                print("Invalid action.")

    def student_menu(self, username):
        student = Student(username, self.users[username]["password"], self.users[username]["points"])
        while True:
            print("\n--- Student Menu ---")
            choice = input("Choose an action: Q (Attempt Quiz), V (View Results), L (Logout): ").strip().upper()
            if choice == "Q":
                subject = input("Enter subject (maths): ").strip().lower()
                difficulty = "low"  # Default difficulty for now
                if subject in self.questions:
                    questions = random.sample(self.questions[subject][difficulty], min(5, len(self.questions[subject][difficulty])))
                    score = student.attempt_quiz(questions)
                    self.performance.setdefault(subject, {}).setdefault(difficulty, {}).setdefault(username, score)
                    self.save_state()
                else:
                    print("Invalid subject.")
            elif choice == "V":
                print(f"\n--- Results for {username} ---")
                for subject, levels in self.performance.items():
                    for level, scores in levels.items():
                        if username in scores:
                            print(f"Subject: {subject}, Difficulty: {level}, Score: {scores[username]}")
            elif choice == "L":
                break
            else:
                print("Invalid choice.")

    def instructor_menu(self, username):
        instructor = Instructor(username, self.users[username]["password"])
        while True:
            print("\n--- Instructor Menu ---")
            choice = input("Choose an action: V (View Performance), L (Logout): ").strip().upper()
            if choice == "V":
                subject = input("Enter subject to view performance: ").strip().lower()
                subject_data = self.performance.get(subject, {})
                if not subject_data:
                    print("No performance data available for this subject.")
                    continue
                for level, scores in subject_data.items():
                    print(f"Difficulty: {level}")
                    for student, score in scores.items():
                        print(f"{student}: {score}")
            elif choice == "L":
                break
            else:
                print("Invalid choice.")

# Run the Quiz System
quiz_system = QuizSystem()
quiz_system.run()
