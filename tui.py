import curses
from curses.textpad import rectangle, Textbox

def enter_is_terminate(x):
    '''
    This just allows the user to use "Enter" instead of "Ctrl+G"
    to submit text in a Textbox.
    '''
    if x == 10:
        return 7
    return x

def tui_event_loop(stdscr):
    stdscr = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(2)
    stdscr.clear()
    header = 'Testing zone'
    footer = "Type 'Quit' to exit"
    while True:
        stdscr.addstr(0,2,header,curses.A_BOLD)
        stdscr.addstr(curses.LINES-2,2,footer,curses.A_BOLD)
        sub1_cols = (curses.COLS - 6) // 5
        remain_cols = curses.COLS - 6 - sub1_cols
        sub1 = stdscr.subwin(curses.LINES - 3, sub1_cols, 1, 2)
        sub1.border()
        sub2_lines = 3 * (curses.LINES - 5) // 4
        sub3_lines = curses.LINES - 5 - sub2_lines
        sub2 = stdscr.subwin(sub2_lines,remain_cols + 3, 1, sub1_cols + 2)
        sub3 = stdscr.subwin(sub3_lines,remain_cols - 2, sub2_lines + 2, sub1_cols + 3)
        sub2.border()
        rectangle(stdscr,sub2_lines + 1, sub1_cols + 2, curses.LINES - 3, curses.COLS - 2)
        tb = Textbox(sub3)
        stdscr.refresh()
        tb.edit(enter_is_terminate)
        message = tb.gather().strip()
        if message.lower() == 'quit':
            break
        else:
            sub2.addstr(1,1,f'{message}')
            sub2.clrtoeol()
        sub3.clear()

curses.wrapper(tui_event_loop)
