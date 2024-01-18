# AskMate

You are tasked with creating an application where people can ask questions and post answers to questions.
Like this [tiny site](https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used/),
but as a console application.

## Implemented Features

- ✅ Users can see a list of questions.
- ✅ Users can see which questions have answers.
- ✅ Users can navigate to see one question and all the answers it might have.
- ✅ Users can register, log in and log out. 
- ✅ Only logged in users can post questions or answers. Author is shown next to questions and answers.

### Optional
- ✅ The list of questions can be ordered by date or author or title.
- ✅ The list of questions can be filtered for date or author or title.

## Setup and Usage

### Prerequisites:
1. Python Installed
2. PostgreSQL installed

### Database Setup
1. Create a PostgreSQL database.
2. Execute the DB setup script to create tables and insert sample data.

### Virual Environment

1. Create a virtual environment 
```shell
    python -m <name> venv
```
2. Activate:
- On windows:
```shell
    .\venv\Scripts\activate 
```
 - On Unix or MacOS:
```shell
    source venv/bin/activate 
```
### Install dependencies 
```shell
    pip install -r requirements.txt
```

### Run the Application

```shell 
    python main.py
```


