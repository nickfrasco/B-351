import math

#Worked with Rowan Lavel

class Player:

    def __init__(self, depthLimit, isPlayerOne):

        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit

    # Returns a heuristic for the board position
    # Good positions for 0 pieces should be positive and good positions for 1 pieces
    # should be negative
    # this is really bad but whatever
    def heuristic(self, board):
        h = 0
        state = board.board

        for col in range(0, board.WIDTH):
            for row in range(0, board.HEIGHT):
                # check horizontal streaks
                try:
                    # add player one streak scores to heur
                    if state[col][row] == state[col + 1][row] == 0: h += 10
                    if state[col][row] == state[col + 1][row] == state[col + 2][row] == 0: h += 100
                    if state[col][row] == state[col + 1][row] == state[col + 2][row] == state[col + 3][row] == 0: h += 10000

                    # subtract player two streak score to heur
                    if state[col][row] == state[col + 1][row] == 1: h -= 10
                    if state[col][row] == state[col + 1][row] == state[col + 2][row] == 1: h -= 100
                    if state[col][row] == state[col + 1][row] == state[col + 2][row] == state[col + 3][row] == 1: h -= 10000
                except IndexError:
                    pass

                # check vertical streaks
                try:
                    # add player one vertical streaks to heur
                    if state[col][row] == state[col][row + 1] == 0: h += 10
                    if state[col][row] == state[col][row + 1] == state[col][row + 2] == 0: h += 100
                    if state[col][row] == state[col][row + 1] == state[col][row + 2] == state[col][row + 3] == 0: h += 10000

                    # subtract player two streaks from heur
                    if state[col][row] == state[col][row + 1] == 1: h -= 10
                    if state[col][row] == state[col][row + 1] == state[col][row + 2] == 1: h -= 100
                    if state[col][row] == state[col][row + 1] == state[col][row + 2] == state[col][row + 3] == 1: h -= 10000
                except IndexError:
                    pass

                # check positive diagonal streaks
                try:
                    # add player one streaks to heur
                    if not row + 3 > board.HEIGHT and state[col][row] == state[col + 1][row + 1] == 0: h += 100
                    if not row + 3 > board.HEIGHT and state[col][row] == state[col + 1][row + 1] == state[col + 2][row + 2] == 0: h += 100
                    if not row + 3 > board.HEIGHT and state[col][row] == state[col + 1][row + 1] == state[col + 2][row + 2] == state[col + 3][row + 3] == 0: h += 10000

                    # add player two streaks to heur
                    if not row + 3 > board.HEIGHT and state[col][row] == state[col + 1][row + 1] == 1: h -= 100
                    if not row + 3 > board.HEIGHT and state[col][row] == state[col + 1][row + 1] == state[col + 2][row + 2] == 1: h -= 100
                    if not row + 3 > board.HEIGHT and state[col][row] == state[col + 1][row + 1] == state[col + 2][row + 2] == state[col + 3][row + 3] == 1: h -= 10000
                except IndexError:
                    pass

                # check negative diagonal streaks
                try:
                    # add  player one streaks
                    if not row - 3 < 0 and state[col][row] == state[col + 1][row - 1] == 0: h += 10
                    if not row - 3 < 0 and state[col][row] == state[col + 1][row - 1] == state[col + 2][row - 2] == 0: h += 100
                    if not row - 3 < 0 and state[col][row] == state[col + 1][row - 1] == state[col + 2][row - 2] == state[col + 3][row - 3] == 0: h += 10000

                    # subtract player two streaks
                    if not row - 3 < 0 and state[col][row] == state[col + 1][row - 1] == 1: h -= 10
                    if not row - 3 < 0 and state[col][row] == state[col + 1][row - 1] == state[col + 2][row - 2] == 1: h -= 100
                    if not row - 3 < 0 and state[col][row] == state[col + 1][row - 1] == state[col + 2][row - 2] == state[col + 3][row - 3] == 1: h -= 10000
                except IndexError:
                    pass
        return h


class PlayerMM(Player):
    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)


    #returns the optimal column to move in by implementing the Minimax algorithm
    def findMove(self, board):
        return self.miniMax(board,self.depthLimit,self.isPlayerOne)[1]


    def miniMax(selfself,board,depth,player):
        if board.isTerminal() == 0:
            return -math.inf if player else math.inf, -1
        elif depth == 0:
            return self.heuristic(board), -1


        if player:
            bestScore = -math.inf
            choose = lambda x: x > bestScore
        else:
            bestScore = math.inf
            choose = lambda x: x < bestScore

        bestMove = -1

        children = board.children()
        for child in children:
            move,childboard = child
            score = self.miniMax(childboard, depth -1, player)[0]
            if choose(score):
                bestScore = score
                bestMove = move

        return bestScore, bestMove


class PlayerAB(Player):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)



    #returns the optimal column to move in by implementing the Alpha-Beta algorithm
    def findMove(self, board):
        return self.alphaBeta(board,self.depthLimit,self.isPlayerOne, -math.inf, math.inf)[1]

    def alphaBeta(self, board, depth, player, alpha, beta):
        if board.isTerminal() == 0:
            return -math.inf if player else math.inf, -1
        elif depth == 0:
            return self.heuristic(board), -1

        if player:
            bestScore = -math.inf
            choose = lambda x: x > bestScore
        else:
            bestScore = math.inf
            choose = lambda x: x < bestScore

        bestMove = -1

        children = board.children()
        for child in children:
            move, childboard = child
            score = self.alphaBeta(childboard, depth - 1, player, alpha, beta)[0]
            if choose(score):
                bestScore = score
                bestMove = move

            if player:
                alpha = max(alpha, score)
            else:
                beta = min(beta, score)
            if alpha >= beta:
                break

        return bestScore, bestMove


#######################################################
###########Example Subclass for Testing
#######################################################

#This will inherit your findMove from above, but will override the heuristic function with
#a new one; you can swap out the type of player by changing X in "class TestPlayer(X):"
class TestPlayer(PlayerMM):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    #define your new heuristic here
    def heurisitic(self):
        pass

#Credit to Abe Leite
class ManualPlayer(Player):
    def findMove(self, board):
        opts = " "
        for c in range(board.WIDTH):
            opts += " " + (str(c + 1) if len(board.board[c]) < 6 else ' ') + "  "
        print(opts)

        col = input("Place a " + ('O' if self.isPlayerOne else 'X') + " in column: ")
        col = int(col) - 1

        return col