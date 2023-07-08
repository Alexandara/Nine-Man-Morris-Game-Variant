from morris_game import MorrisGame

class MiniMaxOpening(MorrisGame):
    def __init__(self, file1, file2, depth):
        file = open(file1, "r")
        start = file.read()
        file.close()
        self.positions_evaluated = 0
        self.player_color = "x"
        self.board_state = []
        self.game_stage = "o"  # Opening stage
        self.turns = -10000
        for i in range(21):
            self.board_state.append(start[i:i+1])
        estimate, move = self.choose_move(self.board_state, depth)

    def choose_move(self, curr_board, depth):
        if depth == 0:
            return 0


if __name__ == '__main__':
    mmo = MiniMaxOpening("files/board1.txt", "files/board2.txt", 3)