from tests.test_frontend import tui_main_loop
from tests import test_backend
from curses import wrapper

def main():
    # wrapper(tui_main_loop)
    test_backend.table_to_df()


if __name__ == "__main__":
    main()
