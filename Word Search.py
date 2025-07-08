"""
while word_len isnt equal to length(word)
go through every letter of word
for letter in board thats equal to our letter > dfs(letter)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def board_dfs(x, y, word_len):
            if word_len == len(word):
                return True

            if (x < 0 or x >= len(board) or 
                y < 0 or y >= len(board[0]) or 
                board[x][y] != word[word_len] or 
                board[x][y] == '#'):  # Already visited
                return False

            temp = board[x][y]
            board[x][y] = '#'

            found = board_dfs(x+1, y, word_len+1) or board_dfs(x-1, y, word_len+1) or board_dfs(x, y+1, word_len+1) or board_dfs(x, y-1, word_len+1)

            board[x][y] = temp

            return found

        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == word[0]:
                    if board_dfs(row, column, 0):
                        return True
        return False
