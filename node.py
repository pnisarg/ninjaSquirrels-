from problem import Problem
import copy
        
class Node:
    INFINITY = float('inf')
    
    def __init__(self, state = [], parent = None, depth = 0, value = -float('inf'), name = "root", problemObj = None, turnTakingPlayer = 'X'):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.value = value
        self.name = name
        self.problemObj = problemObj
        self.turnTakingPlayer = turnTakingPlayer
        self.children = []
        self.expand()


    def __repr__(self):
        return "<Node %s, depth= %s, state = %s, parent: %s" % (self.name, self.depth, self.state, self.parent.name if self.parent!=None else "") 

    def expand(self):
        if self.depth > 0:
            possibleStates = self.problemObj.possibleStates(self.state, self.turnTakingPlayer)
            stateNames = copy.deepcopy(self.problemObj.stateNames)
            i = 0
            for possibleState in possibleStates:
                # if your player is 'X' (then max player is 'X')
                if self.problemObj.player != self.turnTakingPlayer:
                    self.children.append(Node(possibleState, self, int(self.depth) - 1, -self.INFINITY, 
                                          stateNames[i], self.problemObj, 'O' if self.turnTakingPlayer == 'X' else 'X'))
                else:
                    self.children.append(Node(possibleState, self, int(self.depth) - 1, self.INFINITY, 
                                          stateNames[i], self.problemObj, 'O' if self.turnTakingPlayer == 'X' else 'X'))
                i = i+1
