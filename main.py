from helper_function import *

VIEW_QUESTIONS = '1'
VIEW_ANSWERS = '2'
REGISTER = '3'
LOGIN = '4'
POST_QUESTIONS = '5'
POST_ANSWERS = '6'
EXIT = '7'


def main():
    author_id = None

    print("Welcome to AskMate App!")
    while True:
        display_options()
        choice = get_user_input("Enter your choice: ")

        if choice == VIEW_QUESTIONS:
            view_questions()
        elif choice == VIEW_ANSWERS:
            view_answers()
        elif choice == REGISTER:
            register()
        elif choice == LOGIN:
            author_id = log_in()
        elif choice == POST_QUESTIONS:
            post_quiestion(author_id)
        elif choice == POST_ANSWERS:
            post_answers(author_id)
        elif choice == EXIT:
            print_message("Have a good day!")
            break
        else:
            print_message("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
