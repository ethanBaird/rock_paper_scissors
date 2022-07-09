from flask import render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/RPS')
def index():
    return render_template('index.html')

@app.route('/RPS/<p1_choice>/<p2_choice>')
def victor(p1_choice, p2_choice):
    rps = Game()
    p1 = Player('Player 1', p1_choice)
    p2 = Player('Player 2', p2_choice)
    winner = rps.play_game(p1, p2)
    return render_template('victor.html', winner=winner)