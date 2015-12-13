__author__ = 'wolfsgang'
import TTO
import random


def choose(board,player):
    if len(board.available_moves()) == 9:
        return random.choice(9)
    move = board.alpha_beta_search(board,player)
    return move

if __name__ == '__main__':
    board = TTO()
    board.show()
    print "1.You move first \n 2.Computer moves first"
    N=raw_input()
    if N == 1:
        player = 'X'
        while not board.complete():
            player_move = int(raw_input("Next Move: ")) - 1
            if player_move not in board.available_moves():
                continue
            board.make_move(player_move, player)
            board.show()
            if board.complete():
                break
            player = TTO.get_opp(player)
            computer_move = choose(board, player)
            board.make_move(computer_move, player)
            board.show()

    elif N == 2:
        player='O'
        while not board.complete():
            player = TTO.get_opp(player)
            computer_move = choose(board, player)
            board.make_move(computer_move, player)
            board.show()
            if board.complete():
                break
            player_move = int(raw_input("Next Move: ")) - 1
            if not player_move in board.available_moves():
                continue
            board.make_move(player_move, player)
            board.show()

print "winner is", board.winner()