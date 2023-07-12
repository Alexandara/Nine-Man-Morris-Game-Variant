"""
MiniMax versions of the Morris Game

:author: Alexis Tudor
"""
from morris_game import MorrisGame, Result

class MiniMaxOpening(MorrisGame):
    """
    MiniMaxOpening imports Morris Game and calculates the best move based on
    a current board state and depth using MiniMax optimization with the
    in-class static estimation function. This is for opening boards.
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
        result = self.choose_move(self.board_state, depth)
        if debug:
            self.print_board(result.move)
        str_move = self.board_to_string(result.move)
        output_file = open(file2, "w")
        output_file.write(str_move)
        output_file.close()
        print("Board Position: " + str_move)
        print("Positions evaluated by static estimation: " + str(self.positions_evaluated))
        print("MINIMAX estimate: " + str(result.evaluation))

    def choose_move(self, curr_board, depth, max_player=True):
        """
        An override of the choose_move function for the MorrisGame that
        instead calculates the next move based on MiniMax at a certain depth.
        :param curr_board: board to start with
        :param depth: current depth
        :param max_player: whether we are the max_playerimizing player or not
        :return: best move and it's evaluation
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
                result = self.choose_move(self.flip_board(move), depth-1, not max_player)
                if result.evaluation > num.evaluation:
                    num = Result(result.evaluation, move)
            return num
        else:
            num = Result(10000,[])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max_player)
                if result.evaluation < num.evaluation:
                    num = Result(result.evaluation, move)
            return num

class MiniMaxGame(MorrisGame):
    """
    MiniMaxGame imports Morris Game and calculates the best move based on
    a current board state and depth using MiniMax optimization with the
    in-class static estimation function. This is for midgame/endgame boards.
    """
    def __init__(self, file1, file2, depth, debug=False):
        file = open(file1, "r")
        start = file.read()
        file.close()
        self.positions_evaluated = 0
        self.player_color = "W"
        self.board_state = []
        self.game_stage = "me"  # midgame endgame stage
        self.turns = -10000
        for i in range(21):
            self.board_state.append(start[i:i + 1])
        if debug:
            self.print_board(self.board_state)
        result = self.choose_move(self.board_state, depth)
        if debug:
            self.print_board(result.move)
        str_move = self.board_to_string(result.move)
        output_file = open(file2, "w")
        output_file.write(str_move)
        output_file.close()
        print("Board Position: " + str_move)
        print("Positions evaluated by static estimation: " + str(self.positions_evaluated))
        print("MINIMAX estimate: " + str(result.evaluation))

    def choose_move(self, curr_board, depth, max_player=True):
        """
        An override of the choose_move function for the MorrisGame that
        instead calculates the next move based on MiniMax at a certain depth.
        :param curr_board: board to start with
        :param depth: current depth
        :param max_player: whether we are the max_playerimizing player or not
        :return: best move and it's evaluation
        """
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
        if max_player == 1:
            num = Result(-10000, [])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max_player)
                if result.evaluation > num.evaluation:
                    num = Result(result.evaluation, move)
            return num
        else:
            num = Result(10000, [])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max_player)
                if result.evaluation < num.evaluation:
                    num = Result(result.evaluation, move)
            return num

class MiniMaxOpeningBlack(MiniMaxOpening):
    """
    MiniMaxOpeningBlack imports Morris Game and calculates the best move based
    on a current board state and depth using MiniMax optimization with the
    in-class static estimation function. This is for opening boards.
    This class is for the machine playing black.
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
        self.board_state = self.flip_board(self.board_state)
        if debug:
            self.print_board(self.board_state)
        result = self.choose_move(self.board_state, depth)
        if debug:
            self.print_board(result.move)
        result.move = self.flip_board(result.move)
        str_move = self.board_to_string(result.move)
        output_file = open(file2, "w")
        output_file.write(str_move)
        output_file.close()
        print("Board Position: " + str_move)
        print("Positions evaluated by static estimation: " + str(self.positions_evaluated))
        print("MINIMAX estimate: " + str(result.evaluation))

class MiniMaxGameBlack(MiniMaxGame):
    """
    MiniMaxGameBlack imports Morris Game and calculates the best move based on
    a current board state and depth using MiniMax optimization with the
    in-class static estimation function. This is for midgame/endgame boards.
    This class is for the machine playing black.
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
        self.board_state = self.flip_board(self.board_state)
        if debug:
            self.print_board(self.board_state)
        result = self.choose_move(self.board_state, depth)
        if debug:
            self.print_board(result.move)
        result.move = self.flip_board(result.move)
        str_move = self.board_to_string(result.move)
        output_file = open(file2, "w")
        output_file.write(str_move)
        output_file.close()
        print("Board Position: " + str_move)
        print("Positions evaluated by static estimation: " + str(self.positions_evaluated))
        print("MINIMAX estimate: " + str(result.evaluation))

