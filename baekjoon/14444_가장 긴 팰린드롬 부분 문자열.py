"""
접근 방법
1. 반복문으로 가장 처음 문자열을 고정한다.
2. 처음+1 문자열로 반복문을 실행한다.
3. 단어의 몇번째에서 중심이 되는지 검사해야할까??
4. 데칼코마니를 생각했지만 중심이 어딘지 잡을 방법을 모르겠습니다.

1. 반복문으로 가장 처음 문자열을 고정한다.
2. 처음+1 문자열로 반복문을 실행하며 새로운 배열에 값을 넣는다.
3. 새로운 배열에 이미 있는 문자가 있다면 다음 문자를 비교하며 문자열의 중앙을 찾는다.
4. 3번을 할시 범위를 벗어나는 에러가 있다...
데칼코마니를 생각했지만 중심이 어딘지 잡을 방법을 모르겠습니다.
"""

# S = input()

# decal = []
# # 1.
# for i in range(S):
#     # 2.
#     for j in range(i+1, S):
#         # 3.
#         if j in decal:
#             # ??????
#         else:
#             decal.append(j)

def longestPalindrome(s: str) -> str:
    N = len(s)  # 입력 문자열 s의 길이
    dp = [[False]*N for _ in range(N)]  # DP (Dynamic Programming) 테이블 초기화
    ans = s[0]  # 결과로 반환할 가장 긴 팰린드롬 문자열, 초기값은 s의 첫 글자

    # 모든 길이가 1인 부분 문자열은 팰린드롬
    for n in range(N):
        dp[n][n] = True

    # 문자열을 역순으로 탐색하며 팰린드롬 여부를 검사
    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            if s[i] == s[j]:  # 문자열의 i번째와 j번째 문자가 같은 경우
                if j - i == 1 or dp[i+1][j-1]:  # j와 i가 바로 옆에 위치하거나, i+1부터 j-1까지가 팰린드롬인 경우
                    dp[i][j] = True  # 현재 문자열은 팰린드롬
                    if len(ans) < len(s[i:j+1]):  # 현재까지의 최장 팰린드롬과 비교
                        ans = s[i:j+1]  # 최장 팰린드롬을 갱신
    return ans

s = 'babad'
print(longestPalindrome(s))

