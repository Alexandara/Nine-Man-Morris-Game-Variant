"""
Morris Game

:author: Alexis Tudor
"""
class MorrisGame:
    """
    Class that runs the game Nine Man's Morris for Summer 2023 UT Dallas
    Artificial Intelligence course.
    """
    def __init__(self):
        self.player_color = "w" # TODO: fix this
        self.board_state = []
        for i in range(21):
            self.board_state.append('x')
        while self.player_color not in ('w','b'):
            print("Will you play white (w) or black (b)?")
            # self.player_color = input()

    def print_board(self):
        """
        Method that prints the current board state.
        """
        dash = "-" * 5
        line_n = "|" + " " * 4
        n_line_n = " " * 2 + "|" + " " * 2
        n_line = " " * 4 + "|"
        nnn = " " * 5
        # Line 6: a6-, -, -, d6, -, -, -g6
        print(self.board_state[18] + "-" * 4 +
              dash * 2 +
              "-" * 2 + self.board_state[19] + "-" * 2 +
              dash * 2 +
              "-" * 4 + self.board_state[20])
        # Line 6-5: |n, n, n, |, n, n, n|
        print(line_n +
              nnn * 2 +
              n_line_n +
              nnn * 2 +
              n_line)
        # Line 5: |n, b5-, -, -d5-, -, -f5, n|
        print(line_n +
              " " * 2 + self.board_state[15] + "-" * 2 +
              dash +
              "-" * 2 + self.board_state[16] + "-" * 2 +
              dash +
              "-" * 2 + self.board_state[17] + " " * 2 +
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
              " " * 2 + self.board_state[12] + "-" * 2 +
              "-" * 2 + self.board_state[13] + "-" * 2 +
              "-" * 2 + self.board_state[14] + " " * 2 +
              n_line_n +
              n_line)
        # Line 4-3: |n, n|n, n|n, n, n|n, n|n, n|
        print(line_n +
              n_line_n * 2 +
              nnn +
              n_line_n * 2 +
              n_line)
        # Line 3: a3-, -b3-, -c3, n, e3-, -f3-, -g3
        print(self.board_state[6] + "-" * 4 +
              "-" * 2 + self.board_state[7] + "-" * 2 +
              "-" * 2 + self.board_state[8] + " " * 2 +
              nnn +
              " " * 2 + self.board_state[9] + "-" * 2 +
              "-" * 2 + self.board_state[10] + "-" * 2 +
              "-" * 4 + self.board_state[11])
        # Line 3-2: |n, n|n, n|n, n, n|n, n|n, n|
        print(line_n +
              n_line_n * 2 +
              nnn +
              n_line_n * 2 +
              n_line)
        # Line 2: |n, n|n, c2-, -, -e2, n|n, n|
        print(line_n +
              n_line_n +
              " " * 2 + self.board_state[4] + "-" * 2 +
              dash +
              "-" * 2 + self.board_state[5] + " " * 2 +
              n_line_n +
              n_line)
        # Line 2-1: |n, n|n, n, n, n, n|n, n|
        print(line_n +
              n_line_n +
              nnn * 3 +
              n_line_n +
              n_line)
        # Line 1: |n, b1-, -, -, -, -f1, n|
        print(line_n +
              " " * 2 + self.board_state[2] + "-" * 2 +
              dash * 3 +
              "-" * 2 + self.board_state[3] + " " * 2 +
              n_line)
        # Line 1-0: |n, n, n, n, n, n, n|
        print(line_n +
              nnn * 5 +
              n_line)
        # Line 0: a0-, -, -, -, -, -, -g0
        print(self.board_state[0] + "-" * 4 +
              dash * 5 +
              "-" * 4 + self.board_state[1])

    def generate_add(self):
        """
        This method produces a list of board positions possible in the opening
        stage wherein a piece can be placed anywhere there is not currently a
        piece.
        :return: a list L of board positions possible
        """
        L = []
        for i in range(len(self.board_state)):
            if self.board_state[i] == 'x':
                b_copy = self.board_state
                b_copy[i] = 'W'
                if self.close_mill(i, b_copy):
                    L.extend(self.generate_remove(b_copy))
                else:
                    L.append(b_copy)
        return L

    def generate_hopping(self):
        """
        Generate hopping generates moves for when white only has three pieces,
        in which case white can move to any available empty position.
        :return: a list L of board positions after hopping
        """
        L = []
        for a in range(len(self.board_state)):
            if self.board_state[a] == 'W':
                for b in range(len(self.board_state)):
                    if self.board_state[b] == 'x':
                        b_copy = self.board_state
                        b_copy[a] = 'x'
                        b_copy[b] = 'W'
                        if self.close_mill(b, b_copy):
                            L.extend(self.generate_remove(b_copy))
                        else:
                            L.append(b_copy)
        return L

    def generate_move(self):
        """
        Generate move creates a list of possible moves
        :return: a list L of board positions from moving a piece
        """
        L = []
        for location in range(len(self.board_state)):
            if self.board_state[location] == 'W':
                neighbors = self.get_neighbors(location)
                for neighbor in neighbors:
                    if self.board_state[neighbor] == 'x':
                        b_copy = self.board_state
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
                    b_copy = curr_board
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
            return [1,6]
        elif location == 1:
            return [0,11]
        elif location == 2:
            return [3,7]
        elif location == 3:
            return [2,10]
        elif location == 4:
            return [5,8]
        elif location == 5:
            return [4,9]
        elif location == 6:
            return [0,7,18]
        elif location == 7:
            return [2,6,8,15]
        elif location == 8:
            return [4,7,12]
        elif location == 9:
            return [5,10,14]
        elif location == 10:
            return [3,9,11,17]
        elif location == 11:
            return [1,10,20]
        elif location == 12:
            return [8,13]
        elif location == 13:
            return [12,14,16]
        elif location == 14:
            return [9,13]
        elif location == 15:
            return [7,16]
        elif location == 16:
            return [13,15,17,19]
        elif location == 17:
            return [10,16]
        elif location == 18:
            return [6,19]
        elif location == 19:
            return [16,18,20]
        elif location == 20:
            return [11,19]
        else:
            return []

    def close_mill(self, location, curr_board):
        """
        closeMill
        Input: a location j in the array representing the board and the board b
        Output: true if the move to j closes a mill
            C = b[j]; C must be either W or B. Cannot be x.
            switch(j) {
                case j==0 (a0) : return true if
                    (b[6]==C and b[18]==C)
                    else return false
                case j==6 (a3) : return true if
                    (b[0]==C and b[18]==C)
                    or (b[7]==C and b[8]==C)
                    else return false
                etc.
            }
        :param location:
        :param curr_board:
        :return:
        """
        c = curr_board[location]
        if location == 0:
            if curr_board[6] == c and curr_board[3] == c:
                return True
            else:
                return False
        elif location == 1:
            if curr_board[11] == c and curr_board[20] == c:
                return True
            else:
                return False
        elif location == 2:
            if curr_board[7] == c and curr_board[15] == c:
                return True
            else:
                return False
        elif location == 3:
            if curr_board[10] == c and curr_board[17] == c:
                return True
            else:
                return False
        elif location == 4:
            if curr_board[8] == c and curr_board[12] == c:
                return True
            else:
                return False
        elif location == 5:
            if curr_board[9] == c and curr_board[14] == c:
                return True
            else:
                return False
        elif location == 6:
            if curr_board[0] == c and curr_board[18] == c\
                    or curr_board[7] == c and curr_board[8] == c:
                return True
            else:
                return False
        elif location == 7:
            if curr_board[6] == c and curr_board[8] == c \
                    or curr_board[15] == c and curr_board[2] == c:
                return True
            else:
                return False
        elif location == 8:
            if curr_board[6] == c and curr_board[7] == c \
                    or curr_board[4] == c and curr_board[12] == c:
                return True
            else:
                return False
        elif location == 9:
            if curr_board[5] == c and curr_board[14] == c \
                    or curr_board[10] == c and curr_board[11] == c:
                return True
            else:
                return False
        elif location == 10:
            if curr_board[9] == c and curr_board[11] == c \
                    or curr_board[17] == c and curr_board[3] == c:
                return True
            else:
                return False
        elif location == 11:
            return [1,10,20]
        elif location == 12:
            return [8,13]
        elif location == 13:
            return [12,14,16]
        elif location == 14:
            return [9,13]
        elif location == 15:
            return [7,16]
        elif location == 16:
            return [13,15,17,19]
        elif location == 17:
            return [10,16]
        elif location == 18:
            return [6,19]
        elif location == 19:
            return [16,18,20]
        elif location == 20:
            return [11,19]
        else:
            return False

    @staticmethod
    def print_reference():
        print("18-a6 ----- ----- 19-d6 ----- ----- 20-g6")
        print("----- 15-b5 ----- 16-d5 ----- 17-f5 -----")
        print("----- ----- 12-c4 13-d4 14-e4 ----- -----")
        print("06-a3 07-b3 08-c3 ----- 09-e3 10-f3 11-g3")
        print("----- ----- 04-c2 ----- 05-e2 ----- -----")
        print("----- 02-b1 ----- ----- ----- 03-f1 -----")
        print("00-a0 ----- ----- ----- ----- ----- 01-g0\n")
        print("To move, first indicate the number or space code (i.e. a2," +
              " b4, etc.) of the piece you want to move, then indicate the " +
              "number or space code for the place you want to move the " +
              "piece to.")

if __name__ == '__main__':
    morris = MorrisGame()
    morris.generate_add()
