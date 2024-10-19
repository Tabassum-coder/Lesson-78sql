import pandas as pd
import sqlite3

database='database.sqlite'
conn=sqlite3.connect(database)
print("Database opened successfully")

# tables=pd.read_sql("""Select * from sqlite_master where type='table';""",conn)
# print(tables)

match=pd.read_sql("""Select * from Match;""",conn)
print(match)

team=pd.read_sql("""Select * from Team;""",conn)
print(team)

match_win=pd.read_sql("""Select Match_Id,Team_Name as MatchWinner from Match as M inner join Team as T on M.Match_Winner=T.Team_Id;""",conn)
print(match_win)