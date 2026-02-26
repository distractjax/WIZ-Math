# Arithmetic and Number Properties Practice

from curses import wrapper
from frontend.tui import tui_main_loop
from config import ensure_application_path

def main():
    ensure_application_path()
    wrapper(tui_main_loop)

if __name__ == "__main__":
    main()
