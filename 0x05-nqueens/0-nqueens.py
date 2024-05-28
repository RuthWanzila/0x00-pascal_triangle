#!/usr/bin/python3

import sys

def print_board(board):
   print([[row, col] for row, col in board])

def is_valid(board, row, col):
   # Check column
   for row_idx, c in board:
       if c == col:
           return False
           
   # Check diagonals 
   for r, c in board:  
       if abs(row - r) == abs(col - c):
           return False
           
   return True

def solve_nqueens(n):
   if n < 4:
       print("N must be at least 4")
       sys.exit(1)
        
   if not n.isnumeric():
       print("N must be a number")
       sys.exit(1)
        
   board = []   
   backtrack(board, 0, n)
   
def backtrack(board, row, n):
   if row == n:
       print_board(board)
       return
        
   for col in range(n):
       if is_valid(board, row, col):
           board.append([row, col])
           backtrack(board, row+1, n)  
           board.pop()
           
if __name__ == '__main__':
   if len(sys.argv) != 2:
       print("Usage: nqueens N")
       sys.exit(1)
        
   n = int(sys.argv[1])   
   solve_nqueens(n)
