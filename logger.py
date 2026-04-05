
from nba_api.stats.endpoints import playergamelog
import pandas as pd

class Logger:

    def create_file(self):
        pass
    #TODO make a function that returns self.dateframe to a newfile that is appended by
    #1 or a certain value  each time it is called to ensure a new file is made. This is not a top priorty 
    #Complete whenever.

    def __init__(self, id: int):
        self.id = id
        

    
    def log_games(self):

        #GATHER GAME LOGS FROM PLAYER ID
        gamelogs = playergamelog.PlayerGameLog(self.id)
        log = gamelogs.get_data_frames()[0]
        
        #RETURN PREVIOUS 15 GAMES 
        return log.head(15)
    

    def get_last_15_games(self) -> pd.DataFrame:

        df = self.log_games()

        working_list = df[['GAME_DATE', 'MATCHUP', 'PTS', 'REB', 'AST']].copy()
        working_list['PRA'] = working_list['PTS'] + working_list['REB'] + working_list['AST']
        working_list['PR'] = working_list['PTS'] + working_list['REB'] 
        working_list['PA'] = working_list['PTS']  + working_list['AST']
        working_list['RA'] = working_list['REB'] + working_list['AST']
        return working_list




        
        
    #Find games by certain matchups
    def search_by_matchup(self, game_log: pd.DataFrame):
        selection = input("Do you wish to search by matchups: Y/N ")
        if selection.upper() == 'N':
            print(game_log)
            return game_log
        
        #GET ABBREVIATION
        matchup = input("Please select the match up: (ex: LAL) ")

        # Get the last 3 str from DF EX GSW @ LAL turns to just LAL
        series = game_log[game_log['MATCHUP'].str[-3:] == matchup]

        #CHECK IF THE DF WILL RETURN EMPTY
        if  series.empty:
           
           print(f"Curry hasnt played bro in the last few games, here is the full list of recents games:\n {game_log}")
           #RETURN CURRENT LIST OF DF
           return game_log
        
        
        #IF DF ISNT EMPTY RETURN SERIES
        return series
    

    def home_away_differential(self, df: pd.DataFrame):
        away_games = df[df['MATCHUP'].str.contains('@')]
        home_games = df[df['MATCHUP'].str.contains('vs')]
        home_games_average = home_games[['PTS', 'REB', 'AST', 'PRA', 'PR', 'PA', 'RA']].mean()
        away_game_average = away_games[['PTS', 'REB', 'AST', 'PRA', 'PR', 'PA', 'RA']].mean()
        print("HOME AVERAGES")
        print(home_games[['PTS', 'REB', 'AST', 'PRA', 'PR', 'PA', 'RA']].mean())
        print("\nAWAY AVERAGES")
        print(away_games[['PTS', 'REB', 'AST', 'PRA', 'PR', 'PA', 'RA']].mean())

        return home_games, away_games, home_games_average, away_game_average
    

    def show_home_games(self, homeGames: pd.DataFrame):
        print(homeGames)
        return homeGames
        

    def show_away_games(self, awayGames: pd.DataFrame):
        print(awayGames)
        return awayGames
    

     #TODO make a function that returns self.dateframe to a newfile that is appended by
    #1 or a certain value  each time it is called to ensure a new file is made. This is not a top priorty 
    #Complete whenever.
        
    def create_file(self):
            pass
   


       

                  
        
