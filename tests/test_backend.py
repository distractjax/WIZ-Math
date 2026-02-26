import pandas as pd
import numpy as np
import config
from sqlite3 import connect

def table_to_df(tablename: str = "problem_history", filepath: str = config.SQLITE_PATH):
    with connect(filepath) as conn:
        df = pd.read_sql(f"SELECT * FROM {tablename}",conn)
    return df

# Overview Window
# This is just a bar chart that gives the number of questions answered correctly/incorrectly
# by module. Currently, the only module is Functions.

def create_overview():
    df = table_to_df()
    df.replace(0,np.nan,inplace=True)
    df = df.groupby("q_type").count()
    df['was_wrong'] = df['exec_time'] - df['was_right']
    for x in [x for x in df.columns if x != 'was_wrong' and x != 'was_right']:
        df.drop(x, axis=1, inplace=True)
    print(df.to_json())

# Module Window

def create_module_view():
    df = table_to_df()
    df = table_to_df()
    df.replace(0,np.nan,inplace=True)
    df = df.groupby("q_func").count()
    df['was_wrong'] = df['exec_time'] - df['was_right']
    for x in [x for x in df.columns if x != 'was_wrong' and x != 'was_right']:
        df.drop(x, axis=1, inplace=True)
    print(df.to_json())

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
