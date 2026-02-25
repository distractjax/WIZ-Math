# Arithmetic and Number Properties Practice

from curses import wrapper
from tui import tui_main_loop
from config import ensure_application_path, write_db

def main():
    ensure_application_path()
    write_db()
    wrapper(tui_main_loop)

if __name__ == "__main__":
    main()
