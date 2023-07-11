from morris_game import MorrisGame

class Result:
    def __init__(self, evaluation, move):
        self.evaluation = evaluation
        self.move = move

class MiniMaxOpening(MorrisGame):
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

    def choose_move(self, curr_board, depth, max=True):
        if depth == 0:
            self.positions_evaluated = self.positions_evaluated + 1
            if max:
                return Result(self.static_estimation(curr_board), curr_board)
            flipped_board = self.flip_board(curr_board)
            return Result(self.static_estimation(flipped_board), curr_board)
        moves = self.generate_moves_opening(curr_board)
        if len(moves) == 0:
            if max == 1:
                return Result(-10000, curr_board)
            return Result(10000, curr_board)
        if max == 1:
            num = Result(-10000,[])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth-1, not max)
                if result.evaluation > num.evaluation:
                    num = Result(result.evaluation, move)
            return num
        else:
            num = Result(10000,[])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max)
                if result.evaluation < num.evaluation:
                    num = Result(result.evaluation, move)
            return num

class MiniMaxMidgameEndgame(MorrisGame):
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

    def choose_move(self, curr_board, depth, max=True):
        if depth == 0:
            self.positions_evaluated = self.positions_evaluated + 1
            if max:
                return Result(self.static_estimation(curr_board), curr_board)
            flipped_board = self.flip_board(curr_board)
            return Result(self.static_estimation(flipped_board), curr_board)
        moves = self.generate_moves_midgame_endgame(curr_board)
        if len(moves) == 0:
            if max == 1:
                return Result(-10000, curr_board)
            return Result(10000, curr_board)
        if max == 1:
            num = Result(-10000, [])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max)
                if result.evaluation > num.evaluation:
                    num = Result(result.evaluation, move)
            return num
        else:
            num = Result(10000, [])
            for move in moves:
                result = self.choose_move(self.flip_board(move), depth - 1, not max)
                if result.evaluation < num.evaluation:
                    num = Result(result.evaluation, move)
            return num

class MiniMaxOpeningBlack(MiniMaxOpening):
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

class MiniMaxMidgameEndgameBlack(MiniMaxMidgameEndgame):
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

if __name__ == '__main__':
    mmo = MiniMaxOpening("files/board_opening.txt", "files/board_o_answer.txt", 3)
    mmme = MiniMaxMidgameEndgame("files/board_midgame_endgame.txt", "files/board_me_answer.txt", 3)
    mmob = MiniMaxOpeningBlack("files/board_opening.txt", "files/board_ob_answer.txt", 3)
    mmmeb = MiniMaxMidgameEndgameBlack("files/board_midgame_endgame.txt", "files/board_meb_answer.txt", 3)