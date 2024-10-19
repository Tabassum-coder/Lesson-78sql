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

season=pd.read_sql("""Select * from Season;""",conn)
print(season)


# Fetch Details of all matches played by CSK in year 2015
csk_matches_2015 = pd.read_sql("""SELECT Match_Id, Team_2 as Away_Team,
Toss_Winner, Match_Winner
FROM Match
WHERE Team_1 =
(SELECT Team_1
FROM Match
WHERE Team_1 = 3 AND Season_Id =
8); """, conn)
print("Matches Played By Chennai Super Kings in Year 2015")
print(csk_matches_2015)
# Fetch Details of all matches won by CSK in year 2015
csk_wins=pd.read_sql("""SELECT *
FROM Match
WHERE Match_Winner = 3 AND Season_Id = 8;""", conn)
print("Matches won by CSK as Home Team in Year 2015")
print(csk_wins)
# Fetch details of all the matches
# where batsman score more than 5 in year 2015
match_runs = pd.read_sql("""SELECT Match_Id, Runs_Scored as Total_Runs,
Innings_No
FROM Batsman_Scored
WHERE Total_Runs > 5 AND Match_Id IN
(SELECT Match_Id
FROM Match
WHERE Season_Id = 8);""", conn)
print("Matches with Scored Runs Greater Than 5 in Year 2015")
print(match_runs)
# Fetch details of Matches played in year 2015
# where Total Runs Scored were greater than average scored run
avg_runs = pd.read_sql("""SELECT Match_Id, Runs_Scored as Total_Runs,
Innings_No
FROM Batsman_Scored
WHERE Innings_No = 1 AND Runs_Scored >
(SELECT AVG(Runs_Scored)
FROM Batsman_Scored); """, conn)
print("Matches with Scored Runs Greater Than Average Scored Runs")
print(avg_runs)