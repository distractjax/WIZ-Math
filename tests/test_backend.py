import pandas
import config
from sqlite3 import connect

def table_to_df(tablename: str = "problem_history", filepath: str = config.SQLITE_PATH):
    conn = connect(filepath)
    df = pandas.read_sql(f"SELECT * FROM {tablename}",conn)
    return df

# Overview Window
# This is just a bar chart that gives the number of questions answered correctly/incorrectly
# by module. Currently, the only module is Functions.

def create_overview():
    df = table_to_df()
    pass

# Module Window

def create_module_view():
    df = table_to_df()
    pass

# History Window

def create_history_view():
    df = table_to_df()
    pass

# Rank Window

def create_rank_view():
    df = table_to_df()
    pass

if __name__ == '__main__':
    test()
