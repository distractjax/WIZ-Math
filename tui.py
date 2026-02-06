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
    while True:
        sub1_lines = 3 * (curses.LINES - 4) // 4
        sub2_lines = curses.LINES - 4 - sub1_lines
        sub1 = stdscr.subwin(sub1_lines,curses.COLS - 3, 1, 2)
        sub2 = stdscr.subwin(sub2_lines,curses.COLS - 5, sub1_lines + 2, 3)
        sub1.border()
        rectangle(stdscr,sub1_lines + 1, 2, curses.LINES - 2, curses.COLS - 2)
        tb = Textbox(sub2)
        stdscr.refresh()
        tb.edit(enter_is_terminate)
        message = tb.gather().strip()
        if message == 'quit':
            break
        else:
            sub1.addstr(1,1,f'{message}')
            sub1.clrtoeol()
        sub2.clear()

curses.wrapper(tui_event_loop)
