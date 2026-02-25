from collections import defaultdict
from random import randint
import json
import time
import sqlite3
from os import path, mkdir

# This is a file for all of the global variables in my program.

# Globals
APP_PATH = path.expanduser('~/.local/share/gre-prep')
JSON_PATH = path.join(APP_PATH,'print_contents.json')
SQLITE_PATH = path.join(APP_PATH,'gre_prep.db')

# Confirm the existence of your gre-prep directory.
def ensure_application_path():
    if path.isdir(APP_PATH):
        pass
    else:
        try:
            mkdir(APP_PATH)
        except PermissionError:
            print(f'Permission denied: failed to create application directory.')
        except Exception as e:
            print(f'An error occurred: {e}')

# Read and Write from JSON
def write_solution(question: str, answer: str, filepath: str = JSON_PATH) -> None:
    '''
    This is a function that writes the question and answer provided to a JSON file.
    '''
    json_dict = {'question': question, 'answer': answer}
    with open(filepath, 'w') as jfp:
        json.dump(json_dict,fp=jfp)

def read_question(filepath: str = JSON_PATH) -> dict[str]:
    '''
    This is a function that reads the question and answer out of a provided JSON file.
    '''
    with open(filepath, 'r') as jfp:
        json_dict = json.load(jfp)
    return json_dict['question']

# Read and write from SQLite DB
def ensure_sqlite_table(cursor, table_name: str, column_names: list[str]) -> None:
    '''
    This checks if a table exists in a SQLite database that you're connected to and creates it if it doesn't.
    '''
    cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    if cursor.fetchone()[0] == 1:
        pass
    else:
        columns = ', '.join(column_names)
        cursor.execute(f"CREATE TABLE {table_name}({columns}) WITHOUT ROWID")
        pass

def write_db(question: str = '', answer: str = '', filepath: str = SQLITE_PATH) -> None:
    '''
    This is a function that writes the question, answer, time and truth value of the answer to a database.
    '''
    with sqlite3.connect(filepath) as conn:
        c = conn.cursor()
        ensure_sqlite_table(c, "problem_history", ["exec_time primary key","q_type","q_func","was_right","solve_time"])


# Check Solution from frontend
def check_solution(user_in: str, filepath: str = JSON_PATH) -> str:
    '''
    This is a function that checks if the user's provided solution is the same as the answer in the json object.
    '''
    user_in = ''.join([ch for ch in user_in if not ch.isspace()])
    with open(filepath,'r') as jfp:
        json_dict = json.load(jfp)
    if user_in == str(json_dict['answer']):
        return f'Correct! The answer is {json_dict["answer"]}.'
    else: 
        return f'Incorrect! The answer is {json_dict["answer"]}.'
