# Nine-Man-Morris-Game-Variant
A variant on Nine Man Morris done for an Artificial Intelligence 
class in Summer 2023. This program is mostly divided into three
files, one for the Morris Game base class, one for the MiniMax
version of the Morris Game, and one for the Alpha-Beta pruning
version of the Morris game. 
## How to Run
This code was run with Python 3.8 on an iOS system. **Note that
running the code from files directly will overwrite the results
submitted with the project.**
### Running Files in Command Line
Each file can be run in the command line from within the 
morris_game folder.
- To play the game: python3 morris_game.py
- To generate MiniMax results: python3 minimax.py
- To generate Alpha-Beta results: python3 alphabeta.py

*Troubleshooting note: This command must be run in the morris_game
folder or else it will not work due to static direct pathing.*
### Running Files in PyCharm
Each file can be run directly using the play button in the upper
right corner of PyCharm.
### Making Custom Code
These modules are designed in order to best fit Python's style 
while also respecting the design in the project description.
Below are examples on how to call each section of the project
in a Python file:
#### MiniMaxOpening
```
from minimax import MiniMaxOpening

MiniMaxOpening("file1.txt", "file2.txt", DEPTH)
```
#### MiniMaxGame
```
from minimax import MiniMaxGame

MiniMaxGame("file1.txt", "file2.txt", DEPTH)
```
#### ABOpening
```
from alphabeta import ABOpening

ABOpening("file1.txt", "file2.txt", DEPTH)
```
#### ABGame
```
from alphabeta import ABGame

ABGame("file1.txt", "file2.txt", DEPTH)
```
#### MiniMaxOpeningBlack
```
from minimax import MiniMaxOpeningBlack

MiniMaxOpeningBlack("file1.txt", "file2.txt", DEPTH)
```
#### MiniMaxGameBlack
```
from minimax import MiniMaxGameBlack

MiniMaxGameBlack("file1.txt", "file2.txt", DEPTH)
```
#### MiniMaxOpeningImproved
```
from minimax import MiniMaxOpeningImproved

MiniMaxOpeningImproved("file1.txt", "file2.txt", DEPTH)
```
#### MiniMaxGameBlack
```
from minimax import MiniMaxGameImproved

MiniMaxGameImproved("file1.txt", "file2.txt", DEPTH)
```
## Examples
The project submission comes with two opening examples and three
midgame/endgame examples, along with results for every style
of play (MiniMaxOpening and MiniMaxGame along with their black
and improved versions, and ABOpening and ABGame) each labeled 
appropriately.
### Two Cases Where Alpha-Beta Produces Savings over MiniMax
Alpha-beta pruning results in evaluation savings in all examples
I have currently run. For example:
#### Board Opening 1
##### MiniMax:
```
Board Position: WxxxxxxWxxxxxxBxxxxxx
Positions evaluated by static estimation: **5882**
MINIMAX estimate: 1
```
##### Alpha-Beta Pruning
```
Board Position: WxxxxxxWxxxxxxBxxxxxx
Positions evaluated by static estimation: **606**
MINIMAX estimate: 1
```
#### Board Midgame/Endgame 1
##### MiniMax
```
Board Position: BxBWBWxBxxWWxxxxxxxxx
Positions evaluated by static estimation: 45
MINIMAX estimate: 995
```
##### Alpha-Beta Pruning
```
Board Position: BxBWBWxBxxWWxxxxxxxxx
Positions evaluated by static estimation: 167
MINIMAX estimate: 995
```
### Improved Static Evaluation
The improvement I made for static evaluation is that if the
board being evaluated has a mill, I add ten points in the 
opening phase to whoever plays it (+10 for white, -10 for
black when the player is white) or one thousand points in the
midgame/endgame phases. I believe this is better because it
incentivizes the algorithm to choose moves that lead to a mill,
which decreases the enemy pieces on the board.

This is most pronounced in the opening stage of the game where
starting with a mill early can be a large boon to whatever player
manages to do so. 
#### Board Opening 2
##### MiniMax (Regular)
```
Board Position: xxBBxWBxBxWWxxWxWxBBx
Positions evaluated by static estimation: 4086
MINIMAX estimate: -1
```
##### MiniMax (Improved)
```
Board Position: xxBBxxBxBWWWxxWxWxxBx
Positions evaluated by static estimation: 4086
MINIMAX estimate: 9
```
#### Board Opening 3
##### MiniMax (Regular)
```
Board Position: xBBBxWBxBxWWxxWxWxBBx
Positions evaluated by static estimation: 3596
MINIMAX estimate: -2
```
##### MiniMax (Improved)
```
Board Position: xBBBxxBxBWWWxxWxWxxBx
Positions evaluated by static estimation: 3596
MINIMAX estimate: 8
```
## GitHub
GitHub available upon request (currently private for academic
integrity). 