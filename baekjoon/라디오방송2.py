n, m, k = map(int, input().split())

caller = [1] * n # 발신자 베이스
caller_len = len(caller)
print(caller_len)
# 짝수일 때는 +1
# 홀수일 때는 그냥


for i in range(k):
    if i == 0:
        caller[m-1] = 0
        caller_len -= 1
        break
    
    if i % 2 != 0:
        caller[(caller_len % m) + 1] = 0
        caller_len -= 1
        break

    else:
        caller[caller_len % m] = 0
        caller_len -= 1
        break

print(caller)
    