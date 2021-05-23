n = 7  # input()
board = [[2, 5, 1, 6, 1, 4, 1],
         [6, 1, 1, 2, 2, 9, 3],
         [7, 2, 3, 2, 1, 3, 1],
         [1, 1, 3, 1, 7, 1, 2],
         [4, 1, 2, 3, 4, 1, 2],  # [4,1,2,3,4,1,3], [4,1,2,3,4,1,2]
         [3, 3, 1, 2, 3, 4, 1],
         [1, 5, 2, 9, 4, 7, 0]]
cache = [[-1 for _ in range(n)] for _ in range(n)]


def jump(x, y):
    if y >= n or x >= n:
        return 0
    if y == n-1 and x == n-1:
        return 1
    if cache[x][y] != -1:
        return cache[x][y]
  
    jump_size = board[x][y]
    cache[x][y] = jump(x+jump_size, y) or jump(x, y+jump_size)
    return cache[x][y]


print(jump(0, 0))
