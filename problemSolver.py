from problem import Problem
from node import Node

class ProblemSolver:
    
    INFINITY = float("inf")
    
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


    #Greedy Best-first search algorithm, heuristic cost = path_cost(evaluation function)
    def greedyBFS(self):
        problemObj = Problem(self.initialState, self.boardValue,self.player)
        possibleStates = problemObj.possibleStates(self.initialState, self.player)
        stateCost = []
        for state in possibleStates:
            stateCost.append(problemObj.pathCost(state))
        nextState = possibleStates[stateCost.index(max(stateCost))]
        self.printState(nextState)
        self.outputState(nextState) #save output to a file.

        #DEBUG lines
        # print max(stateCost)
        # print stateCost


    def minimax(self, node, depth, isMaxPlayer, problemObj):
        
        if (depth == 0) or problemObj.goalTest(node.state):
            return problemObj.pathCost(node.state)

        if isMaxPlayer:
            bestValue = -self.INFINITY
            for child in node.children:
                v = self.minimax(child, int(depth) - 1, False, problemObj)
                child.value = v
                bestValue = max(bestValue, v)
                node.value = bestValue
                print child.name+","+ str(int(self.cuttingDepth) - child.depth)+","+ str(child.value)
                print node.name +","+ str(int(self.cuttingDepth) - child.depth)+","+ str(node.value)
            return bestValue

        else:
            bestValue = self.INFINITY
            for child in node.children:
                v = self.minimax(child, int(depth) - 1, True, problemObj)
                child.value = v
                bestValue = min(bestValue, v)
                node.value = bestValue
                print child.name+","+ str(int(self.cuttingDepth) - child.depth)+","+ str(child.value)
                print node.name +","+  str(int(self.cuttingDepth) - child.depth)+"," + str(node.value)
            return bestValue

        #DEBUG lines
        # print node
        # for child in node.children:
        #     print child.name +" Depth = " , child.depth , " value: ", child.value
        #     for grandChild in child.children:
        #         print "   "+grandChild.name + " Depth = " , grandChild.depth, " value: ", grandChild.value





    def initMinMax(self):
        problemObj = Problem(self.initialState, self.boardValue,self.player)
        node = Node(self.initialState, None, self.cuttingDepth,-float('inf'),"root",problemObj, self.player)   
        print self.minimax(node, self.cuttingDepth, True, problemObj)
        


