# part2_binary_tree.py
# 이진 트리(Binary Tree)
# 이진트리는 연결리스트를 좌우노드로 분화하는 형태로 바꾼 구조를 가리킨다.
# 즉, 연결리스트가 다음 노드 하나만 가리켰다면
# 이진트리는 이전이나 다음이라는 개념이 아니라
# 둘 다 다음인데, 왼쪽과 오른쪽으로 분화하는 개념인 것이다.

# 노드 클래스
# 기존의 노드 클래스와 같지만, left와 right를 속성으로 가진다는 게 다른 점이다.
class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right= right

# 이진트리 클래스
# 이진트리 클래스에서는 새로운 데이터를 삽입하거나
# 데이터를 순차적으로 순회하는 기능정도만 구현해보자.
class BinaryTree():
	# 이진트리의 최상위 노드인 root를 전달받거나 전달받지 못했다면
	# None으로 지정하는 self.root
	def __init__(self, root:Node=None):
		self.root = root
	
	# 새로운 데이터를 이진트리에 추가하는 메서드
	def insert(self, data):
		# 새롭게 입력되는 데이터가 노드인지 여부에 따라 다르게 처리한다.
		new_node = data if isinstance(data, Node) else Node(data)
		
		# 루트 노드가 없는 이진트리라면
		if not self.root:
			self.root = new_node
			return # 데이터 삽입이 끝났으므로 메서드 종료

		# 먼저 확인한 노드를 먼저 내보내는 방식을 취해야 하므로
		# queue 자료구조를 활용하여 노드의 자식노드를 확인하고 데이터를 삽입한다.
		queue = [self.root]
		# 큐가 비어있지 않은 동안 무한히 자식 노드 확인
		while queue:
			# 현재 확인할 노드
			current = queue.pop(0) # 0번째 노드를 추출하여 current에 담아 확인한다.
			if not current.left:
				# 현재 보고 있는 노드의 왼쪽 노드가 비어있으면(None)
				# 해당 위치에 새로운 데이터 노드를 삽입한다.
				current.left = new_node
				# 데이터 삽입이 끝났으므로 메서드를 종료한다.
				return
			if current.right is None:
				current.right = new_node
				return
			# 자식 노드 좌우가 모두 채워져 있을 경우
			# 자식 노드들도 삽입할 데이터 노드의 부모 노드가 될 수 있다.
			# -> 큐에 좌우 자식 노드를 모두 담아야 한다.
			queue.extend([current.left, current.right])
		# 큐가 빌 때까지 자식 노드가 꽉 차있는 경우는 발생할 수 없다.
		# 그런 경우가 있다면, 그건 루트가 아닌 자식 노드가 루트로 지정된 경우뿐이다(예외상황)
		# 그렇기 때문에 while문 아래쪽으로 내려오는 경우는 고려하지 않는다.

	# 데이터 순회방법
	# 이진트리에서 데이터를 순회할 때에는 세 가지 방법이 있는데
	# 이 구분은 현재 노드의 데이터를 언제 출력할 것인가를 기준으로 한다.
	# 즉, 좌우 자식노드를 확인하기 전에 데이터를 출력하면 전위순회
	# 왼쪽 자식노드를 확인한 뒤 오른쪽 자식노드를 확인하기 전에 데이터를 출력하면 중위순회
	# 좌우 자식노드를 모두 확인한 뒤 데이터를 출력하면 이는 후위순회라고 부른다.
	# 이러한 순회하는 메서드는 모두 재귀함수로 구현된다.

	# 전위순회(preorder Traversal)
	def preorder(self, node: Node):
		if node: # 전달받은 노드가 존재하면(None이 아니면)
			# 재귀케이스
			# 전위순회이므로 먼저 데이터를 출력한다.
			print(node.data, end=" ")
			# 재귀적으로 전위순회를 진행한다.
			self.preorder(node.left)
			self.preorder(node.right)
		# 노드가 비어있다면 아무것도 하지 않는다.
		return

	# 중위순회(inorder Traversal)
	def inorder(self, node: Node):
		if node: # 전달받은 노드가 존재하면(None이 아니면)
			self.inorder(node.left) # 왼쪽 자식 노드를 먼저 탐색한 뒤
			print(node.data, end=" ") # 현재 노드의 데이터를 출력한다.
			self.inorder(node.right)
		return

	# 후위순회(postorder Traversal)
	def postorder(self, node: Node):
		if node: # 전달받은 노드가 존재하면(None이 아니면)
			self.postorder(node.left) # 왼쪽 자식 노드를 먼저 탐색한 뒤
			self.postorder(node.right)# 오른쪽 자식노드도 다 확인하고
			print(node.data, end=" ") # 마지막에 현재 노드의 데이터를 출력한다.
		return

if __name__ == "__main__":
	root_node = Node(1)
	bt = BinaryTree(root_node)
	bt.insert(2)
	bt.insert(3)
	bt.insert(4)
	bt.insert(5)
	bt.insert(6)
	bt.insert(7)
	bt.preorder(bt.root)  # 1 2 4 5 3 6 7
	print()
	bt.inorder(bt.root)   # 4 2 5 1 6 3 7
	print()
	bt.postorder(bt.root) # 4 5 2 6 7 3 1