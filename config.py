from collections import defaultdict
from random import randint
import json

# This is a file for all of the global variables in my program.

# Globals
json_filepath = './print_contents.json'

# Dictionaries

# General Functions
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

def check_solution(user_in: str, filepath: str = json_filepath) -> str:
    '''
    This is a function that checks if the user's provided solution is the same as the answer in the json object.
    '''
    user_in = ''.join([ch for ch in user_in if not ch.isspace()])
    with open(filepath,'r') as jfp:
        json_dict = json.load(jfp)
    if user_in == str(json_dict['answer']):
        return f'Success! The answer is {json_dict["answer"]}.'
    else: 
        return f'Failure! The answer is {json_dict["answer"]}.'

def function_picker(user_in: str, function_dict: dict[str]):
    user_in = user_in.lower().strip()
    keys = list(function_dict.keys())

    def show_options():
        print('\n'.join(x.title() for x in keys))
        return 2

    def run_random():
        random_key = keys[randint(0,len(keys)-1)]
        function_dict[random_key]()

    def handle_error():
        print("I'm sorry, I didn't understand your input. The options are:\n"+'\n'.join(x.title() for x in keys))
        return 2 

    function_map = defaultdict(lambda: handle_error)
    function_map.update(function_dict)
    function_map['get options'] = show_options
    function_map['random'] = run_random
    function_map['exit'] = lambda: "exit"
    result = function_map[user_in]()

    if result == "exit":
        return

    if result != 2:
        if input('Would you like to go again?\n').lower().strip() == 'no':
            return

    user_in = input('Which would you like to try?\n')
    function_picker(user_in,function_dict)

