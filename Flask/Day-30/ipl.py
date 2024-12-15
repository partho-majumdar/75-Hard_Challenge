import numpy as np
import pandas as pd

matches = pd.read_csv("./ipl-matches.csv")
print(matches.head())


def teamsAPI():
    teams = list(set(list(matches["Team1"]) + list(matches["Team2"])))
    team_dict = {"teams": teams}
    return team_dict

def teamVteamAPI(team1, team2):
    temp_df = matches[((matches['Team1'] == team1) & (matches['Team2'] == team2)) | ((matches['Team1'] == team2) & (matches['Team2'] == team1))]

    total_matches = temp_df.shape[0]
    winning_count = temp_df['WinningTeam'].value_counts()

    matches_won_team1 = winning_count.get(team1, 0)
    matches_won_team2 = winning_count.get(team2, 0)

    # Rule - 02 this give me error when total matches == 1
    # matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
    # matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]
    
    matches_draw = total_matches - (matches_won_team1 + matches_won_team2)

    response = {
        'total_matches': total_matches,
        team1: (int)(matches_won_team1),
        team2: (int)(matches_won_team2),
        'matches_draw': (int)(matches_draw),
    } 
    return response
