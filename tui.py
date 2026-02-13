import curses
from curses.textpad import rectangle, Textbox
import function_dicts
import config
import json

def enter_is_terminate(x):
    '''
    This just allows the user to use "Enter" instead of "Ctrl+G"
    to submit text in a Textbox.
    '''
    if x == 10:
        return 7
    return x

def handle_cursor(c):
    '''
    This function manages cursor movement.
    '''
    global sidebar_contents
    global side_y
    global side_x
    if c == curses.KEY_UP:
        side_y = len(sidebar_contents) if side_y <= 1 else side_y - 1

    elif c == curses.KEY_DOWN:
        side_y = 1 if side_y >= len(sidebar_contents) else side_y + 1

def answer_question(edit_win, results_win):
    '''
    This function moves the cursor and allows the user to answer questions.
    '''
    edit_win.move(0,0)
    tb = Textbox(edit_win)
    tb.edit(enter_is_terminate)
    answer = tb.gather().strip()
    message = config.check_solution(answer)

    results_win.addstr(1,1,f'{message}')
    results_win.clrtoeol()
    edit_win.clear()
    
    results_win.refresh()
    edit_win.refresh()

def tui_questions_loop(stdscr):
    '''
    This handles the loop for answering questions.
    '''
    return None

# stdscr is already global because of how the wrapper works.
def tui_main_loop(stdscr):
    '''
    This handles the primary program loop.
    '''
    curses.use_default_colors()
    stdscr.keypad(True)
    curses.curs_set(2)
    stdscr.clear()

    # Header needs to be global
    global header_set
    header_set = ['Main Menu']
    # Footer needs to be global
    global footer
    footer = ""

    # TODO: Find a better fix for this. Use a textwrap function to handle it.
    # These all belong to one specific loop
    global sidebar_cols
    sidebar_cols = (curses.COLS - 6) // 3
    global remain_cols
    remain_cols = curses.COLS - 6 - sidebar_cols

    global sidebar
    sidebar = stdscr.subwin(curses.LINES - 3, sidebar_cols, 1, 2)

    print_win_lines = 3 * (curses.LINES - 5) // 4
    print_win = stdscr.subwin(print_win_lines,remain_cols + 3, 1, sidebar_cols + 2)

    textbox_lines = curses.LINES - 5 - print_win_lines
    textbox = stdscr.subwin(textbox_lines,remain_cols - 2, print_win_lines + 2, sidebar_cols + 3)

    sidebar.keypad(True)
    sidebar.leaveok(False)
    print_win.keypad(True)
    print_win.leaveok(False)
    textbox.keypad(True)
    textbox.leaveok(False)

    global sidebar_contents
    sidebar_contents = [x for x in function_dicts.category_dict.keys()]
    sidebar_contents.append('Quit')

    # These need to be global
    y, x = 1, 2
    global side_y, side_x
    side_y, side_x = y, x

    while True:
        header = header_set[-1]
        stdscr.addstr(0,2,header,curses.A_BOLD)
        stdscr.clrtoeol()
        stdscr.addstr(curses.LINES-2,2,footer,curses.A_BOLD)

        sidebar.border()
        print_win.border()

        rectangle(stdscr,print_win_lines + 1, sidebar_cols + 2, curses.LINES - 3, curses.COLS - 2)

        for a,b in enumerate(sidebar_contents):
            sidebar.addstr(a+1,1,f'[ ] {b}')

        stdscr.noutrefresh()
        sidebar.noutrefresh()
        print_win.noutrefresh()
        textbox.noutrefresh()

        y, x = side_y, side_x
        sidebar.move(y,x)

        curses.doupdate()

        # This can be local
        c = sidebar.getch()

        # 10 is the ASCII character for the ENTER key. DO NOT USE curses.KEY_ENTER, it's for numpad enter.
        if c == 10:
            if sidebar_contents[y-1] == '<-':
                sidebar.clear()
                print_win.clear()
                header_set.pop()
                sidebar_contents = [x for x in function_dicts.category_dict.keys()]
                sidebar_contents.append('Quit')
            elif sidebar_contents[y-1] == 'Quit':
                break
            elif header == 'Main Menu':
                sidebar.clear()
                header_set.append(sidebar_contents[y-1])
                sidebar_contents = [x.title() for x in function_dicts.category_dict[sidebar_contents[y-1]].keys()]
                sidebar_contents.insert(0,'<-')
                sidebar_contents.append('Quit')
            else:
                function_dicts.foundations_dict[sidebar_contents[y-1].lower()]()
                question = config.read_question()
                print_win.clear()
                print_win.addstr(1,1,f'{question}')
                print_win.border()
                print_win.refresh()
                answer_question(textbox,print_win)
        else:
            handle_cursor(c)
