def solution(board, moves):
    box = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if(board[j][i-1] == 0):
                pass
            else:
                box.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if(len(box) >=2 and box[-1:] == box[-2:-1]):
            answer += 1
            box.pop(-1)
            box.pop(-1)

    return answer*2
