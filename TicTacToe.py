__author__ = 'ideapad'
import copy


class TTO(object):

    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    def __init__(self, squares=[]):
        if len(squares) == 0:
            self.squares = [None for i in range(9)]
        else:
            self.squares = squares

    def show(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print element

    def get_squares(self, player):
        return [k for k, v in enumerate(self.squares) if v == player]

    def complete(self):
        if None not in [v for v in self.squares]:
            return True
        if self.winner('X') or self.winner('O') is not None:
            return True
        return False

    def make_move(self, position, player):
        self.squares[position] = player

    def available_moves(self):
        return [k for k, v in enumerate(self.squares) if v is None]

    def winner(self,player):
        if player in ('X', 'O'):
            positions = self.get_squares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return True
        return None #TIE

    def score(self,player,depth):
        if self.winner(player):
            return 10 - depth
        elif self.winner(TTO.get_opp(player)):
            return depth - 10
        else:
            return 0

    def alpha_beta_search(self,board,player):
        alpha = -10
        beta = 10
        v_max = -10
        state = copy.copy(board)
        opp = TTO.get_opp(player)
        for k in state.available_moves():
            if state.complete(): #check terminal
                val,move = state.score(player,0),k
                break
            state.make_move(k,player)
            val = state.min_value(state,alpha,beta,player,opp,0)
            state.make_move(k, None)

            if v_max <= val:
                v_max,move = val,k

        return move

    def max_value(self,state,alpha,beta,player,opp,depth):

        if state.complete(): #check terminal
            return state.score(player,depth)

        val = -10
        depth += 1
        for k in state.available_moves():
            state.make_move(k,player)
            val = max(val,state.min_value(state,alpha,beta,player,opp,depth))
            '''if val >= beta:
                return val
            alpha = max(val,alpha)'''
            state.make_move(k, None)
        return val

    def min_value(self,state,alpha,beta,player,opp,depth):

        if state.complete(): #check terminal
            return state.score(player,depth)
        val = 10
        depth += 1
        for k in state.available_moves():
            state.make_move(k,opp)
            val = min(val,state.max_value(state,alpha,beta,player,opp,depth))
            '''if val <= alpha:
                return val
            beta=min(val,beta)'''
            state.make_move(k, None)
        return val

    @staticmethod
    def get_opp(player):
        if player == 'X':
            return 'O'
        return 'X'