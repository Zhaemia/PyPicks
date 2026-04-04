import players
import logger
import matplotlib.pyplot as plt
import pandas as pd
def main():

    
    new_player = players.Player()
    player = input("Please enter a name: ")
    id = new_player.get_player(player)

    
    

    game_log = logger.Logger(id)
    logs = game_log.get_last_15_games()
    homeGames, awayGames, homeAvg, awayAvg = game_log.home_away_differential(logs)

    
    
   

    





if __name__ == "__main__":
    main()

