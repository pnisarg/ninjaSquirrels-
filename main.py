"""
__author__ = "Nisarg Pate"
__version__ = "1.0.1"
__date__ = "02/06/2016"
"""

from node import Node
from problem import Problem
import sys
from problemSolver import ProblemSolver

class Controller:
    def __init__(self):
        self.algorithm = 0 #algorithm type: 1 - best first, 2 - minimax, 3 - alpha-beta 
        self.player = 'X' #Your player: X or O [X goes first]
        self.cuttingDepth = 0  #Cut-off depth starting from root
        self.player1Algo = 1
        self.player2Algo = 1
        self.player2CuttingDepth = 1
        self.boardValue = []  #value of each block in 5x5 board
        self.currentBoard = [] #Current board state, indicating position of each players territory; * -> unoccupied

    def readInput(self):
        with open(sys.argv[2]) as inputFile:
            content = inputFile.readlines()

        self.algorithm = content[0]  
        if int(self.algorithm) != 4:
            self.player = content[1].strip()        
            self.cuttingDepth = content[2]     
            self.boardValue = [] 
            self.currentBoard = [] 
            
            for x in range (3,8):
                self.boardValue.append(map(int, content[x].split()))
            for x in range(8,13):
                self.currentBoard.append(list(content[x].strip()))

        else:
            self.player = content[1].strip()
            self.player1Algo = content[2].strip()
            self.cuttingDepth = content[3].strip()
            self.opponent = content[4].strip()
            self.player2Algo = content[5].strip()
            self.player2CuttingDepth = content[6].strip()
            for x in range (7,12):
                self.boardValue.append(map(int, content[x].split()))
            for x in range(12,17):
                self.currentBoard.append(list(content[x].strip()))

            

        
    
    def solveProblem(self):
        problemSolverObj = ProblemSolver(self.currentBoard, self.boardValue, self.player, self.cuttingDepth)
        if int(self.algorithm) == 1:
            problemSolverObj.greedyBFS()
        elif int(self.algorithm) == 2:
            problemSolverObj.initMinMax()
        elif int(self.algorithm) == 3:
            problemSolverObj.initAlphaBeta()
        elif int(self.algorithm) == 4:
            problemSolverObj.initBattleSimulation(self.player1Algo, self.player2Algo, self.opponent, self.player2CuttingDepth)

            
def main():
    # read Input 
    controllerObj = Controller()
    controllerObj.readInput()
    controllerObj.solveProblem()
    
             

if __name__ == "__main__":
    main()
