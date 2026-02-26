import pandas
import config
from sqlite3 import connect

def test():
    conn = connect(config.SQLITE_PATH)
    df = pandas.read_sql("SELECT * FROM problem_history",conn)
    print(df)

if __name__ == '__main__':
    test()
