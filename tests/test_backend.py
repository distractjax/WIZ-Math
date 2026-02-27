import pandas as pd
import numpy as np
import config
from sqlite3 import connect

def table_to_df(tablename: str = "problem_history", filepath: str = config.SQLITE_PATH):
    with connect(filepath) as conn:
        df = pd.read_sql(f"SELECT * FROM {tablename}",conn)
    df.replace(0,np.nan,inplace=True)
    return df

# Overview Window
# This is just a bar chart that gives the number of questions answered correctly/incorrectly
# by module. Currently, the only module is Functions.

def create_overview():
    df = table_to_df()
    df = df.groupby("q_type").count()
    df['was_wrong'] = df['exec_time'] - df['was_right']
    for x in [x for x in df.columns if x != 'was_wrong' and x != 'was_right']:
        df.drop(x, axis=1, inplace=True)
    df = df.transpose()
    print(df.to_json())

# Module Window

def create_module_view(module: str = "Foundations"):
    df = table_to_df()
    df = df[df['q_type'] == module].groupby("q_func").count()
    df['was_wrong'] = df['exec_time'] - df['was_right']
    for x in [x for x in df.columns if x != 'was_wrong' and x != 'was_right']:
        df.drop(x, axis=1, inplace=True)
    df = df.transpose()
    print(df.to_json())

# History Window

def create_history_view():
    df = table_to_df()
    df['exec_time'] = pd.to_datetime(df['exec_time'],format='%Y-%m-%d %H:%M:%S.%f')
    df['exec_time'] = df['exec_time'].dt.to_period("D")
    df = df.groupby('exec_time').count()
    df['was_wrong'] = df['q_type'] - df['was_right']
    for x in [x for x in df.columns if x != 'was_wrong' and x != 'was_right']:
        df.drop(x, axis=1, inplace=True)
    df = df.transpose()
    print(df.to_json())
    pass

# Rank Window

def create_rank_view():
    df = table_to_df()
    df.replace(0,np.nan,inplace=True)
    pass

if __name__ == '__main__':
    test()
