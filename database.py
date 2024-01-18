import psycopg2
from psycopg2 import extras
import os

def connect_to_db():
    db_params = {
        'dbname': f'{os.environ["dbname"]}',
        'user': f'{os.environ["user"]}',
        'password': f'{os.environ["password"]}',
        'host': f'{os.environ["lhost"]}',
        'port': f'{os.environ["lport"]}'
    }

    try:
        connection = psycopg2.connect(**db_params)
    except psycopg2.DatabaseError as exception:
        print(f"Db connection error")
        raise exception

    connection.autocommit = True
    return connection


def execute_query(query_string, query_parameters=None):
    with connect_to_db() as connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query_string, query_parameters)
            result = cursor.fetchall()
    return result


def get_user_id(username):
    query = "SELECT id FROM users WHERE username = %s"
    result = execute_query(query, (username,))
    return result[0]['id'] if result else None


def register_user(username, password):
    query = "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id"
    result = execute_query(query, (username, password))
    return result[0]['id'] if result else None


def login(username, password):
    query = "SELECT id FROM users WHERE username = %s AND password = %s"
    result = execute_query(query, (username, password))
    return result[0]['id'] if result else None


def post_question(title, content, author_id):
    query = "INSERT INTO questions (title, content, author_id) VALUES (%s, %s, %s) RETURNING id"
    result = execute_query(query, (title, content, author_id))
    return result[0]['id'] if result else None


def post_answer(content, question_id, author_id):
    query = "INSERT INTO answers (content, question_id, author_id) VALUES (%s, %s, %s) RETURNING id"
    result = execute_query(query, (content, question_id, author_id))
    return result[0]['id'] if result else None


def get_questions():
    query = "SELECT * FROM questions ORDER BY created_at DESC"
    return execute_query(query)


def get_answers(question_id):
    query = "SELECT * FROM answers WHERE question_id = %s"
    return execute_query(query, (question_id,))
