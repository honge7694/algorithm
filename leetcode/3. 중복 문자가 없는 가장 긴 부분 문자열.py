# 1. 배열에 저장 후, 같은게 나오면 배열 초기화.
# 2. count가 max_count 보다 크면 max_count = count

from collections import deque

def lengthOfLongestSubstring(s: str) -> int:

    # list = []
    # count = 0
    # max_count = 0

    # for char in s:
    #     if char not in list:
    #         list.append(char)
    #         count += 1
    #     else:
    #         if count > max_count:
    #             max_count = count
    #             count = 0
    #             list = []
    #             list.append(char)
    #             count += 1
    # else:
    #     if count > max_count:
    #         max_count = count 
        
    # return max_count

    max_count = 0
    q = deque()

    for char in s:
        # 큐에 들어있지 않다면 삽입
        if char not in q:
            q.append(char)

        else:
            # 큐에 들어있다면 index를 찾음.
            index = q.index(char)

            # 인덱스까지 모든 요소 pop.
            for _ in range(index+1):
                q.popleft()
            
            # 다시 문자열 넣음
            q.append(char)

        max_count = max(max_count, len(q))
    
    return max_count

s = "abcabcbb"
s1 = "bbbbbbb"
s2 = "pwwkew"
s3 = "dvdf"

print(lengthOfLongestSubstring(s3))