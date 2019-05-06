import random
from heuristic import Heuristic

class SearchTimeout(Exception):
    """Subclass base exception for code clarity."""
    pass

class MinimaxPlayer:
    def __init__(self, search_depth=3, score_cls=Heuristic(), timeout=10.):
        '''
        Game-playing agent that chooses a move using minimax search. 
        You must finish and test this player to make sure it properly uses
        minimax to return a good move before the search time limit expires.
        Params
        ----------
        search_depth : int (optional)
            A strictly positive integer (i.e., 1, 2, 3,...) for the number of
            layers in the game tree to explore for fixed-depth search. (i.e., a
            depth of one (1) would only explore the immediate sucessors of the
            current state.)
        score_fn : callable (optional)
            A function to use for heuristic evaluation of game states.
        timeout : float (optional)
            Time remaining (in milliseconds) when search is aborted. Should be a
            positive value large enough to allow the function to return before the
            timer expires.
        '''

        self.search_depth = search_depth
        self.score = score_cls.get_score
        self.TIMER_THRESHOLD = timeout

    def search(self, game, time_left):
        '''
        Search for the best move from the available legal moves and return a
        result before the time limit expires.
        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.
        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.
        Returns
        -------
        int
            Board row corresponding to a legal move; may return
            -1 if there are no available legal moves.
        '''


        self.time_left = time_left
        best_move = -1

        try:
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            print('timeout')
            pass

        return best_move

    def minimax(self, game, depth):
        '''
        Implement minimax search algorithm as described in the lectures.
        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md
        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************
            Parameters
            ----------
            game : `connect4.Connect4`
                An instance of `connect4.Connect4` encoding the current state of the game.
            depth : int
                Depth is an integer representing the maximum number of plies to
                search in the game tree before aborting
            Returns
             -------
            int
                The board row of the best move found in the current search;
                -1 if there no legal move is found
            Notes
            -----
            (1) You MUST use the `self.score()` method for board evaluation
                to participate in the tournament; you cannot call any other evaluation
                function directly.
            (2) If you use any helper functions (e.g., as shown in the AIMA pseudocode) 
                then you must copy the timer check into the top of each helper function 
                or else your agent will timeout while playing.
        '''

        '''
        TODO
        ----
        initialize a best_move variable to -1
        initialize a depth variable to 1
        while there is time left do a search at the current depth and increase depth by 1
        when time runs out, return the best move found
        '''

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        return self.minimax_search(game, depth)

    def terminal_state(self, game):
        '''
        Checks if the game has ended
        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.
        '''

        return not game.available_moves

    def min_value(self, game, depth):
        '''
        Finds the lowest utility among all the posible actions from the given board
        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        Returns
        -------
        float
            The lowest utility value found among all the actions for the given board state.
        '''

        '''
        TODO
        ----
        add an alpha parameter.
        add a beta parameter.
        add alpha and beta to the max_value call
        for each action if util <= alpha return util
        for each action update beta with the min between beta and util 
        '''

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return(self.score(game))

        if self.terminal_state(game):
            return(self.score(game))
        
        util = float('inf')
        actions = random.sample(game.available_moves, len(game.available_moves))
        for action in actions:
            util = min(util, self.max_value(game.sim_move(action), depth-1))
        return util

    def max_value(self, game, depth):
        '''
        Finds the highest utility among all the posible actions from the given board
        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        Returns
        -------
        float
            The highest utility value found among all the actions for the given board state.
        '''

        '''
        TODO
        ----
        add an alpha parameter.
        add a beta parameter.
        add alpha and beta to the min_value call
        for each action if util >= beta return util
        for each action update alpha with the max between alpha and util 
        '''


        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return(self.score(game))

        if self.terminal_state(game):
            return(self.score(game))

        util = float('-inf')
        actions = random.sample(game.available_moves, len(game.available_moves))
        for action in actions:
            util = max(util, self.min_value(game.sim_move(action), depth-1))
        return util

    def minimax_search(self, game, depth):
        '''
        Finds the best action among all the posible actions from the given board
        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        Returns
        -------
        int
            Board row corresponding to a legal move.
        '''

        '''
        TODO
        ----
        add an alpha parameter.
        add a beta parameter.
        add alpha and beta to the min_value call
        get a randomized list of available actions
        initialize a best_score and best move variables
        initialize a util variable to keep track of the value returned by min_value
        for each action if util > best_score update best_score and best_move
        for each action update alpha with the max between alpha and util 
        '''

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        return max(random.sample(game.available_moves, len(game.available_moves)),
                    key=lambda m: self.min_value(game.sim_move(m), depth-1))