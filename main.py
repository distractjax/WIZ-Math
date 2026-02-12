# Arithmetic and Number Properties Practice

from foundations.foundations_picker import foundations_function_picker
from config import function_picker

section_dict = {
    'foundations':  foundations_function_picker
}

def main():
    user_in = input('What would you like to do? Type "Get Options" if you want to see all the available functions, or just select "Random" to get started.\nYou can also type "Exit" to quit the program.\n')
    function_picker(user_in, section_dict)

if __name__ == "__main__":
    main()
