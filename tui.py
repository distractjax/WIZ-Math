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


# stdscr is already global because of how the wrapper works.
def tui_event_loop(stdscr):
    curses.use_default_colors()
    stdscr.keypad(True)
    curses.curs_set(2)
    stdscr.clear()

    # Header needs to be global
    global header
    header = 'Main Menu'
    # Footer needs to be global
    global footer
    footer = ""

    # TODO: Find a better fix for this. Use a textwrap function to handle it.
    # These all belong to one specific loop
    sub1_cols = (curses.COLS - 6) // 3
    remain_cols = curses.COLS - 6 - sub1_cols

    sub1 = stdscr.subwin(curses.LINES - 3, sub1_cols, 1, 2)

    sub2_lines = 3 * (curses.LINES - 5) // 4
    sub2 = stdscr.subwin(sub2_lines,remain_cols + 3, 1, sub1_cols + 2)

    sub3_lines = curses.LINES - 5 - sub2_lines
    sub3 = stdscr.subwin(sub3_lines,remain_cols - 2, sub2_lines + 2, sub1_cols + 3)

    sub1.keypad(True)
    sub1.leaveok(False)
    sub2.keypad(True)
    sub2.leaveok(False)
    sub3.keypad(True)
    sub3.leaveok(False)

    active_idx = 0

    options = [x for x in function_dicts.category_dict.keys()]
    options.append('Quit')

    global sidebar_contents
    sidebar_contents = options.copy()

    # These need to be global
    y, x = 1, 2
    global side_y, side_x
    side_y, side_x = y, x

    while True:
        stdscr.addstr(0,2,header,curses.A_BOLD)
        stdscr.clrtoeol()
        stdscr.addstr(curses.LINES-2,2,footer,curses.A_BOLD)

        sub1.border()
        sub2.border()

        rectangle(stdscr,sub2_lines + 1, sub1_cols + 2, curses.LINES - 3, curses.COLS - 2)

        for a,b in enumerate(sidebar_contents):
            sub1.addstr(a+1,1,f'[ ] {b}')

        stdscr.noutrefresh()
        sub1.noutrefresh()
        sub2.noutrefresh()
        sub3.noutrefresh()

        y, x = side_y, side_x
        sub1.move(y,x)

        curses.doupdate()

        # This can be local
        c = sub1.getch()

        # 10 is the ASCII character for the ENTER key. DO NOT USE curses.KEY_ENTER, it's for numpad enter.
        if c == 10:
            if sidebar_contents[y-1] == '<-':
                sub1.clear()
                sub2.clear()
                header = 'Main Menu'
                sidebar_contents = options.copy()
            elif sidebar_contents[y-1] == 'Quit':
                break
            elif header == 'Main Menu':
                sub1.clear()
                prev_header = header
                header = sidebar_contents[y-1]
                sidebar_contents = [x.title() for x in function_dicts.category_dict[header].keys()]
                sidebar_contents.insert(0,'<-')
                sidebar_contents.append('Quit')
            else:
                function_dicts.foundations_dict[sidebar_contents[y-1].lower()]()
                question = config.read_question()
                sub2.clear()
                sub2.addstr(1,1,f'{question}')
                sub2.border()
                sub2.refresh()
                answer_question(sub3,sub2)
        else:
            handle_cursor(c)
