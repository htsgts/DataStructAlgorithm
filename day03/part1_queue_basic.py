# part1_queue_basic.py
# 자료구조 Queue
# Queue 자료구조는 이름처럼 대기열을 구현한 자료구조다.
# 많은 데이터를 처리하는 데 있어서 어떤 데이터를 먼저 처리하느냐를 정하는 것에 중점을 둔다.
# Queue는 먼저 들어온 데이터를 먼저 처리하는 선입선출(FIFO)의 구조를 가진다.
# 이를 리스트 자료구조로 구현하면 먼저 들어온 0번째 요소를 먼저 내보내는 방식을 취하면 된다.

def queue():
	que = list()
	# 데이터를 추가
	# 이때 마지막에 요소를 추가하므로 append를 사용한다.
	que.append("문서1")
	que.append("문서2")
	que.append("문서3")
	print(que)
	# 먼저 들어온 0번째 요소를 반환 및 사용
	item = que.pop(0)
	print(item)
	print("queue:", que)

	# 1번째 요소 제거
	item = que.pop(0)
	print(item)
	print("queue:", que)

	# 2번째 요소 제거
	item = que.pop(0)
	print(item)
	print("queue:", que)

if __name__ == "__main__":
	queue()
	pass