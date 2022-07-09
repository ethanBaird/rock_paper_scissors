import random

from flask import render_template, request, redirect
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<p1_choice>/<p2_choice>')
def victor(p1_choice, p2_choice):
    rps = Game()
    p1 = Player('Player 1', p1_choice)
    p2 = Player('Player 2', p2_choice)
    winner = rps.play_game(p1, p2)
    return render_template('victor.html', winner=winner)

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play', methods=['POST'])
def vs_comp():
    rps = Game()
    player = Player(request.form['name'], request.form['choice'])
    computer = Player('The Computer', random.choice(['rock', 'paper', 'scissors']))
    winner = rps.play_game(player, computer)
    return render_template('victor.html', winner=winner)