class TTO(object):

    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    def __int__(self,squares=[]):
        if len(squares)==9:
            self.squares=[None for i in range(9)]
        else:
            self.squares=squares

    def show(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print element

    def get_squares(self, player):
        return [k for k, v in enumerate(self.squares) if v == player]

    def complete(self):
        if None not in [v for v in self.squares]:
            return True
        if self.winner() is not None:
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
        elif self.winner(get_opp(player)):
            return depth - 10
        else:
            return 0

    def alpha_beta_search(self,state,player):
        alpha=-10
        beta=10
        opp=get_opp(player)
        val,move=self.max_value(state,alpha,beta,player,opp,0)
        return move

    def max_value(self,state,alpha,beta,player,opp,depth):
        if state.complete(): #check terminal
            return state.score(player,depth)
        val=-10
        depth += 1
        for k in self.available_moves():
            state.make_move(k,player)
            val = max(val,self.min_value(state,alpha,beta,player,opp,depth))
            if val >= beta:
                return val
            alpha=max(val,alpha)

        return val,k

    def min_value(self,state,alpha,beta,player,opp,depth):
        if state.complete(): #check terminal
            return state.score(player,depth)
        val=10
        depth += 1
        for k in self.available_moves():
            state.make_move(k,opp)
            val = max(val,self.max_value(state,alpha,beta,player,opp,depth))
            if val <= alpha:
                return val
            beta=min(val,beta)

        return val


def get_opp(player):
    if player == 'X':
        return 'O'
    return 'X'