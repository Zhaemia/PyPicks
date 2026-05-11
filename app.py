from flask import Flask, jsonify
import players
import logger
import predictionModel
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('/index.html')

@app.route('/player/<search_player>')
def getPlayer(search_player):
    player = players.Player()
    player = player.search_players(search_player)
    return jsonify(player)

    
    
@app.route('/logs/<Player>')
def showPlayerStats(Player):
    log = logger.Logger(Player)
    df = log.get_last_15_games()
    json_df = df.to_json(orient='records')
    return jsonify(json_df)

@app.route('/prediction/<id>/<cat>/<statLine>')
def getPrediction(id, cat, statLine):
    logs = logger.Logger(id)
    copyLogs = logs.get_last_15_games()
    p = predictionModel.PredictionModel(copyLogs, cat, statLine)
    return p.hitRate()
    
