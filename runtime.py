from backend import function_dicts, model, update, view
from json import loads

def main():
    state = model.GlobalState(problem_history = None)
    while state.is_running:
        try frontend := loads(state.frontend_json_path):
            pass
        finally:
            pass
        
    pass

if __name__ == "__main__":
    main()
