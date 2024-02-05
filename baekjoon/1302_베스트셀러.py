import sys
input = sys.stdin.readline

N = int(input())

books = [input().strip() for _ in range(N)]

book_count = dict()
for book in books :
	if book in book_count :
		book_count[book] += 1
	else:
		book_count[book] = 1

# 가장 많이 팔린 책의 값 GET
max_count = max(book_count.values())

# 많이 팔린 책들의 KEY GET
max_books = [book for book, count in book_count.items() if max_count == count]
max_books.sort()
print(max_books[0])