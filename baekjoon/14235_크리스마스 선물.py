import sys
input = sys.stdin.readline

N = int(input())
a = []
for _ in range(N):
	temp = input().split()
	if temp[0] == '0':
		if len(a) > 0:
			maxIndex = a.index(max(a)) # 가중치가 가장 높은 선물을 찾음
			print(a.pop(maxIndex)) # 선물 출력
		else:
			print(-1)
	# 입력한 선물 가중치를 index 1부터 a에 추가
	else:
		for tmp in temp[1:]:
			a.append(int(tmp))

# warning, blog
# from Queue import priorityQueue, heapq 사용해보기			
# priorityQueue는 thread safe 멀티 스레드 환경에서 에러가 안나게한다.
# python 코테 볼 때는 priorityQueue 사용 x, 우선 순위 큐에서는 heapq 사용하는게 좋다.
# heapq : 멀티 스레드 환경에서는 주의해야함 - 충돌이 생길 수 있음 (검사 x) 
# for 문안에서 index 조회, 정렬하고 있다? 우선순위큐(heapq)를 사용해라.
