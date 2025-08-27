# part1_DFS_basic.py
# 깊이 우선 탐색(Depth-First Search)
# 한 경로를 따라서 더 이상 진행할 수 없는 부분까지 진행한 뒤
# 가장 가까운, 방문한 적 없는 경로로 다시 깊게 파고드는
# 가장 깊은 부분부터 탐색하는 탐색 알고리즘
# 스택 자료구조(혹은 재귀함수)를 활용하여 DFS를 구현할 수 있다.

# 재귀함수를 활용한 DFS 구현
def dfs_recursive(graph, start, visited=set()):
	# graph: 탐색할 그래프 정보를 매개변수를 통해 전달받는다.
	# start: 탐색할 그래프에서 어느 노드(정점)부터 시작을 했는지를 전달받는다.
	# 방문 여부를 담을 변수 visited
	# 이 함수를 최초로 실행했을 때는 set()자료구조로 초기화를 한다
	# 만약 최초 실행이 아니라 재귀적으로 실행된 거라면,
	# 전달된 visited를 visited 매개변수에 전달하면 된다.
	# visited = set()
	
	# 현재 노드(start)를 방문 처리
	visited.add(start)
	# 방문한 노드 출력
	print(start, end=" ")

	# 현재 노드의 이웃 노드를 탐색
	# 방문했는지 여부를 visited를 이용해서 검사
	for next_node in graph[start]:
		# 아직 방문하지 않은 이웃 노드에 대해서 재귀적으로 DFS 수행
		if next_node not in visited:
			dfs_recursive(graph, next_node, visited)
	# 이웃 노드들을 모두 방문했다면 반복문이 종료된다.

# 스택 자료구조를 이용한 단일 함수
def dfs_stack(graph, start):
	# 방문했는지 여부를 관리할 set자료구조 초기화
	visited = set()
	# 스택 자료구조로 데이터를 넣고 뺄 것이다.
	stack = [start]

	# 스택이 비어있지 않다면, 반복적으로 실행한다.
	while stack:
		# 스택에서 노드를 꺼냄(가장 최근에 추가된 노드)
		vertex = stack.pop() # vertex: 정점

		# 아직 방문하지 않은 정점이라면
		if vertex not in visited:
			visited.add(vertex) # 방문 처리
			print(vertex, end=" ")

			# 현재 노드의 이웃 노드들을 스택에 추가
			stack.extend([e for e in graph[vertex] if e not in visited])


if __name__ == "__main__":
	graph_example = {
		'A': ['B', 'C'],      # A는 B, C와 연결됨
		'B': ['A', 'D', 'E'], # B는 A, D, E와 연결됨
		'C': ['A', 'F'],      # C는 A, F와 연결됨
		'D': ['B'],           # D는 B와 연결됨
		'E': ['B', 'F'],      # E는 B, F와 연결됨
		'F': ['C', 'E']       # F는 C, E와 연결됨
	}
	# A -> B -> D -> E -> F -> C
	dfs_recursive(graph_example, 'A')
	print()
	# A -> C -> F -> E -> B -> D
	dfs_stack(graph_example, 'A')
	# 두 방식이 방문하는 순서가 다른 이유는
	# 갈림길에서 왼쪽을 먼저 방문하냐, 오른쪽을 먼저 방문하냐 따라 달라진다.