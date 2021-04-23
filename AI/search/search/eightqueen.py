import search
import random
import time
# Module Classes

class EightQueensState:
    def __init__( self ):
        self.board = list()
        self.qPos = list()
        row = list()
        for i in range(8):
            for j in range(8):
                row.append('.')         
            self.board.append(row.copy())
            row.clear()        

    def isGoal( self ):
        if len(self.qPos) != 8:
            return False

        for i in range(len(self.qPos) - 1):
            pos = self.qPos[i]            
            # if not checkRow(pos[0], self.qPos[pos:]) or \
            #     not checkCol(pos[1], self.qPos[pos:]) or \
            #     not checkDiag(pos, self.qPos[pos:]):
            if not self.checkAtk(pos, self.qPos[i + 1:]):
                return False
        return True

    def checkAtk(self, pos, rest):
        x, y = pos
        if not self.checkCol(y, rest) or \
            not self.checkRow(x, rest) or \
            not self.checkDiag(pos, rest):

            return False
        return True

    def checkRow(self, pos, rest):
        for i in rest:
            if pos == i[0]:
                return False
        return True

    def checkCol(self, pos, rest):
        for i in rest:
            if pos == i[1]:
                return False
        return True

    def checkDiag(self, pos, rest):
        x, y = pos     
        i = 1   
        while (x + i < 8) and (y + i < 8):
            if [x + i, y + i] in rest: return False
            i += 1
        i = 1
        while (x - i > -1) and (y - i > -1):
            if [x - i, y - i] in rest: return False
            i += 1
        i = 1
        while (x + i < 8) and (y - i > - 1):
            if [x + i, y - i] in rest: return False
            i += 1
        i = 1
        while (x - i > -1) and (y + i < 8):
            if [x - i, y + i] in rest: return False
            i += 1                    
        return True

    def legalMoves( self ):
        moves = []
        for i in range(8):
            for j in range(8):
                if [i, j] not in self.qPos and \
                    self.checkAtk([i, j], self.qPos):

                    moves.append([i, j])
        
        return moves

    def result(self, move):
        row, col = move
                
        # Create a copy of the current chess board        
        newBoard = EightQueensState()
        newBoard.board = [rows.copy() for rows in self.board]        
        # And update it to reflect the move        
        newBoard.board[row][col] = 'Q'            
        newBoard.qPos = self.qPos.copy()
        newBoard.qPos.append([row, col])

        return newBoard

    # Utilities for comparison and display
    def __eq__(self, other):
        for row in range(8):
            if self.board[row] != other.board[row]:
                return False
        return True

    def __hash__(self):
        return hash(str(self.board))

    def __getAsciiString(self):
        """
          Returns a display string for the maze
        """
        lines = []
        horizontalLine = ('-' * (17))
        lines.append(horizontalLine)
        for row in self.board:
            rowLine = ''
            for col in row:                
                rowLine = rowLine + ' ' + col.__str__()
            lines.append(rowLine)
            lines.append(horizontalLine)
        return '\n'.join(lines)

    def __str__(self):
        return self.__getAsciiString()

# TODO: Implement The methods in this class

class EightQueensSearchProblem(search.SearchProblem):
    def __init__(self, board):
        self.board = board

    def getStartState(self):
        return board

    def isGoalState(self, state):
        return state.isGoal()

    def getSuccessors(self,state):
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 0))
        return succ

    def getCostOfActions(self, actions):
        return len(actions)

def createRandomChessBoard(moves=8):
    board = EightQueensState()
    for i in range(moves):
        # Execute a random legal move           
        board =  board.result(random.sample(board.legalMoves(), 1)[0])
        # board =  board.result([1,0])
    return board

if __name__ == '__main__':
    board = createRandomChessBoard(1)
    print('A random board:')
    print(board)

    problem = EightQueensSearchProblem(board)
    startTime = time.time()
    path = search.bfs(problem)
    
    print("Cal: ", time.time() - startTime)

    if path == 'FAILURE' or path == 'CUTOFF':
            print('No solution')
    else:
        print('Found a path of %d moves: ' % (len(path)))
        for node in path:
            print(node)
            print("\n")

    # curr = board
    # i = 1
    # for a in path:
    #     curr = curr.result(a)
    #     print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
    #     print(curr)

    #     input("Press return for the next state...")   # wait for key stroke
    #     i += 1