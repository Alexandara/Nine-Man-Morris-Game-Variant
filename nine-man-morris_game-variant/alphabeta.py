"""
Alpha Beta versions of the Morris Game

:author: Alexis Tudor
"""
from morris_game import MorrisGame, Result

class ABOpening(MorrisGame):
    """
    ABOpening calculates the next move in the MorrisGame using alpha beta
    pruning. This is for opening moves.
    """
    def __init__(self, file1, file2, depth, debug=False):
        file = open(file1, "r")
        start = file.read()
        file.close()
        self.positions_evaluated = 0
        self.player_color = "W"
        self.board_state = []
        self.game_stage = "o"  # Opening stage
        self.turns = -10000
        for i in range(21):
            self.board_state.append(start[i:i+1])
        if debug:
            self.print_board(self.board_state)
        result = self.choose_move(self.board_state, depth, Result(-10001, []), Result(10001, []))
        if debug:
            self.print_board(result.move)
        str_move = self.board_to_string(result.move)
        output_file = open(file2, "w")
        output_file.write(str_move)
        output_file.close()
        print("Board Position: " + str_move)
        print("Positions evaluated by static estimation: " + str(self.positions_evaluated))
        print("MINIMAX/Alpha-Beta estimate: " + str(result.evaluation))

    def choose_move(self, curr_board, depth, alpha, beta, max_player=True):
        """
        Choose move function for alpha beta pruning.
        :param curr_board: board to start with
        :param depth: depth to explore to
        :param alpha: Alpha value
        :param beta: Beta value
        :param max_player: whether we are currently the maximizing player
        :return: next move and its evaluation
        """
        if depth == 0:
            self.positions_evaluated = self.positions_evaluated + 1
            if max_player:
                return Result(self.static_estimation(curr_board), curr_board)
            flipped_board = self.flip_board(curr_board)
            return Result(self.static_estimation(flipped_board), curr_board)
        moves = self.generate_moves_opening(curr_board)
        if len(moves) == 0:
            if max_player == 1:
                return Result(-10000, curr_board)
            return Result(10000, curr_board)
        if max_player == 1:
            num = Result(-10000,[])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth-1,
                                          alpha, beta, max_player=not max_player)
                if result.evaluation > num.evaluation:
                    num = Result(result.evaluation, move)
                if result.evaluation > alpha.evaluation:
                    alpha = Result(result.evaluation, move)
                if beta.evaluation <= alpha.evaluation:
                    break
            return num
        else:
            num = Result(10000,[])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1,
                                          alpha, beta, max_player=not max_player)
                if result.evaluation < num.evaluation:
                    num = Result(result.evaluation, move)
                if result.evaluation < beta.evaluation:
                    beta = Result(result.evaluation, move)
                if beta.evaluation <= alpha.evaluation:
                    break
            return num

class ABGame(MorrisGame):
    """
    ABOpening calculates the next move in the MorrisGame using alpha beta
    pruning. This is for midgame/endgame moves.
    """
    def __init__(self, file1, file2, depth, debug=False):
        file = open(file1, "r")
        start = file.read()
        file.close()
        self.positions_evaluated = 0
        self.player_color = "W"
        self.board_state = []
        self.game_stage = "me"  # Opening stage
        self.turns = -10000
        for i in range(21):
            self.board_state.append(start[i:i+1])
        if debug:
            self.print_board(self.board_state)
        result = self.choose_move(self.board_state, depth, Result(-10001, []), Result(10001, []))
        if debug:
            self.print_board(result.move)
        str_move = self.board_to_string(result.move)
        output_file = open(file2, "w")
        output_file.write(str_move)
        output_file.close()
        print("Board Position: " + str_move)
        print("Positions evaluated by static estimation: " + str(self.positions_evaluated))
        print("MINIMAX/Alpha-Beta estimate: " + str(result.evaluation))

    def choose_move(self, curr_board, depth, alpha, beta, max_player=True):
        """
        Choose move function for alpha beta pruning.
        :param curr_board: board to start with
        :param depth: depth to explore to
        :param alpha: Alpha value
        :param beta: Beta value
        :param max_player: whether we are currently the maximizing player
        :return: next move and its evaluation
        """
        # Base Cases
        if depth == 0:
            self.positions_evaluated = self.positions_evaluated + 1
            if max_player:
                return Result(self.static_estimation(curr_board), curr_board)
            flipped_board = self.flip_board(curr_board)
            return Result(self.static_estimation(flipped_board), curr_board)
        moves = self.generate_moves_midgame_endgame(curr_board)
        if len(moves) == 0:
            if max_player == 1:
                return Result(-10000, curr_board)
            return Result(10000, curr_board)
        # If maximizing player
        if max_player == 1:
            num = Result(-10000,[])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth-1,
                                          alpha, beta, max_player=not max_player)
                if result.evaluation > num.evaluation:
                    num = Result(result.evaluation, move)
                if result.evaluation > alpha.evaluation:
                    alpha = Result(result.evaluation, move)
                if beta.evaluation <= alpha.evaluation:
                    break
            return num
        # Else if minimizing player
        num = Result(10000,[])
        for move in moves:
            result = self.choose_move(self.flip_board(move), depth - 1,
                                      alpha, beta, max_player=not max_player)
            if result.evaluation < num.evaluation:
                num = Result(result.evaluation, move)
            if result.evaluation < beta.evaluation:
                beta = Result(result.evaluation, move)
            if beta.evaluation <= alpha.evaluation:
                break
        return num

if __name__ == '__main__':
    print("Alpha-Beta Pruning Examples")
    # Opening Examples
    print("Opening Examples")
    ABOpening("files/board_opening1.txt", "files/board_opening1_ABOpening_D3.txt", 3)
    ABOpening("files/board_opening2.txt", "files/board_opening2_ABOpening_D3.txt", 3)
    ABOpening("files/board_opening3.txt", "files/board_opening3_ABOpening_D3.txt", 3)
    ABOpening("files/board_opening3.txt", "files/board_opening3_ABOpening_D3.txt", 3)
    # Game Examples
    print("Game Examples")
    ABGame("files/board_midgame_endgame1.txt", "files/board_midgame_endgame1_ABGame_D3.txt", 3)
    ABGame("files/board_midgame_endgame2.txt", "files/board_midgame_endgame2_ABGame_D3.txt", 3)
    ABGame("files/board_midgame_endgame3.txt", "files/board_midgame_endgame3_ABGame_D3.txt", 3)
