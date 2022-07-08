import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player1 = Player('Ethan', 'rock')
        self.player2 = Player('Rachel', 'scissors')
        self.player3 = Player('Minnie', 'paper')

    # @unittest.skip('pass')
    def test_rock_beats_scissors(self):
        self.assertEqual("Ethan", self.game.play_game(self.player1, self.player2))

    # @unittest.skip('pass')
    def test_rock_loses_to_paper(self):
        self.assertEqual("Minnie", self.game.play_game(self.player1, self.player3))

    # @unittest.skip('pass')
    def test_rock_draws_rock(self):
        self.assertEqual(None, self.game.play_game(self.player1, self.player1))

    def test_scissors_beats_paper(self):
        self.assertEqual("Rachel", self.game.play_game(self.player2, self.player3))
    
    def test_scissors_loses_to_rock(self):
        self.assertEqual("Ethan", self.game.play_game(self.player2, self.player1))
    
    def test_scissors_draws_scissors(self):
        self.assertEqual(None, self.game.play_game(self.player2, self.player2))

    def test_paper_beats_rock(self):
        self.assertEqual("Minnie", self.game.play_game(self.player3, self.player1))

    def test_paper_loses_to_scissors(self):
        self.assertEqual("Rachel", self.game.play_game(self.player3, self.player2))

    def test_paper_draws_paper(self):
        self.assertEqual(None, self.game.play_game(self.player3, self.player3))
        
