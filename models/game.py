from secrets import choice


class Game:

    def __init__(self):
        pass

    def play_game(self, player_1, player_2):
        if player_1.choice == 'rock':
            player_1.choice = 1
            if player_2.choice == 'scissors':
                player_2.choice = 0
            elif player_2.choice == 'paper':
                player_2.choice = 2
            else:
                player_2.choice = 1
        if player_1.choice == 'scissors':
            player_1.choice = 1
            if player_2.choice == 'paper':
                player_2.choice = 0
            elif player_2.choice == 'rock':
                player_2.choice = 2
            else:
                player_2.choice = 1
        # breakpoint()
        if player_1.choice == 'paper':
            player_1.choice = 1
            if player_2.choice == 'rock':
                player_2.choice = 0
            elif player_2.choice == 'scissors':
                player_2.choice = 2
            else:
                player_2.choice = 1
        # breakpoint()
        if player_1.choice > player_2.choice:
            return player_1.name
        elif player_2.choice > player_1.choice:
            return player_2.name
        else:
            return None


        

        