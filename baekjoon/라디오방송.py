# 1. n = 교환대에 있는 발신자 수
# 2. m = k번째 발신자에게 도달할 때까지 매번 건너뛰는 위치의 수
# 3. n개의 1을 갖고있는 데크 생성
# 4. m-1번째 값을 0으로 만듬
# 5. 반복하며 0이 아닌 값을 m_count 후 m-1과 같아지면, deque[m-1]=0 m_count = 0으로 만듬.
# 6. k == count가 되면 종료
import collections


while True:
    n, m, k = map(int, input().split())

    caller = [1] * n # 발신자 베이스
    count = 0 
    index = 0
    result = 0
    if n == 0 and m == 0 and k == 0:
        break
    for i in range(k):
        while True:
            
            # 마지막 실행 조건
            if i == k-1 and count == m-1 and caller[index] == 1:
                result = index
                break

            # m번째 사람이면 0으로 초기화
            if m != 1 and i != k-1 and count == m-1:
                caller[index] = 0
                count = 0
                break
            # m==1일떄, 종료조건?
            if m == 1 and i != k-1 and count == m-1 :
                caller[index] = 0
                index += 1
                count = 0
                break
                
                

            # caller[i]가 1이면 index, count += 1, 아니면 index += 1
            if caller[index] == 1:
                count += 1
                index += 1
            else:
                index += 1
                continue
            
            # index 초기화
            if index == n-1:
                index = 0
                if count != m-1:
                    count += 1

    print(result+1)

