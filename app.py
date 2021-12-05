from flask import Flask, render_template, request, redirect
import requests
import json
from epicstore_api import EpicGamesStoreAPI
from datetime import datetime
from operator import itemgetter
import harperdb
#from harperDB import harperdb_request
 
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():

    games_list = []
    
    #Stores user search input in q
    q = request.args.get('query')
    if type(q) != str:
        q =""


    db = harperdb.HarperDB(url="https://database-latulod360.harperdbcloud.com", username="database_project", password="database_project")
    
    
    app.run(debug=True)
    database_games = db.sql("select * from video.videogame")
    
    for i in database_games:
        
        game_data_2 = {
            'title' : i['title'],
            'price' : i['price'],
            'initialprice' : i['initialprice'],
            'discount' : i['discount'],
            'store' : i['store'],
            'link' : i['link'],
            'thumbnail' : i['thumbnail']

        }
        games_list.append(game_data_2)


    games_list.sort(key=itemgetter("price"))
    #games_list = sorted(games_list, key = lambda i: i['price'])
    #Implements Search Functionality
    for i in games_list:
        i['price']=format(i['price'],".2f")
        i['initialprice']=format(i['initialprice'],".2f")

    if q:
        games_list = [games for games in games_list if q.lower() in games['title'].lower()]
        
    else:
        games_list
        
    return render_template('index1.html', games = games_list)
