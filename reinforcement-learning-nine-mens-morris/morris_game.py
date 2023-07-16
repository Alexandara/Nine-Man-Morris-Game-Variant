"""
Morris Game

:author: Alexis Tudor
"""
class Result:
    """
    Result objects store the results of static estimation (evaluation) on a
    given move (move).
    """
    def __init__(self, evaluation, move):
        self.evaluation = evaluation
        self.move = move

class MorrisGame:
    """
    Class that runs the game Nine Man's Morris for Summer 2023 UT Dallas
    Artificial Intelligence course.
    """
    def __init__(self):
        self.player_color = "x"
        self.board_state = []
        self.game_stage = "o" # Opening stage
        self.turns = 0
        for i in range(24):
            self.board_state.append('x')

    def play(self):
        """
        Function that plays the Morris Game with a human player.
        """
        while self.player_color not in ('W','B'):
            print("Will you play white (W) or black (B)?")
            self.player_color = input().upper()
        if self.player_color == 'W':
            self.player_turn()
        while self.turns < 60 and self.game_over() == 'x':
            if self.game_stage == "o":
                if self.player_color == 'B':
                    moves = self.generate_moves_opening(self.board_state.copy())
                    self.board_state = self.choose_move(moves.copy())
                else:
                    temp_board = self.flip_board(self.board_state.copy())
                    moves = self.generate_moves_opening(temp_board)
                    new_board = self.choose_move(moves.copy())
                    self.board_state = self.flip_board(new_board.copy())
            else:
                if self.player_color == 'B':
                    moves = self.generate_moves_midgame_endgame(self.board_state.copy())
                    self.board_state = self.choose_move(moves.copy())
                else:
                    temp_board = self.flip_board(self.board_state.copy())
                    moves = self.generate_moves_midgame_endgame(temp_board)
                    new_board = self.choose_move(moves.copy())
                    self.board_state = self.flip_board(new_board.copy())
            self.player_turn()
        print("Win for " + self.game_over())

    def player_turn(self):
        """
        Function to allow the human player to take a turn.
        """
        self.print_board(self.board_state)
        if self.game_stage == "o":
            print("Please enter the numerical designation " + \
              "(i.e. 0, 7, etc.) indicating the space you'd like to place a " + \
                  "piece. Enter \'h\' for help and board reference.")
            move = -1
            while move < 0 or move > 23:
                move = input().upper()
                if move == 'H':
                    self.print_reference()
                    move = -1
                else:
                    move = int(move)
            self.board_state[move] = self.player_color
            if self.close_mill(move, self.board_state):
                print("Please enter the numerical designation (" + \
                      "i.e. 0, 7, etc.) indicating the piece you'd like to" + \
                      " remove. Enter \'h\' for help and board reference.")
                move = -1
                while move < 0 or move > 23:
                    move = input().upper()
                    if move == 'H':
                        self.print_reference()
                        move = -1
                    else:
                        move = int(move)
                self.board_state[move] = 'x'
        else:
            print("Please enter the numerical designation " + \
                  "(i.e. 0, 7, etc.) indicating the piece you'd like to move")
            print("Enter \'h\' for help and board reference.")
            move = -1
            while move < 0 or move > 23:
                move = input().upper()
                if move == 'H':
                    self.print_reference()
                    move = -1
                else:
                    move = int(move)
            self.board_state[move] = 'x'
            print("Please enter the numerical designation " + \
                  "(i.e. 0, 7, etc.) indicating the place you'd like" + \
                  " to move to.")
            print("Enter \'h\' for help and board reference.")
            move = -1
            while move < 0 or move > 23:
                move = input().upper()
                if move == 'H':
                    self.print_reference()
                    move = -1
                else:
                    move = int(move)
            self.board_state[move] = self.player_color
            if self.close_mill(move, self.board_state):
                print("Please enter the numerical designation (" + \
                      "i.e. 0, 7, etc.) indicating the piece you'd like to" + \
                      " remove. Enter \'h\' for help and board reference.")
                move = -1
                while move < 0 or move > 23:
                    move = input().upper()
                    if move == 'H':
                        self.print_reference()
                        move = -1
                    else:
                        move = int(move)
                self.board_state[move] = 'x'
        self.turns = self.turns + 1
        if self.turns == 16:
            self.game_stage = "me"

    def choose_move(self, moves):
        """
        Basic function to choose a move for the computer to play.
        :param moves: list of possible moves.
        :return: chosen move
        """
        best = []
        for move in moves:
            best.append(self.static_estimation(move))
        ind = best.index(max(best))
        self.turns = self.turns + 1
        if self.turns == 16:
            self.game_stage = "me"
        return moves[ind]

    @staticmethod
    def print_board(curr_board):
        """
        Method that prints the current board state.
        """
        dash = "-" * 5
        line_n = "|" + " " * 4
        n_line_n = " " * 2 + "|" + " " * 2
        n_line = " " * 4 + "|"
        nnn = " " * 5
        # Line 6: a6-, -, -, d6, -, -, -g6
        print(curr_board[21] + "-" * 4 +
              dash * 2 +
              "-" * 2 + curr_board[22] + "-" * 2 +
              dash * 2 +
              "-" * 4 + curr_board[23])
        # Line 6-5: |n, n, n, |, n, n, n|
        print(line_n +
              nnn * 2 +
              n_line_n +
              nnn * 2 +
              n_line)
        # Line 5: |n, b5-, -, -d5-, -, -f5, n|
        print(line_n +
              " " * 2 + curr_board[18] + "-" * 2 +
              dash +
              "-" * 2 + curr_board[19] + "-" * 2 +
              dash +
              "-" * 2 + curr_board[20] + " " * 2 +
              n_line)
        # Line 5-4: |n, n|n, n, n|n, n, n|n, n|n
        print(line_n +
              n_line_n +
              nnn +
              n_line_n +
              nnn +
              n_line_n +
              n_line)
        # Line 4: |n, n|n, c4-, -d4-, -e4, n|n, n|
        print(line_n +
              n_line_n +
              " " * 2 + curr_board[15] + "-" * 2 +
              "-" * 2 + curr_board[16] + "-" * 2 +
              "-" * 2 + curr_board[17] + " " * 2 +
              n_line_n +
              n_line)
        # Line 4-3: |n, n|n, n|n, n, n|n, n|n, n|
        print(line_n +
              n_line_n * 2 +
              nnn +
              n_line_n * 2 +
              n_line)
        # Line 3: a3-, -b3-, -c3, n, e3-, -f3-, -g3
        print(curr_board[9] + "-" * 4 +
              "-" * 2 + curr_board[10] + "-" * 2 +
              "-" * 2 + curr_board[11] + " " * 2 +
              nnn +
              " " * 2 + curr_board[12] + "-" * 2 +
              "-" * 2 + curr_board[13] + "-" * 2 +
              "-" * 4 + curr_board[14])
        # Line 3-2: |n, n|n, n|n, n|n, n|n, n|n, n|
        print(line_n +
              n_line_n * 2 +
              nnn +
              n_line_n * 2 +
              n_line)
        # Line 2: |n, n|n, c2-, -d2-, -e2, n|n, n|
        print(line_n +
              n_line_n +
              " " * 2 + curr_board[6] + "-" * 2 +
              "-" * 2 + curr_board[7] + "-" * 2 +
              "-" * 2 + curr_board[8] + " " * 2 +
              n_line_n +
              n_line)
        # Line 2-1: |n, n|n, n, n|n, n, n|n, n|
        print(line_n +
              n_line_n +
              nnn +
              n_line_n +
              nnn +
              n_line_n +
              n_line)
        # Line 1: |n, b1-, -, -d1-, -, -f1, n|
        print(line_n +
              " " * 2 + curr_board[3] + "-" * 2 +
              dash +
              "-" * 2 + curr_board[4] + "-" * 2 +
              dash +
              "-" * 2 + curr_board[5] + " " * 2 +
              n_line)
        # Line 1-0: |n, n, n, n|n, n, n, n|
        print(line_n +
              nnn * 2 +
              n_line_n +
              nnn * 2 +
              n_line)
        # Line 0: a0-, -, -, -d0-, -, -, -g0
        print(curr_board[0] + "-" * 4 +
              dash * 2 +
              "-" * 2 + curr_board[1] + "-" * 2 +
              dash * 2 +
              "-" * 4 + curr_board[2])

    @staticmethod
    def flip_board(curr_board):
        """
        Helper method that flips white and black on the board.
        :param curr_board: board to flip
        :return: flipped board
        """
        new_board = curr_board.copy()
        for i in range (len(new_board)):
            if new_board[i] == 'W':
                new_board[i] = 'B'
            elif new_board[i] == 'B':
                new_board[i] = 'W'
        return new_board

    def generate_moves_opening(self, curr_board):
        """
        Returns a list of valid opening moves
        :return: list of valid opening moves
        """
        return self.generate_add(curr_board)

    def generate_moves_midgame_endgame(self, curr_board):
        """
        If the board has 3 white pieces Return the list produced by
        GenerateHopping applied to the board. Otherwise return the
        list produced by GenerateMove applied to the board.
        :param curr_board: current board state
        :return: list of possible moves
        """
        num_white = self.count_piece("W", curr_board)
        if num_white <= 3:
            return self.generate_hopping(curr_board)
        return self.generate_move(curr_board)

    def generate_add(self, curr_board):
        """
        This method produces a list of board positions possible in the opening
        stage wherein a piece can be placed anywhere there is not currently a
        piece.
        :return: a list L of board positions possible
        """
        L = []
        for i in range(len(curr_board)):
            if curr_board[i] == 'x':
                b_copy = curr_board.copy()
                b_copy[i] = 'W'
                if self.close_mill(i, b_copy):
                    L.extend(self.generate_remove(b_copy))
                else:
                    L.append(b_copy)
        return L

    def generate_hopping(self, curr_board):
        """
        Generate hopping generates moves for when white only has three pieces,
        in which case white can move to any available empty position.
        :return: a list L of board positions after hopping
        """
        L = []
        for a in range(len(curr_board)):
            if curr_board[a] == 'W':
                for b in range(len(curr_board)):
                    if curr_board[b] == 'x':
                        b_copy = curr_board.copy()
                        b_copy[a] = 'x'
                        b_copy[b] = 'W'
                        if self.close_mill(b, b_copy):
                            L.extend(self.generate_remove(b_copy))
                        else:
                            L.append(b_copy)
        return L

    def generate_move(self, curr_board):
        """
        Generate move creates a list of possible moves
        :return: a list L of board positions from moving a piece
        """
        L = []
        for location in range(len(curr_board)):
            if curr_board[location] == 'W':
                neighbors = self.get_neighbors(location)
                for neighbor in neighbors:
                    if curr_board[neighbor] == 'x':
                        b_copy = curr_board.copy()
                        b_copy[location] = 'x'
                        b_copy[neighbor] = 'W'
                        if self.close_mill(neighbor, b_copy):
                            L.extend(self.generate_remove(b_copy))
                        else:
                            L.append(b_copy)
        return L

    def generate_remove(self, curr_board):
        """
        Method generates a list of moves from removing one black piece.
        :return: positions are added to L by removing black pieces
        """
        L = []
        for location in range(len(curr_board)):
            if curr_board[location] == 'B':
                if not self.close_mill(location, curr_board):
                    b_copy = curr_board.copy()
                    b_copy[location] = 'x'
                    L.append(b_copy)
        if not L:
            L.append(curr_board)
        return L

    def get_neighbors(self, location):
        """
        Method returns a list of the locations of all neighbors of a space.
        :param location: location to check neighbors for
        :return: a list of locations of neighbors of the piece at location
        """
        if location == 0:
            return [1,9]
        elif location == 1:
            return [0,2,4]
        elif location == 2:
            return [1,14]
        elif location == 3:
            return [4,10]
        elif location == 4:
            return [1,3,5,7]
        elif location == 5:
            return [4,13]
        elif location == 6:
            return [7,11]
        elif location == 7:
            return [4,6,8]
        elif location == 8:
            return [7,12]
        elif location == 9:
            return [0,10,21]
        elif location == 10:
            return [3,9,11,18]
        elif location == 11:
            return [6,10,15]
        elif location == 12:
            return [8,13,17]
        elif location == 13:
            return [5,12,14,20]
        elif location == 14:
            return [2,13,23]
        elif location == 15:
            return [11,16]
        elif location == 16:
            return [15,17,19]
        elif location == 17:
            return [12,16]
        elif location == 18:
            return [10,19]
        elif location == 19:
            return [16,18,20,22]
        elif location == 20:
            return [13,19]
        elif location == 21:
            return [9,22]
        elif location == 22:
            return [19,21,23]
        elif location == 23:
            return [14,22]
        else:
            return []

    def close_mill(self, location, curr_board):
        """
        Close mill calculates whether a board has a closed mill or not
        :param location: Most recent move
        :param curr_board: Current board being looked at
        :return: True is the location closes a mill, false if not
        """
        c = curr_board[location]
        if location == 0:
            if curr_board[9] == c and curr_board[21] == c or\
                    curr_board[1] == c and curr_board[2] == c:
                return True
            else:
                return False
        elif location == 1:
            if curr_board[0] == c and curr_board[2] == c or \
                    curr_board[4] == c and curr_board[7] == c:
                return True
            else:
                return False
        elif location == 2:
            if curr_board[0] == c and curr_board[1] == c or \
                    curr_board[14] == c and curr_board[23] == c:
                return True
            else:
                return False
        elif location == 3:
            if curr_board[4] == c and curr_board[5] == c or \
                    curr_board[10] == c and curr_board[18] == c:
                return True
            else:
                return False
        elif location == 4:
            if curr_board[3] == c and curr_board[5] == c or \
                    curr_board[1] == c and curr_board[7] == c:
                return True
            else:
                return False
        elif location == 5:
            if curr_board[3] == c and curr_board[4] == c or \
                    curr_board[13] == c and curr_board[20] == c:
                return True
            else:
                return False
        elif location == 6:
            if curr_board[7] == c and curr_board[8] == c\
                    or curr_board[11] == c and curr_board[15] == c:
                return True
            else:
                return False
        elif location == 7:
            if curr_board[6] == c and curr_board[8] == c \
                    or curr_board[1] == c and curr_board[4] == c:
                return True
            else:
                return False
        elif location == 8:
            if curr_board[6] == c and curr_board[7] == c \
                    or curr_board[12] == c and curr_board[17] == c:
                return True
            else:
                return False
        elif location == 9:
            if curr_board[0] == c and curr_board[21] == c \
                    or curr_board[10] == c and curr_board[11] == c:
                return True
            else:
                return False
        elif location == 10:
            if curr_board[9] == c and curr_board[11] == c \
                    or curr_board[3] == c and curr_board[18] == c:
                return True
            else:
                return False
        elif location == 11:
            if curr_board[6] == c and curr_board[15] == c \
                    or curr_board[9] == c and curr_board[10] == c:
                return True
            else:
                return False
        elif location == 12:
            if curr_board[8] == c and curr_board[17] == c \
                    or curr_board[13] == c and curr_board[14] == c:
                return True
            else:
                return False
        elif location == 13:
            if curr_board[12] == c and curr_board[14] == c \
                    or curr_board[5] == c and curr_board[20] == c:
                return True
            else:
                return False
        elif location == 14:
            if curr_board[12] == c and curr_board[13] == c \
                    or curr_board[2] == c and curr_board[23] == c:
                return True
            else:
                return False
        elif location == 15:
            if curr_board[6] == c and curr_board[11] == c \
                    or curr_board[16] == c and curr_board[17] == c:
                return True
            else:
                return False
        elif location == 16:
            if curr_board[15] == c and curr_board[17] == c \
                    or curr_board[19] == c and curr_board[22] == c:
                return True
            else:
                return False
        elif location == 17:
            if curr_board[15] == c and curr_board[16] == c \
                    or curr_board[8] == c and curr_board[12] == c:
                return True
            else:
                return False
        elif location == 18:
            if curr_board[3] == c and curr_board[10] == c \
                    or curr_board[19] == c and curr_board[20] == c:
                return True
            else:
                return False
        elif location == 19:
            if curr_board[18] == c and curr_board[20] == c \
                    or curr_board[16] == c and curr_board[22] == c:
                return True
            else:
                return False
        elif location == 20:
            if curr_board[19] == c and curr_board[18] == c \
                    or curr_board[13] == c and curr_board[5] == c:
                return True
            else:
                return False
        elif location == 21:
            if curr_board[22] == c and curr_board[23] == c \
                    or curr_board[9] == c and curr_board[0] == c:
                return True
            else:
                return False
        elif location == 22:
            if curr_board[21] == c and curr_board[23] == c \
                    or curr_board[16] == c and curr_board[19] == c:
                return True
            else:
                return False
        elif location == 23:
            if curr_board[21] == c and curr_board[22] == c \
                    or curr_board[14] == c and curr_board[2] == c:
                return True
            else:
                return False
        else:
            return False

    def game_over(self):
        """
        Method that checks if someone has won yet.
        :return: W if white won, B if black won, x if no winner yet.
        """
        if self.game_stage == "o":
            return "x"
        curr_estimate = self.static_estimation(self.board_state)
        if curr_estimate == 10000:
            return "W"
        elif curr_estimate == -10000:
            return "B"
        else:
            return "x"

    def static_estimation(self, curr_board):
        """
        Base in-class static estimation function.
        :param curr_board: board to estimate
        :return: numerical estimate of board
        """
        num_white = self.count_piece("W", curr_board)
        num_black = self.count_piece("B", curr_board)
        if self.game_stage == "o":
            return num_white - num_black
        else:
            list_moves = self.generate_moves_midgame_endgame(curr_board)
            num_black_moves = len(list_moves)
            if num_black <= 2:
                return 10000
            if num_white <= 2:
                return -10000
            if num_black_moves == 0:
                return 10000
            return 1000 * (num_white - num_black) - num_black_moves

    @staticmethod
    def count_piece(piece_color, curr_board):
        """
        Counts how many pieces of a certain color are on the board
        :param piece_color: which color to count
        :param curr_board: board to count on
        :return: count of pieces
        """
        num = 0
        for piece in curr_board:
            if piece == piece_color:
                num = num + 1
        return num

    @staticmethod
    def print_reference():
        """
        A helpful reference guide to help players know which number corresponds
        to which space.
        """
        print("21-a6 ----- ----- 22-d6 ----- ----- 23-g6")
        print("----- 18-b5 ----- 19-d5 ----- 20-f5 -----")
        print("----- ----- 15-c4 16-d4 17-e4 ----- -----")
        print("09-a3 10-b3 11-c3 ----- 12-e3 13-f3 14-g3")
        print("----- ----- 06-c2 07-d2 08-e2 ----- -----")
        print("----- 03-b1 ----- 04-d1 ----- 05-f1 -----")
        print("00-a0 ----- ----- 01-d0 ----- ----- 02-g0\n")
        print("To move, first indicate the numerical designation (i.e. 0" +
              " for a0, 11 for g3, etc.) of the piece you want to move, " +
              "\nthen indicate the number or space code for the place you " +
              "want to move the piece to.")

    @staticmethod
    def board_to_string(curr_board):
        """
        Converts a board list to a string.
        :param curr_board: board list
        :return: string board
        """
        result = ""
        for pos in curr_board:
            result = result + pos
        return result

    @staticmethod
    def string_to_board(board_string: str):
        """
        Converts a string to a board list.
        :param board_string: board string
        :return: list board
        """
        board = []
        for char in board_string:
            board.append(char)
        return board

if __name__ == '__main__':
    morris = MorrisGame()
    morris.print_board(morris.board_state)
    morris.print_reference()
    #morris.play()
