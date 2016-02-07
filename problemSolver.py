from problem import Problem
from node import Node

class ProblemSolver:
    
    INFINITY = float("inf")
    logFile = "" 
    returnFlag = False
    globalAlpha = -INFINITY
    globalBeta = INFINITY
    globalBreakFlag = False
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


    # Greedy Best-first search algorithm, heuristic cost = path_cost(evaluation function)
    def greedyBFS(self):
        problemObj = Problem(self.initialState, self.boardValue, self.player)
        possibleStates = problemObj.possibleStates(self.initialState, self.player)
        stateCost = []
        for state in possibleStates:
            stateCost.append(problemObj.pathCost(state))
        nextState = possibleStates[stateCost.index(max(stateCost))]
        self.printState(nextState)
        self.outputState(nextState)  # save output to a file.

        # DEBUG lines
        # print max(stateCost)
        # print stateCost

    """ minimax algorithm
    :param node: node with complete set of children reachable at given depth
    :param depth: maxmimum depth desired in search tree. Root is at depth 0
    :param isMaxPlayer: First player is Max player. Hence, True if it is first player
    :param problemObj: Object of problem class. Provides defination and helper function for given problem 
    """
    def minimax(self, node, depth, isMaxPlayer, problemObj):
        # check for termination condition
        if (depth == 0) or problemObj.goalTest(node.state):
            return problemObj.pathCost(node.state)
    
        # if it is maximizing player
        if isMaxPlayer:
            bestValue = -self.INFINITY
            self.logFile.write("\n" + node.name + "," + str(int(self.cuttingDepth) - int(node.depth))
                               + "," + str(node.value).replace('inf', 'Infinity'))
            self.returnFlag = False
            for child in node.children:
                v = self.minimax(child, int(depth) - 1, False, problemObj)
                child.value = v
                bestValue = max(bestValue, v)
                node.value = bestValue
                if not self.returnFlag:
                    self.logFile.write("\n" + child.name + "," + str(int(self.cuttingDepth) - child.depth)
                                   + "," + str(child.value).replace('inf', 'Infinity'))
                self.logFile.write("\n" + node.name + "," + str(int(self.cuttingDepth) - int(node.depth))
                                   + "," + str(node.value).replace('inf', 'Infinity'))
                # print child.name+","+ str(int(self.cuttingDepth) - child.depth)+","+ str(child.value)
                # print node.name +","+ str(int(self.cuttingDepth) - int(node.depth))+","+ str(node.value)
            self.returnFlag = True
            return bestValue
        
        # if it is minimizing player
        else:
            bestValue = self.INFINITY
            self.logFile.write("\n" + node.name + "," + str(int(self.cuttingDepth) - int(node.depth))
                               + "," + str(node.value).replace('inf', 'Infinity'))
            self.returnFlag = False
            for child in node.children:
                v = self.minimax(child, int(depth) - 1, True, problemObj)
                child.value = v
                bestValue = min(bestValue, v)
                node.value = bestValue
                if not self.returnFlag:
                    self.logFile.write("\n" + child.name + "," + str(int(self.cuttingDepth) - child.depth)
                                   + "," + str(child.value).replace('inf', 'Infinity'))
                self.logFile.write("\n" + node.name + "," + str(int(self.cuttingDepth) - int(node.depth))
                                   + "," + str(node.value).replace('inf', 'Infinity'))
                # print child.name+","+ str(int(self.cuttingDepth) - child.depth)+","+ str(child.value)
                # print node.name +","+  str(int(self.cuttingDepth) - int(node.depth))+"," + str(node.value)
            self.returnFlag = True
            return bestValue


    def initMinMax(self):
        problemObj = Problem(self.initialState, self.boardValue, self.player)
        self.logFile = open("traverse_log.txt", "w")
        self.logFile.write("Node,Depth,Value")
        # self.logFile.write("root,0,-Infinity\n")
        node = Node(self.initialState, None, self.cuttingDepth, -float('inf'), "root", problemObj, self.player)   
        bestValue = self.minimax(node, self.cuttingDepth, True, problemObj)
        for childNode in node.children:
            if childNode.value == bestValue:
                self.outputState(childNode.state)  # stores result in next_state.txt file
                # self.printState(childNode.state)
                # print childNode.value
                break
        self.logFile.close()


    """
    Alpha-beta pruning
    :param node: node with complete set of children reachable at given depth
    :param depth: maxmimum depth desired in search tree. Root is at depth 0
    :param isMaxPlayer: First player is Max player. Hence, True if it is first player
    :param problemObj: Object of problem class. Provides defination and helper function for given problem 
    :param alpha: best value for maximizer player along path to root 
    :param beta: best value for minimizer player along paht to root
    """
    def alphabeta(self, node, depth, alpha, beta, isMaxPlayer, problemObj):
        # check for termination condition
        if (depth == 0) or problemObj.goalTest(node.state):
            return problemObj.pathCost(node.state)
        
        # if it is maximizing player
        if isMaxPlayer:
            bestValue = -self.INFINITY
            self.logFile.write("\n" + node.name + "," + str(int(self.cuttingDepth) - int(node.depth))
                               + "," + str(node.value).replace('inf', 'Infinity')
                               +","+str(alpha).replace('inf', 'Infinity')+","+str(beta).replace('inf', 'Infinity'))
            #all the following flags are used to match required output file specification.
            #they don't server any purpose in actual alpha-beta algorithm
            self.returnFlag = False
            breakFlag = False
            self.globalBreakFlag = False
            for child in node.children:
                value = self.alphabeta(child, int(depth) - 1, alpha, beta, False, problemObj)
                child.value = value
                bestValue = max(bestValue, value)
                if not self.returnFlag:
                    if self.globalBreakFlag:
                         self.logFile.write("\n" + child.name + "," + str(int(self.cuttingDepth) - child.depth)
                                   + "," + str(child.value).replace('inf', 'Infinity')
                                   +","+str(alpha).replace('inf', 'Infinity')+","+str(self.globalBeta).replace('inf', 'Infinity'))
                         self.globalBreakFlag = False
                    else:
                        self.logFile.write("\n" + child.name + "," + str(int(self.cuttingDepth) - child.depth)
                                   + "," + str(child.value).replace('inf', 'Infinity')
                                   +","+str(alpha).replace('inf', 'Infinity')+","+str(beta).replace('inf', 'Infinity'))
               

                self.globalAlpha = alpha   #useless; variable to store alpha value just for the purpose of output format 
                alpha = max(alpha, bestValue)
                node.value = bestValue
                if beta <= alpha:
                    breakFlag = True
                    self.globalBreakFlag = True
                    break
                self.logFile.write("\n" + node.name + "," + str(int(self.cuttingDepth) - int(node.depth))
                               + "," + str(node.value).replace('inf', 'Infinity')
                               +","+str(alpha).replace('inf', 'Infinity')+","+str(beta).replace('inf', 'Infinity'))
            if not breakFlag:
                self.returnFlag = True
            return bestValue
        
        # if it is minimizing player
        else:
            bestValue = self.INFINITY
            self.logFile.write("\n" + node.name + "," + str(int(self.cuttingDepth) - int(node.depth))
                               + "," + str(node.value).replace('inf', 'Infinity')
                               +","+str(alpha).replace('inf', 'Infinity')+","+str(beta).replace('inf', 'Infinity'))
            self.returnFlag = False
            breakFlag = False
            self.globalBreakFlag = False
            for child in node.children:
                value = self.alphabeta(child, int(depth) - 1, alpha, beta, True, problemObj)
                child.value = value
                bestValue = min(bestValue, value)
                
                if not self.returnFlag:
                    if self.globalBreakFlag:
                         self.logFile.write("\n" + child.name + "," + str(int(self.cuttingDepth) - child.depth)
                                   + "," + str(child.value).replace('inf', 'Infinity')
                                   +","+str(self.globalAlpha).replace('inf', 'Infinity')+","+str(beta).replace('inf', 'Infinity'))
                         self.globalBreakFlag = False
                    else:
                        self.logFile.write("\n" + child.name + "," + str(int(self.cuttingDepth) - child.depth)
                                   + "," + str(child.value).replace('inf', 'Infinity')
                                   +","+str(alpha).replace('inf', 'Infinity')+","+str(beta).replace('inf', 'Infinity'))
                self.globalBeta = beta   #useless; variable to store beta value just for the purpose of output format 
                beta = min(beta, bestValue)
                node.value = bestValue
                if beta <= alpha:
                    breakFlag = True
                    self.globalBreakFlag = True
                    break
                self.logFile.write("\n" + node.name + "," + str(int(self.cuttingDepth) - int(node.depth))
                               + "," + str(node.value).replace('inf', 'Infinity')
                               +","+str(alpha).replace('inf', 'Infinity')+","+str(beta).replace('inf', 'Infinity'))
            
            if not breakFlag:
                self.returnFlag = True
            return bestValue
 
    def initAlphaBeta(self):
        INFINITY = float('inf')
        problemObj = Problem(self.initialState, self.boardValue, self.player)
        self.logFile = open("traverse_log.txt", "w")
        self.logFile.write("Node,Depth,Value,Alpha,Beta")
        node = Node(self.initialState, None, self.cuttingDepth, -INFINITY, "root", problemObj, self.player)   
        bestValue = self.alphabeta(node, self.cuttingDepth, -INFINITY, INFINITY, True, problemObj)
        print bestValue
        for childNode in node.children:
            if childNode.value == bestValue:
                self.outputState(childNode.state)  # stores result in next_state.txt file
                # self.printState(childNode.state)
                # print childNode.value
                break
        self.logFile.close()       
        

