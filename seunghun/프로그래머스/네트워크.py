def solution1(n, computers): # 실패
    answer = n
    for i in range(n):
        for j in range(i, n):
            if i != j and computers[i][j] == 1:
                answer -= 1
                computers[i][j] = 0
                computers[j][i] = 0
    return answer

def solution2(n, computers):
    visited = [0] * n
    answer = 0
    def DFS(x):
        visited[x] = True
        for i in range(n):
            if visited[i] == False and computers[x][i] == 1:
                computers[x][i] = 0
                computers[i][x] = 0
                DFS(i)

    for i in range(n):
        if visited[i] == False:
            DFS(i)
            answer += 1
    return answer
