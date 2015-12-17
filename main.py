from TicTacToe import TTO
import random


def choose(board,player):
    if len(board.available_moves()) == 9:
        return random.randint(0,8)
    move = board.alpha_beta_search(board,player)
    return move

if __name__ == '__main__':
    board = TTO()
    board.show()
    print "\n1.You move first \n2.Computer moves first"
    N=input('->')
    if N == 1:
        player = 'X'
        while not board.complete():
            player_move = int(raw_input("Next Move: ")) - 1
            if player_move not in board.available_moves():
                continue
            board.make_move(player_move, player)
            board.show()
            print '\n'
            if board.complete():
                break
            cplayer = TTO.get_opp(player)
            computer_move = choose(board, cplayer)
            board.make_move(computer_move, cplayer)
            board.show()
            print '\n'

    elif N == 2:
        player='O'
        while not board.complete():
            cplayer = TTO.get_opp(player)
            computer_move = choose(board, cplayer)
            board.make_move(computer_move, cplayer)
            board.show()
            print '\n'
            if board.complete():
                break
            player_move = int(raw_input("Next Move: ")) - 1
            if not player_move in board.available_moves():
                continue
            board.make_move(player_move, player)
            board.show()
            print '\n'

if board.winner(player):
    print "winner is", player
elif board.winner(cplayer):
    print "winner is",cplayer
else:
    print("TIE")