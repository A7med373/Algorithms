"""
Hint:
We can find the index of each square by the equation (row / 3) * 3 + (col / 3).
Then we use hash set for O(1) lookups while inserting the number into its row,
column and square it belongs to.
We use separate hash maps for rows, columns, and squares.


"""
import collections

board=[["1","2",".",".","3",".",".",".","."],
       ["4",".",".","5",".",".",".",".","."],
       [".","9","8",".",".",".",".",".","3"],
       ["5",".",".",".","6",".",".",".","4"],
       [".",".",".","8",".","3",".",".","5"],
       ["7",".",".",".","2",".",".",".","6"],
       [".",".",".",".",".",".","2",".","."],
       [".",".",".","4","1","9",".",".","8"],
       [".",".",".",".","8",".",".","7","9"]]


def is_valid(board):
    n = len(board)
    squares = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    for row in range(n):
        for col in range(n):
            if board[row][col] == '.':
                continue
            num = board[row][col]
            if (num in rows[row]
                    or num in cols[col]
                    or num in squares[(row // 3, col // 3)]):
                return False
            rows[row].add(num)
            cols[col].add(num)
            squares[(row // 3, col // 3)].add(num)
    return True
print(is_valid(board))