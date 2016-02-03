from problem import Problem

class ProblemSolver:

    def __init__(self, initialState, boardValue, player, cuttingDepth):
        self.initialState = initialState
        self.boardValue = boardValue
        self.player = player
        self.cuttingDepth = cuttingDepth

    def printStates(self, states):
        print "================================"
        for x in states:
            for y in x:
                print ''.join(y)
            print "================================"

    def printState(self, state):
        print "================================"
        for x in state:
            print ''.join(x)
        print "================================"
    
    def outputState(self, state):
        outFile = open("next_state.txt", "w+")
        for x in state:
            outFile.write(''.join(x))
            outFile.write("\n")
        outFile.close()



    def greedyBFS(self):
        problemObj = Problem(self.initialState, self.boardValue,self.player)
        possibleStates = problemObj.possibleStates(self.initialState, self.player)
        stateCost = []
        for state in possibleStates:
            stateCost.append(problemObj.pathCost(state))
        nextState = possibleStates[stateCost.index(max(stateCost))]
        self.printState(nextState)
        print max(stateCost)
        print stateCost
        self.outputState(nextState)
        
