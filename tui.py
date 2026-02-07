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
    curses.use_default_colors()
    stdscr.keypad(True)
    curses.curs_set(2)
    stdscr.clear()
    header = 'Testing zone'
    footer = "Type 'Quit' to exit"

    sub1_cols = (curses.COLS - 6) // 5
    remain_cols = curses.COLS - 6 - sub1_cols

    sub1 = stdscr.subwin(curses.LINES - 3, sub1_cols, 1, 2)

    sub2_lines = 3 * (curses.LINES - 5) // 4
    sub2 = stdscr.subwin(sub2_lines,remain_cols + 3, 1, sub1_cols + 2)

    sub3_lines = curses.LINES - 5 - sub2_lines
    sub3 = stdscr.subwin(sub3_lines,remain_cols - 2, sub2_lines + 2, sub1_cols + 3)

    windows = [sub1, sub2, sub3]
    for i, w in enumerate(windows):
        w.keypad(True)
        w.leaveok(False)

    active_idx = 0

    while True:
        stdscr.addstr(0,2,header,curses.A_BOLD)
        stdscr.addstr(curses.LINES-2,2,footer,curses.A_BOLD)

        sub1.border()
        sub2.border()

        rectangle(stdscr,sub2_lines + 1, sub1_cols + 2, curses.LINES - 3, curses.COLS - 2)

        stdscr.noutrefresh()
        for w in windows:
            w.noutrefresh()

        target_win = windows[active_idx]
        target_win.move(1, 1)

        curses.doupdate()

        c = target_win.getch()

        if c == curses.KEY_RIGHT:
            active_idx = (active_idx + 1) % len(windows)

        elif c == curses.KEY_LEFT:
            active_idx = (active_idx - 1) % len(windows)

        elif c == curses.KEY_DOWN:
            active_idx = 2
            sub3.move(0,0)

            tb = Textbox(sub3)
            tb.edit(enter_is_terminate)
            message = tb.gather().strip()

            if message.lower() == 'quit':
                break

            sub2.addstr(1,1,f'{message}')
            sub2.clrtoeol()
            sub3.clear()

        elif c == ord('q'):
            break

curses.wrapper(tui_event_loop)