class MiniMaxOpeningImproved(MorrisGame):
    """
    MiniMaxOpeningImproved imports Morris Game and calculates the best move
    on a current board state and depth using MiniMax optimization with the
    modified static estimation function. This is for opening boards.
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
        result = self.choose_move(self.board_state, depth)
        if debug:
            self.print_board(result.move)
        str_move = self.board_to_string(result.move)
        output_file = open(file2, "w")
        output_file.write(str_move)
        output_file.close()
        print("Board Position: " + str_move)
        print("Positions evaluated by static estimation: " + str(self.positions_evaluated))
        print("MINIMAX estimate: " + str(result.evaluation))

    def choose_move(self, curr_board, depth, max_player=True):
        """
        An override of the choose_move function for the MorrisGame that
        instead calculates the next move based on MiniMax at a certain depth.
        :param curr_board: board to start with
        :param depth: current depth
        :param max_player: whether we are the max_playerimizing player or not
        :return: best move and it's evaluation
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
                result = self.choose_move(self.flip_board(move), depth-1, not max_player)
                if result.evaluation > num.evaluation:
                    num = Result(result.evaluation, move)
            return num
        else:
            num = Result(10000,[])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max_player)
                if result.evaluation < num.evaluation:
                    num = Result(result.evaluation, move)
            return num

    def static_estimation(self, curr_board):
        """
        An override of the base Morris Game static estimation learned in class.
        This static estimation takes milling into consideration.
        :param curr_board: board to evaluate
        :return: numerical evaluation of the board
        """
        num_white = self.count_piece("W", curr_board)
        num_black = self.count_piece("B", curr_board)
        add_num = 0
        for i in range(20):
            if self.close_mill(i, curr_board):
                if curr_board[i] == 'W':
                    add_num = 10
                elif curr_board[i] == "B":
                    add_num = -10
        if self.game_stage == "o":
            return num_white - num_black + add_num
        else:
            list_moves = self.generate_moves_midgame_endgame(curr_board)
            num_black_moves = len(list_moves)
            if num_black <= 2:
                return 10000
            elif num_white <= 2:
                return -10000
            elif num_black_moves == 0:
                return 10000
            else:
                return (1000 * (num_white - num_black) - num_black_moves) + (1000 * add_num)

class MiniMaxGameImproved(MorrisGame):
    """
    MiniMaxGameImproved imports Morris Game and calculates the best move
    on a current board state and depth using MiniMax optimization with the
    modified static estimation function. This is for midgame/endgame boards.
    """
    def __init__(self, file1, file2, depth, debug=False):
        file = open(file1, "r")
        start = file.read()
        file.close()
        self.positions_evaluated = 0
        self.player_color = "W"
        self.board_state = []
        self.game_stage = "me"  # midgame endgame stage
        self.turns = -10000
        for i in range(21):
            self.board_state.append(start[i:i + 1])
        if debug:
            self.print_board(self.board_state)
        result = self.choose_move(self.board_state, depth)
        if debug:
            self.print_board(result.move)
        str_move = self.board_to_string(result.move)
        output_file = open(file2, "w")
        output_file.write(str_move)
        output_file.close()
        print("Board Position: " + str_move)
        print("Positions evaluated by static estimation: " + str(self.positions_evaluated))
        print("MINIMAX estimate: " + str(result.evaluation))

    def choose_move(self, curr_board, depth, max_player=True):
        """
        An override of the choose_move function for the MorrisGame that
        instead calculates the next move based on MiniMax at a certain depth.
        :param curr_board: board to start with
        :param depth: current depth
        :param max_player: whether we are the max_playerimizing player or not
        :return: best move and it's evaluation
        """
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
        if max_player == 1:
            num = Result(-10000, [])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max_player)
                if result.evaluation > num.evaluation:
                    num = Result(result.evaluation, move)
            return num
        else:
            num = Result(10000, [])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max_player)
                if result.evaluation < num.evaluation:
                    num = Result(result.evaluation, move)
            return num

    def static_estimation(self, curr_board):
        """
        An override of the base Morris Game static estimation learned in class.
        This static estimation takes milling into consideration.
        :param curr_board: board to evaluate
        :return: numerical evaluation of the board
        """
        num_white = self.count_piece("W", curr_board)
        num_black = self.count_piece("B", curr_board)
        add_num = 0
        for i in range(20):
            if self.close_mill(i, curr_board):
                if curr_board[i] == 'W':
                    add_num = 10
                elif curr_board[i] == "B":
                    add_num = -10
        if self.game_stage == "o":
            return num_white - num_black + add_num
        else:
            list_moves = self.generate_moves_midgame_endgame(curr_board)
            num_black_moves = len(list_moves)
            if num_black <= 2:
                return 10000
            elif num_white <= 2:
                return -10000
            elif num_black_moves == 0:
                return 10000
            else:
                return (1000 * (num_white - num_black) - num_black_moves) + (1000 * add_num)

if __name__ == '__main__':
    # Opening Examples
    mmo = MiniMaxOpening("files/board_opening.txt", "files/board_opening_example1.txt", 3)
    mmme = MiniMaxGame("files/board_midgame_endgame.txt", "files/board_me_answer.txt", 3)
    mmob = MiniMaxOpeningBlack("files/board_opening.txt", "files/board_ob_answer.txt", 3)
    mmmeb = MiniMaxGameBlack("files/board_midgame_endgame.txt", "files/board_meb_answer.txt", 3)
    mmoi = MiniMaxOpeningImproved("files/board_opening.txt", "files/board_oi_answer.txt", 3)
    mmmei = MiniMaxGameImproved("files/board_midgame_endgame.txt", "files/board_mei_answer.txt", 3)
