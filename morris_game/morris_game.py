class MorrisGame:
    def __init__(self):
        self.playerColor = "null"
        while self.playerColor != "w" and self.playerColor != "b":
            print("Will you play white (w) or black (b)?")
            self.playerColor = input()
        if self.playerColor == "w":
            self.boardState = "xxxxxxxxxxxxxxxxxWxx"

    def print_board(self):
        dash = "-" * 3
        line_n = "|" + " " * 2
        n_line_n = " " + "|" + " "
        n_line = " " * 2 + "|"
        n = " " * 3
        # Line 6: a6-, -, -, d6, -, -, -g6
        print(self.boardState[17:18] + "-" * 2 +
              dash * 2 +
              "-" + self.boardState[18:19] + "-" +
              dash * 2 +
              "-" * 2 + self.boardState[19:])
        # Line 6-5: |n, n, n, |, n, n, n|
        print(line_n +
              n * 2 +
              n_line_n +
              n * 2 +
              n_line)
        # Line 5: |n, b5-, -, -d5-, -, -f5, n|
        print("|" + " " * 2 +
              " " + self.boardState[14:15] + "-" +
              dash +
              "-" + self.boardState[15:16] + "-" +
              dash +
              "-" + self.boardState[16:17] + " " +
              n_line)
        # Line 5-4: |n, n|n, n, n|n, n, n|n, n|n
        print(line_n +
              n_line_n +
              n +
              n_line_n +
              n +
              n_line_n +
              n_line)
        # Line 4: |n, n|n, c4-, -d4-, -e4, n|n, n|
        print(line_n +
              n_line_n +
              " " + self.boardState[11:12] + "-" +
              "-" + self.boardState[12:13] + "-" +
              "-" + self.boardState[13:14] + " " +
              n_line_n +
              n_line)