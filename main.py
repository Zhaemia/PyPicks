import players
import logger
import predictionModel
import matplotlib.pyplot as plt
import pandas as pd
def main():

    
    new_player = players.Player()
    player = input("Please enter a name: ")
    print("\n")
    id, players_name = new_player.get_player(player)
    print(f"\nPlayer selected: {players_name}\n")

    game_log = logger.Logger(id)
    logs = game_log.get_last_15_games()
    # homeGames, awayGames, homeAvg, awayAvg = game_log.home_away_differential(logs)
    print(logs, "\n\nStat Categories:\n")
    
    
    for i, c in enumerate(logs.columns[2:], 1):
        print("-", i, c)
    print("\n")
    while True:

        try:
        
            category = str(input("Enter a stat to calculate: ").upper())
            print("\n")
            if category in logs.columns:
                break
            else:
                print("Column not found please try this again\n")
                print(logs.columns)

        except:
            "Enter a valid column"

    
    while True:

        try:
            line = float(input("Enter prediction stat: "))
            break
        except: 
            print("Please enter number. ")
      
    p = predictionModel.PredictionModel(logs, category.upper(), line)
    print (p.hitRate())

    
    
   

    





if __name__ == "__main__":
    main()

