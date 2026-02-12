import json

def json_test():
    test_output = {'1': 'I love Skyler', '2': 'Hello, world!'}
    print(test_output)
    with open('./print_contents.json', 'w') as test_file:
        json.dump(test_output,fp=test_file)
    with open('./print_contents.json', 'r') as test_file:
        test_input = json.load(fp=test_file)
    print(test_input)
    if test_input == test_output:
        print('Success!')
    else:
        print('Failure')

def json_update_test():
    with open('./print_contents.json','r') as test_file:
        test_output = json.load(test_file)
    test_output['3'] = 'Hello, world!'
    with open('./print_contents.json','w') as test_file:
        json.dump(test_output,fp=test_file)

def check_answer():
    with open('./print_contents.json','r') as test_file:
        test_input = json.load(test_file)
    if test_input['2'] == test_input['3']:
        print('Success!')

if __name__ == '__main__':
    json_test()
    json_update_test()
    check_answer()
