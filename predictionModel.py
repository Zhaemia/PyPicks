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
        Return the percentage
            '''
            count = self.gamelogs[self.cat].gt(self.statLine).sum()
            rows = len(self.gamelogs)
            total = count / rows
            percentage = int(round(total * 100))
            print(f" Hit percentage: {percentage}%")

            if percentage >= 65:
                 return f"This line has a chance of hitting. \n Percentage: {percentage}%\nBot Strongly recommends  O"
            elif percentage >= 50:
                 return f"This line has a chance of hitting. \n Percentage: {percentage}%\nBot says choose O"
            elif percentage >= 40:
                 return f"This line has a low chance of hitting. \n Percentage: {percentage}%\nBot Strongly recommends  U"
            else:
                 return f"This line has No chance of hitting. \n Percentage: {percentage}%\n Dont bet."
            


    


        