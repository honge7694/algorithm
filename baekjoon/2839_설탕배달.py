# 설탕 5kg으로 들 때
# 설탕 5kg, 3kg으로 나누어 들 때
# 설탕 3kg으로만 들 때
# 둘 다 못 나누어 들 때


N = int(input())
result = 0

# 설탕 5kg으로만
if N % 5 == 0:
    result = N // 5
    print(result)
else:
    while N > 0:
        N -= 3
        result += 1
        # 설탕을 나누어 들 때
        if N % 5 == 0:
            result += N // 5
            print(result)
            break
        # 설탕을 못 나누어 들 때
        elif 1 <= N <= 2:
            print(-1)
            break
        # 설탕 3kg으로만
        elif N == 0:
            print(result)
            break




