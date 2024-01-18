SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET default_tablespace = '';

SET default_with_oids = false;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS answers;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS answers (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    question_id INTEGER REFERENCES questions(id),
    author_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password) VALUES ('Robert', 'p@ssword');
INSERT INTO users (username, password) VALUES ('Anna', 'P@ssword1');
INSERT INTO users (username, password) VALUES ('Adam', 'pa55word@');
INSERT INTO users (username, password) VALUES ('Dmitry', 'Dmitry@Friend');

INSERT INTO questions (title, content, author_id) VALUES ('Python Code', 'How do you comment a single line in Python?', 2);
INSERT INTO questions (title, content, author_id) VALUES ('Python problem', 'What is Python?', 1);
INSERT INTO questions (title, content, author_id) VALUES ('Python problem', 'Explain the purpose of a virtual environment?', 3);
INSERT INTO questions (title, content, author_id) VALUES ('Python typing', 'What is duck typing in Python?', 4);
INSERT INTO questions (title, content, author_id) VALUES ('Python OOP', 'What does the __str__ method do in a Python class?', 4);

INSERT INTO answers (content, question_id, author_id) VALUES ('Python is a high-level, interpreted programming language known for its readability and versatility.', 1, 1);
INSERT INTO answers (content, question_id, author_id) VALUES ('A virtual environment isolates Python projects, managing dependencies and avoiding conflicts between different projects.', 3, 3);
INSERT INTO answers (content, question_id, author_id) VALUES ('Duck typing is a concept where the type of an object is determined by its behavior, focusing on methods and properties rather than explicit types.', 4, 4);
INSERT INTO answers (content, question_id, author_id) VALUES ('It returns a human-readable string representation when str() or print() is called.', 5, 4);
