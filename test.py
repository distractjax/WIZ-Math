from tests.test_frontend import tui_main_loop
from tests import test_backend
from curses import wrapper

def main():
    # wrapper(tui_main_loop)
    # test_backend.create_overview()
    # test_backend.create_module_view()
    test_backend.create_history_view()

if __name__ == "__main__":
    main()
