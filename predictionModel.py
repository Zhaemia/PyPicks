import pandas as pd
class PredictionModel:
    def __init__(self, gamelogs: pd.DataFrame, cat: str, statLine: int):
        self.gamelogs = gamelogs
        self.cat = cat
        self.statLine = statLine
        
    def hitRate(self):
        '''
        Loop through the games in self.gamelogs
        Check how many times self.cat (e.g. PTS) was greater than self.statLine
        Return the percentage'''

        