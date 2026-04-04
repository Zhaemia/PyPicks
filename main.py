import players
import logger
import predictionModel
import matplotlib.pyplot as plt
import pandas as pd
def main():

    
    new_player = players.Player()
    player = input("Please enter a name: ")
    id = new_player.get_player(player)

    game_log = logger.Logger(id)
    logs = game_log.get_last_15_games()
    # homeGames, awayGames, homeAvg, awayAvg = game_log.home_away_differential(logs)
    print(logs)
    

    print(logs.columns)
    while True:

        try:
        
            category = str(input("Enter a stat to calculate").upper())
            if category in logs.columns:
                break
            else:
                print("Column not found please try this again")
                print(logs.columns)

        except:
            "Enter a valid column"

    
    while True:

        try:
            line = int(input("Enter prediction stat: "))
            break
        except: 
            print("Please enter number. ")
      
    p = predictionModel.PredictionModel(logs, category.upper(), line)
    print (p.hitRate())

    
    
   

    





if __name__ == "__main__":
    main()

