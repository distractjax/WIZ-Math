import curses
from curses.textpad import rectangle, Textbox
from backend import function_dicts
import config
import json

# stdscr is already global because of how the wrapper works.
def stats_loop(print_win):
    ind = 0
    while True:
        print_win.border()
        print_win.addstr(1,2,'')
        stat_views = function_dicts.category_dict['Stats'].keys()
        for x, y in enumerate(stat_views):
            if x == ind:
                print_win.addstr(y, curses.A_BOLD)
            else:
                print_win.addstr(y)
            print_win.addstr(" | ")
        print_win.refresh()
        c = print_win.getch()
        if c == curses.ascii.ESC:
            break
        elif c == curses.KEY_LEFT:
            ind = len(stat_views) - 1 if ind <= 1 else ind - 1
        elif c == curses.KEY_RIGHT:
            ind = 1 if ind >= len(stat_views) else ind + 1

        # stdscr.clrtoeol()
        # stdscr.addstr(curses.LINES-2,2,footer,curses.A_BOLD)
        #
        # sidebar.border()
        # print_win.border()
        #
        # rectangle(stdscr,1, sidebar_cols + 2, curses.LINES - 3, curses.COLS - 2)
        #
        # for a,b in enumerate(sidebar_contents):
        #     sidebar.addstr(a+1,1,f'[ ] {b}')
        #
        # stdscr.noutrefresh()
        # sidebar.noutrefresh()
        # print_win.noutrefresh()
        #
        # y, x = side_y, side_x
        # sidebar.move(y,x)
        #
        # curses.doupdate()
        #
        # # This can be local
        # c = sidebar.getch()
        #
        # # 10 is the ASCII character for the ENTER key. DO NOT USE curses.KEY_ENTER, it's for numpad enter.
        # if c == 10:
        #     if sidebar_contents[y-1] == '<-':
        #         sidebar.clear()
        #         print_win.clear()
        #         header_set.pop()
        #         sidebar_contents = [x for x in function_dicts.category_dict.keys()]
        #         sidebar_contents.append('Quit')
        #     elif sidebar_contents[y-1] == 'Stats':
        #         print_win.clear()
        #         header_set.append(sidebar_contents[y-1])
        #         tests.stats.stats_window(stdscr, )
        #
        #     elif sidebar_contents[y-1] == 'Quit':
        #         break
        #     elif header == 'Main Menu':
        #         sidebar.clear()
        #         header_set.append(sidebar_contents[y-1])
        #         sidebar_contents = [x.title() for x in function_dicts.category_dict[sidebar_contents[y-1]].keys()]
        #         sidebar_contents.insert(0,'<-')
        #         sidebar_contents.append('Quit')
        #     else:
        #         function_dicts.foundations_dict[sidebar_contents[y-1].lower()]()
        #         question = config.read_question_json()
        #         print_win.clear()
        #         print_win.addstr(1,1,f'{question}')
        #         print_win.border()
        #         print_win.refresh()
        # else:
        #     handle_cursor(c)
