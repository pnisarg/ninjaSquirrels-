from node import Node
from problem import Problem
from problemSolver import ProblemSolver

class Controller:
    def __init__(self):
        self.algorithm = 0 #algorithm type: 1 - best first, 2 - minimax, 3 - alpha-beta 
        self.player = 'X' #Your player: X or O [X goes first]
        self.cuttingDepth = 0  #Cut-off depth starting from root
        self.boardValue = []  #value of each block in 5x5 board
        self.currentBoard = [] #Current board state, indicating position of each players territory; * -> unoccupied

    def readInput(self):
        self.algorithm = raw_input()  
        self.player = raw_input().strip()        
        self.cuttingDepth = raw_input()       
        self.boardValue = [] 
        self.currentBoard = [] 
        
        for x in range (0,5):
            self.boardValue.append(map(int, raw_input().strip().split()))
        for x in range(0,5):
            self.currentBoard.append(list(raw_input().strip()))
    
    def solveProblem(self):
        problemSolverObj = ProblemSolver(self.currentBoard, self.boardValue, self.player, self.cuttingDepth)
        if int(self.algorithm) == 1:
            problemSolverObj.greedyBFS()
        elif int(self.algorithm) == 2:
            problemSolverObj.initMinMax()

            
def main():
    # read Input 
    controllerObj = Controller()
    controllerObj.readInput()
    controllerObj.solveProblem()
    
             

if __name__ == "__main__":
    main()
