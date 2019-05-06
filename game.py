import connect4
import agents
import timeit


TIME_LIMIT_MILLIS = 150.

class Game:
    def __init__(self):
        self.game = connect4.Connect4()
        self.player1 = agents.MinimaxPlayer()
        self.player2 = agents.MinimaxPlayer()
        self.active_player = self.game.player

    def print_board(self):
        print(self.game.state)
        print("Player {}'s turn".format(self.active_player))

    def move(self, time_limit=TIME_LIMIT_MILLIS):
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda: time_limit - (time_millis() - move_start)
        if self.active_player == 1:
            move = self.player1.search(self.game, time_left)
        elif self.active_player == -1:
            move = self.player2.search(self.game, time_left)
        move_end = time_left()

        if move_end < 0.:
            print('Timeout')
        else:
            print(move)
            self.game.move(move)
            self.active_player = self.game.player
            self.print_board()