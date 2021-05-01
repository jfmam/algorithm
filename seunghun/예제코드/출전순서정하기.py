russian = [3000, 2700, 2800, 2200, 2500, 1900]
korean = [2800, 2750, 2995, 1800, 2600, 2000]
n = len(russian)

russianSort = sorted(russian, reverse=True)
koreanSort = sorted(korean, reverse=True)
cnt = 0


def selectWinnerList(rus):
    winnerList = []
    for i in koreanSort:
        if rus < i:
            winnerList.append(i)
        else:
            break
    return winnerList


for i in range(n):
    result = selectWinnerList(russian[i])
    if len(result):
        koreanSort.remove(result[-1])
        cnt += 1

print(cnt)