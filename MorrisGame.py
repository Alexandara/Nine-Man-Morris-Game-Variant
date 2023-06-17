class MorrisGame:
    def __init__(self):
        self.playerColor = "null"
        while self.playerColor != "w" and self.playerColor != "b"
            print("Will you play white (w) or black (b)?")
            self.playerColor = input()
        if self.playerColor == "w":
            self.boardState = "xxxxxxxxxxxxxxxxxWxx"

    def printBoard(self):
        boardPrint = "|"
        boardPring =    "6: |-------|" + \
                        "   |   |   |" + \
                        "5: | ----- |" + \
                        "   | | | | |" + \
                        "4: | |---| |" + \

        for i in range(49):
            # a6
            if i == 0:
                boardPrint = boardPrint + self.boardState[17:17]
            # d6
            elif i == 3:
                boardPrint = boardPrint + self.boardState[18:18]
            # g6
            elif i == 6:
                boardPrint = boardPrint + self.boardState[19:19] + "|\n|       |"
            # a5 (not a path)
            elif i == 7:
                boardPrint = boardPrint + "| "
            # b5
            elif i == 8:
                boardPrint = boardPrint + self.boardState[14:14]
            # d5
            elif i == 10:
                boardPrint = boardPrint + self.boardState[15:15]
            # f5
            elif i == 12:
                boardPrint = boardPrint + self.boardState[16:16]
            # g5 (end of row)
            elif i == 13:
                boardPrint = boardPrint + " |\n"
            #
