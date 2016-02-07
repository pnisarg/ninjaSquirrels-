import copy

class Problem:
    def __init__(self, initialState = [], boardValue = [], player = ''):
        self.initialState = initialState
        self.boardValue = boardValue
        self.player = player
        self.boardRowIds = ['1','2','3','4','5']
        self.boardColIds = ['A', 'B', 'C', 'D', 'E']
        self.stateNames = []
    
    def goalTest(self, state):
        for x in state:
            if x.count('*') > 0:
                return False
        return True

    def pathCost(self, state):
        #returns value of evaulation function
        countX = 0
        countO = 0
        for i in range(0,5):
            for j in range(0,5):
                if state[i][j] == 'X':
                    countX += self.boardValue[i][j]
                elif state[i][j] == 'O':
                    countO += self.boardValue[i][j]          
        if self.player == 'X':
            evaluation = countX - countO
        else:
            evaluation = countO - countX
        return evaluation

    #Returns list of all possible state traversable from given 'state'
    def possibleStates(self, state, turnTakingPlayer):
        moveY = [-1,1,0,0 ]
        moveX = [0, 0,-1,1]
        self.stateNames = []
        opponent = 'X' if turnTakingPlayer == 'O' else 'O'
        possibleStates = []
        for i in range(0,5):
            for j in range(0,5):
                if(state[i][j] == '*'):
                    isRaid = False
                    temp = copy.deepcopy(state)
                    temp[i][j] = turnTakingPlayer
                    self.stateNames.append(self.boardColIds[j]+self.boardRowIds[i]) 
                    # also convert any adjacent opponent's block (raid)
                    for x in range(0,4):
                        indexY = i + moveY[x]
                        indexX = j + moveX[x] 
                        if indexX < 0 or indexX > 4 or indexY < 0 or indexY >4:
                            continue
                        if temp[indexY][indexX] == turnTakingPlayer:
                            isRaid = True
                            break
                    if isRaid:
                        for x in range(0,4):
                            indexY = i + moveY[x]
                            indexX = j + moveX[x] 
                            if indexX < 0 or indexX > 4 or indexY < 0 or indexY >4:
                                continue
                
                            if temp[indexY][indexX] == opponent:
                                temp[indexY][indexX] = turnTakingPlayer
                    possibleStates.append(temp)
        return possibleStates
         

