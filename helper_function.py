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



