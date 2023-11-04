# 1. 제일 위에 있는 카드를 버린다.
# 2. 1.을 시행했으면 제일 위 카드를 아래로 옮긴다.
# 3. 카드가 1장 남을 때까지 반복한다.

from collections import deque

N = int(input())


# cards = sorted(cards, reverse=True)

# while len(cards) > 1:
#     cards.pop(0) # 1.
#     card = cards.pop(0)
#     cards.append(card) # 2.

def card_queue(num):
    cards = deque([num for num in range(1, num+1)])

    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    return cards.popleft()

print(card_queue(N))
