from collections import defaultdict
from random import randint
import json
import time
import sqlite3
from os import path

# This is a file for all of the global variables in my program.

# Globals
json_filepath = './print_contents.json'
db_filepath = './userDB.db'

# Dictionaries

# Read and Write from JSON
def write_solution(question: str, answer: str, filepath: str = json_filepath) -> None:
    '''
    This is a function that writes the question and answer provided to a JSON file.
    '''
    json_dict = {'question': question, 'answer': answer}
    with open(filepath, 'w') as jfp:
        json.dump(json_dict,fp=jfp)

def read_question(filepath: str = json_filepath) -> dict[str]:
    '''
    This is a function that reads the question and answer out of a provided JSON file.
    '''
    with open(filepath, 'r') as jfp:
        json_dict = json.load(jfp)
    return json_dict['question']

# Read and write from DB
def write_db

# Check Solution from frontend
def check_solution(user_in: str, filepath: str = json_filepath) -> str:
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
