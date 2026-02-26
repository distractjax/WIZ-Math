from collections import defaultdict
from random import randint
import json
import datetime
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

# What functions do I actually need to be able to have?
# I need one that creates a new row in the problem_history table, initializing with exec_time, q_type and q_func.
# Then I need one that updates that table with was_right and solve_time
def create_question_row(exec_time: datetime.datetime, q_type: str, q_func: str, filepath: str = SQLITE_PATH) -> None:
    '''
    This function creates a new row in the problem_history table with values for exec_time, q_type and q_func.
    '''
    with sqlite3.connect(filepath) as conn:
        c = conn.cursor()
        ensure_sqlite_table(c, "problem_history", ["exec_time primary key","q_type","q_func","was_right","solve_time"])
        sql = '''INSERT INTO problem_history (exec_time, q_type, q_func)
            VALUES(?, ?, ?);'''
        c.execute(sql, (exec_time,q_type,q_func))

def update_question_row(was_right: bool, exec_time: str, filepath: str = SQLITE_PATH) -> None:
    '''
    This function updates a row in the problem_history table with values for was_right and solve_time.
    '''
    exec_time = datetime.datetime.strptime(exec_time, "%Y-%m-%d %H:%M:%S.%f") 
    end_time = datetime.datetime.now()
    with sqlite3.connect(filepath) as conn:
        c = conn.cursor()
        sql = '''UPDATE problem_history
            SET was_right = ?, solve_time = ?
            WHERE exec_time = ?;
        '''
        c.execute(sql, (was_right, (exec_time - end_time).total_seconds(), exec_time))

# Read and Write from JSON
# Let me actually think about this. The point of the JSON file is to communicate between the frontend
# and the backend. So the only things that need to be in the JSON file are things that both
# the frontend and the backend need to know. I just need to write SQL functions that communicate the information
# when the function runs on the backend to the DB.
def write_solution_json(exec_time: datetime.datetime, question: str, answer: str, filepath: str = JSON_PATH) -> None:
    '''
    This is a function that writes the question and answer provided to a JSON file.
    '''
    json_dict = {'question': question, 
                 'answer': answer,
                 'exec_time': str(exec_time),
                 }
    with open(filepath, 'w') as jfp:
        json.dump(json_dict,fp=jfp)

def read_question_json(filepath: str = JSON_PATH) -> dict[str]:
    '''
    This is a function that reads the question and answer out of a provided JSON file.
    '''
    with open(filepath, 'r') as jfp:
        json_dict = json.load(jfp)
    return json_dict['question']

# Check Solution from frontend
def check_solution(user_in: str, filepath: str = JSON_PATH) -> str:
    '''
    This is a function that checks if the user's provided solution is the same as the answer in the json object.
    '''
    user_in = ''.join([ch for ch in user_in if not ch.isspace()])
    with open(filepath,'r') as jfp:
        json_dict = json.load(jfp)

    was_right = user_in == str(json_dict['answer'])

    update_question_row(was_right, json_dict['exec_time'])
    return f'{['Incorrect!', 'Correct!'][was_right]} The answer is {json_dict["answer"]}.'
