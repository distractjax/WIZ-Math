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

def tui_event_loop(stdscr):
    curses.use_default_colors()
    stdscr.keypad(True)
    curses.curs_set(2)
    stdscr.clear()
    header = 'Main Menu'
    prev_header = header
    footer = ""

    sub1_cols = (curses.COLS - 6) // 5
    remain_cols = curses.COLS - 6 - sub1_cols

    sub1 = stdscr.subwin(curses.LINES - 3, sub1_cols, 1, 2)

    sub2_lines = 3 * (curses.LINES - 5) // 4
    sub2 = stdscr.subwin(sub2_lines,remain_cols + 3, 1, sub1_cols + 2)

    sub3_lines = curses.LINES - 5 - sub2_lines
    sub3 = stdscr.subwin(sub3_lines,remain_cols - 2, sub2_lines + 2, sub1_cols + 3)

    input_windows = [sub1, sub3]
    for i, w in enumerate(input_windows):
        w.keypad(True)
        w.leaveok(False)
    sub2.keypad(True)
    sub2.leaveok(False)

    active_idx = 0

    options = [x for x in function_dicts.category_dict.keys()]
    options.append('Quit')

    sidebar_contents = options.copy()

    y, x = 1, 2
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
        for w in input_windows:
            w.noutrefresh()
        sub2.noutrefresh()

        target_win = input_windows[active_idx]
        if active_idx == 0:
            y, x = side_y, side_x
        target_win.move(y,x)

        curses.doupdate()

        c = target_win.getch()

        if c == curses.KEY_RIGHT:
            active_idx = (active_idx + 1) % len(input_windows)
            if active_idx == 1:
                y, x = 0, 0

        elif c == curses.KEY_LEFT:
            active_idx = (active_idx - 1) % len(input_windows)
            if active_idx == 1:
                y, x = 0, 0

        elif c == curses.KEY_UP:
            if active_idx == 0:
                side_y = len(sidebar_contents) if side_y <= 1 else side_y - 1

        elif c == curses.KEY_DOWN:
            if active_idx == 0:
                side_y = 1 if side_y >= len(sidebar_contents) else side_y + 1

        # 10 is the ASCII character for the ENTER key. DO NOT USE curses.KEY_ENTER, it's for numpad enter.
        elif c == 10:
            if active_idx == 0:
                if sidebar_contents[y-1] == '<-':
                    target_win.clear()
                    sub2.clear()
                    header = prev_header
                    sidebar_contents = options.copy()
                elif sidebar_contents[y-1] == 'Quit':
                    break
                elif header == 'Main Menu':
                    target_win.clear()
                    prev_header = header
                    header = sidebar_contents[y-1]
                    sidebar_contents = [x.title() for x in function_dicts.category_dict[header].keys()]
                    sidebar_contents.insert(0,'<-')
                    sidebar_contents.append('Quit')
                else:
                    function_dicts.foundations_dict[sidebar_contents[y-1].lower()]()
                    question = config.read_question()
                    sub2.addstr(1,1,f'{question}')
                    sub2.clrtoeol()
            elif active_idx == 1:
                tb = Textbox(sub3)
                tb.edit(enter_is_terminate)
                answer = tb.gather().strip()
                message = config.check_solution(answer)

                sub2.addstr(1,1,f'{message}')
                sub2.clrtoeol()
                sub3.clear()
