# part2_BFS_basic.py
# 깊이 우선 탐색이 가장 깊은 노드(leaf)부터 탐색하는 거라면
# 너비우선탐색(Breadth-First Search)은
# 가까운 영역부터 순차적으로 넓혀나가서 탐색하는 방식이다.
# 이진트리 구조를 예시로 들면, 각 레벨(depth)단위로 방문한 뒤
# 다음 레벨로 나아가는 방식인 것이다.

# BFS를 Queue 자료구조로 구현하는 함수
def bfs_queue(graph, start:str):
	# 방문한 노드를 저장할 set 자료구조 초기화
	visited = set()
	# 시작노드를 포함한 큐 생성(리스트 자료구조 활용)
	queue = [start]
	# 시작 노드를 방문 처리
	visited.add(start)

	# 큐가 빌 때까지 반복실행
	while queue:
		# 큐의 가장 왼쪽(먼젓번)의 노드를 꺼낸다(선입선출)
		vertex = queue.pop(0)
		# 현재 방문 중인 노드를 출력
		print(vertex, end=" ")

		# 현재 정점의 이웃 노드들을 순회
		for neighbor in graph[vertex]:
			# 아직 방문하지 않은 이웃 노드에 대해
			if neighbor not in visited:
				# 방문 처리
				visited.add(neighbor)
				# 큐의 오른쪽에 이웃 노드 추가
				queue.append(neighbor)


if __name__ == "__main__":
	graph_example = {
		'A': ['B', 'C'],      # A는 B, C와 연결됨
		'B': ['A', 'D', 'E'], # B는 A, D, E와 연결됨
		'C': ['A', 'F'],      # C는 A, F와 연결됨
		'D': ['B'],           # D는 B와 연결됨
		'E': ['B', 'F'],      # E는 B, F와 연결됨
		'F': ['C', 'E']       # F는 C, E와 연결됨
	}
	bfs_queue(graph_example, 'D')