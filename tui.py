import curses
from curses.textpad import rectangle, Textbox
from foundations import foundations_picker

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
    main_header = 'Main Menu'
    header = main_header
    footer = "Type 'Quit' to exit"

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

    options = ['Foundations', 'Quit']
    foundations_options = [x.title() for x in foundations_picker.function_dict.keys()]
    foundations_options.insert(0,'<-')
    foundations_options.append('Quit')

    sidebar_contents = options.copy()

    y, x = 1, 2

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
        target_win.move(y,x)

        curses.doupdate()

        c = target_win.getch()

        if c == curses.KEY_RIGHT:
            active_idx = (active_idx + 1) % len(input_windows)
            if active_idx == 0:
                y, x = 1, 2
            elif active_idx == 1:
                y, x = 0, 0

        elif c == curses.KEY_LEFT:
            active_idx = (active_idx - 1) % len(input_windows)
            if active_idx == 0:
                y, x = 1, 2
            elif active_idx == 1:
                y, x = 0, 0

        elif c == curses.KEY_UP:
            y -= 1

        elif c == curses.KEY_DOWN:
            y += 1

        # 10 is the ASCII character for the ENTER key. DO NOT USE curses.KEY_ENTER, it's for numpad enter.
        elif c == 10:
            if active_idx == 0:
                if sidebar_contents[y-1] == 'Foundations':
                    target_win.clear()
                    header = options[0]
                    sidebar_contents = foundations_options.copy()
                elif sidebar_contents[y-1] == '<-':
                    target_win.clear()
                    header = main_header
                    sidebar_contents = options.copy()
                elif sidebar_contents[y-1] == 'Quit':
                    break
            elif active_idx == 1:
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
