#Pailndrome - 회문  주어진 문자열 s로 회문을 만들어라

class Solution:
    def longestPalindrome(self, s):
        a = [0] * 52
        for i in s:
            if i.isupper():
                a[ord(i) - 65] += 1
            else:
                a[ord(i) - 71] += 1
        cnt = 0
        for i in a:
            cnt += i // 2 * 2 # i // 2의 몫을 구하고 * 2
            if cnt % 2 == 0 and i % 2 == 1:
                cnt += 1
        return cnt

# cnt += i // 2 * 2 부분의 경우 배열의 수를 더하는 것이아닌
# 그보다 작은 짝수 개수 만큼 더해여쟝한다.
