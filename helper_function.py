import bcrypt
from database import *


def get_user_input(prompt):
    return input(prompt)


def get_secure_user_input(prompt):
    mySalt = bcrypt.gensalt()
    pas = input(prompt).encode('utf-8')
    res = bcrypt.hashpw(pas, mySalt)
    return res


def print_message(message):
    print("\n" + message)


def display_options():
    print("\n1. View Questions\n2. View Answers\n3. Register\n4. Login\n5. Post Question\n6. Post Answer\n7. Exit")


def view_questions():
    questions = get_questions()
    for question in questions:
        print(
            f"\n Question[{question['id']}]: {question['title']} - {question['content']} (created at: {question['created_at']})")


def view_answers():
    question_id = int(get_user_input("Enter the question ID: "))
    answers = get_answers(question_id)
    for answer in answers:
        print(f"\nAnswer id :[{answer['id']}] - {answer['content']} (created at: {answer['created_at']})")


def register():
    username = get_user_input("Enter your username: ")
    password = get_secure_user_input("Enter your password: ")
    author_id = register_user(username, password)
    if author_id:
        print_message("Registration successful!")
    else:
        print_message("Registration failed. Please try again.")


def log_in():
    username = get_user_input("Enter your username: ")
    password = get_user_input("Enter your password: ")
    author_id = login(username, password)
    if author_id:
        print_message("Login successful!")
        return author_id
    else:
        print_message("Invalid username or password.")


def post_quiestion(author_id):
    if author_id:
        title = get_user_input("Enter the question title: ")
        content = get_user_input("Enter the question content: ")
        post_question(title, content, author_id)
        print_message("Question posted successfully!")
    else:
        print_message("You need to register or log in first.")


def post_answers(author_id):
    if author_id:
        question_id = int(get_user_input("Enter the question ID: "))
        content = get_user_input("Enter the answer content: ")
        answer_id = post_answer(content, question_id, author_id)
        print_message(f"Answer posted successfully! Answer ID: {answer_id}")
    else:
        print_message("You need to register or log in first.")
