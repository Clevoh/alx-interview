#!/usr/bin/python3
"""N Queens
n queens problem of placing n non-attacking queens on an n×n chessboard
solution requires that no two queens share the same row, column, or diagonal
"""
import sys


def checkNqueensArgs(args):
    """Check for validity of argument of Nqueen
    """
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(args[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    return N


def nQueens(board):
    """n queens problem of placing n non-attacking queens on an n×n
    """
    res = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'Q':
                res.append([i, j])
    print(res)


def isSafe(board, row, col):
    """Check if two queens threaten each other or not
    """
    # return False if two queen share the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # return false if two queen share vertical diagonal
    (i, j) = (row, col)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # return false if two queen share the same '/' diagonal
    (i, j) = (row, col)
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def chessBoard(board, row):
    """Create a ChessBoard of NxN
    """
    # if `N` queens are placed successfully, print the solution
    if row == len(board):
        nQueens(board)
        return

    for i in range(len(board)):
        # if no two queens threaten each other
        if isSafe(board, row, i):
            # place queen on the current square
            board[row][i] = 'Q'

            # recur for the next row
            chessBoard(board, row + 1)

            #  backtrack and remove the queen from the current square
            board[row][i] = '*'


if __name__ == "__main__":
    N = checkNqueensArgs(sys.argv)
    # Create board
    board = [["*" for i in range(N)] for j in range(N)]
    chessBoard(board, 0)

