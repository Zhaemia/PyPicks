from nba_api.stats.static import players
import statGrabber
class Player:      
    def get_player(self, name):
        
        #Get Nba player
        player = players.find_players_by_full_name(name)

        #Check if that player exsist return -1 for now if not.
        if not player:
            print("Player not found")
            return -1

        
        #Enumerate through our player obe
        for i, x in enumerate(player, 1):
            print(i, x['full_name'])

        while True:
            try:
                selection = int(input("select a player from the list: "))
            
            except:
                print("Input must be an integer")

            if selection > len(player) or selection <= 0:
                print("Please make a valid selection")
                
            else:
                break
        
        id = player[selection - 1]['id']
        return id
        
        
            

        