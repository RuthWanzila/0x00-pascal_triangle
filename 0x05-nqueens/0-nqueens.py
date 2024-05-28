#!/usr/bin/env python3
"""Solve the N Queens problem"""

import argparse
from typing import List

def validate_input(n: int) -> None:
    """Validate input board size"""
    if not n.isdigit():
        print("N must be a number")
        exit(1)
    if int(n) < 4:
        print("N must be at least 4")
        exit(1)

def queens(
    board_size: int, 
    row_index: int = 0,
    queens_cols: List[int] = [],
    diag1: List[int] = [], 
    diag2: List[int] = []
) -> List[List[int]]:
    """Find all possible queen placements on the board"""
    if row_index < board_size:
        for col in range(board_size): 
            if col not in queens_cols and 
                row_index + col not in diag1 and
                row_index - col not in diag2:
                yield from queens(
                    board_size, row_index+1, 
                    queens_cols + [col], 
                    diag1 + [row_index+col],
                    diag2 + [row_index-col]
                )
    else:
        yield queens_cols

def solve(board_size: int) -> None:
    """Solve the N Queens problem and print solutions"""
    for solution in queens(board_size):
        print(solution)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="Board size")
    args = parser.parse_args()
    
    n = args.n
    validate_input(n)
    
    solve(n)
