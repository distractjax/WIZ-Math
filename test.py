from tests.test_tui import tui_main_loop
from curses import wrapper

def main():
    wrapper(tui_main_loop)

if __name__ == "__main__":
    main()
