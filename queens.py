from copy import deepcopy


def init_board(n):
    return [[0 for x in range(n)] for y in range(n)]


def cover_attack_range_tower(board, x, y):
    n = len(board)
    for k in range(n):
        if board[x][k] != 1:
            board[x][k] = -1
    for k in range(n):
        if board[k][y] != 1:
            board[k][y] = -1
    return board


def cover_attack_range_queen(board, x, y):
    n = len(board)
    for k in range(n):
        if board[x][k] != 1:
            board[x][k] = -1
    for k in range(n):
        if board[k][y] != 1:
            board[k][y] = -1
    k = x
    j = y
    l = 0
    while k >= 0:
        if l + j < n and board[k][l + j] != 1:
            board[k][l + j] = -1
        if j - l >= 0 and board[k][j - l] != 1:
            board[k][j - l] = -1
        k -= 1
        l += 1
    k = x
    j = y
    l = 0
    while k < n:
        if l + j < n and board[k][l + j] != 1:
            board[k][j + l] = -1
        if j - l >= 0 and board[k][j - l] != 1:
            board[k][j - l] = -1
        k += 1
        l += 1
    return board


def print_board(board):
    n = len(board)
    queens = 0
    for x in range(n):
        print "|",
        for y in range(n):
            w = board[x][y]
            if w == 1:
                queens += 1
                print "T",
            if w == 0:
                print "0",
            if w == -1:
                print "X",
        print "|"
    raw_input("Press Enter to continue...")


def place_queen(board, queens):
    # print queens
    n = len(board)
    for x in range(n):
        if queens == 0 and x >= n / 2:
            continue
        if queens == 0:
            print "whipe"
        for y in range(n):
            t_board = deepcopy(board)
            if t_board[x][y] == 0:
                t_board[x][y] = 1
                queens += 1
                cover_attack_range_queen(t_board, x, y)
                # print "Original Board:"
                # print_board(board)
                # print "queens and tqueen ",queens
                # print "modified board Board:"
                # print_board(t_board)
                queens = place_queen(t_board, queens)
                queens -= 1
                if queens == n:
                    print "RIIPP"
                    print_board(t_board)
    return queens


chess_board = init_board(8)
place_queen(chess_board, 0)
