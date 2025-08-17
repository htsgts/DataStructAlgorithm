# part1_linked_list.py
# 연결 리스트(Linked List)
# 연결 리스트는 요소의 역할을 하는 노드(Node)로 이루어져 있다.
# 이 노드는 데이터를 저장하는 변수와 다음 노드의 주소값을 저장하는 변수로 이루어져 있다.
# 이 노드에 대한 클래스와 해당 노드들을 요소로 삼는 링크드 리스트 클래스를 만들어보자.

# 노드 클래스
# data를 저장할 self.data
# 다음 노드 객체를 저장할 self.next
# 초기화할 때 데이터를 전달받아서 self.data에 저장하자.
class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next: Node = next # Node 객체를 담을 변수
	
	# 노드를 문자열로 출력하면 가진 데이터를 출력
	def __str__(self):
		return f"{self.data}"

# LinkedList 클래스
# 첫번째 노드를 담을 self.head 속성 필요
# 추가, 삭제, 순회, 탐색 등의 메서드가 필요하다
class LinkedList():
	def __init__(self, head:Node=None):
		self.head = head

	# 노드의 추가
	# 노드는 마지막 노드의 뒤에 새로운 노드를 추가해야 한다.
	# 즉, Node객체의 .next가 None이면
	# 해당 위치에 전달받은 새로운 데이터 혹은 노드를 대입하면 된다.
	# + 입력되는 데이터가 만약 노드 타입이면 있는 그대로 .next에 담아야 한다.
	def append(self, data):
		# refactoring)새로운 데이터를 검사하고 노드 타입으로 통일한 뒤 변수에 담아서 활용하자
		new_node:Node = data if isinstance(data, Node) else Node(data)
		# 만약 헤드 노드가 없으면 아무 노드도 없는 것이므로
		if not self.head:
			# 헤드노드에 새로운 데이터를 담은 노드를 저장한다.
			self.head = new_node
			# 데이터 노드 추가가 되었으므로 메서드 종료
			return
		# 헤드 노드가 있는 상태이므로
		# 헤드노드로부터 출발해야 한다.
		current = self.head
		# 현재 보고 있는 노드에 다음 노드가 있는 동안
		# 다음 노드를 current에 담기를 반복한다.
		# 언제까지? 다음 노드가 없을 때까지
		while current.next:
			current = current.next
		# while문을 탈출했다는 건, current.next가 없다는 이야기이다.
		# 즉, current.next에 새로운 데이터를 담은 노드를 저장하면 끝난다.
		current.next = new_node

	# 노드 삭제
	# 노드를 삭제할 때 해당 노드를 찾을 기준을 정해야 한다.
	# 일반적으로 지울 데이터값을 전달하여 해당 데이터를 가진 노드를 삭제하는 방식을 취한다.
	def delete(self, data):
		result = None # 반환할 노드
		# 헤드 노드가 없으면 None을 반환한다.
		if not self.head: return result
		# 만약 헤드노드의 데이터가 찾는 데이터라면
		if self.head.data == data:
			result = self.head
			# 헤드노드의 다음 노드를 헤드로 삼고
			self.head = self.head.next
			# 헤드 노드를 제거하고 반환한다.
			return result
		# 여기까지 왔다면 head도 존재하고 그 데이터도 전달받은 데이터랑 다르다는 의미이다.
		# 현재 확인하고 있는 노드를 담을 변수에 헤드노드의 다음 노드를 저장한다.
		prev = self.head
		current = self.head.next
		while current: # current 노드가 None이 아니라면 while문 입장
			if current.data == data:# 현재 보고 있는 노드의 데이터가 전달받은 데이터와 같다면
				# 다음 노드의 정보를 이전 노드의 next에 저장한다.
				# 이로써 current를 가리키는 노드가 없게 된다(제거)
				prev.next = current.next
				# 해당 데이터를 가진 노드(current)를 반환한다.
				return current
			# 만약 current의 데이터가 일치하지 않으면
			# 다음 노드를 확인해야 하므로 prev에는 current 노드가
			# current 노드에는 next 노드가 저장되어야 한다.
			# prev = current
			# current = current.next
			prev, current = current, current.next
		# 여기까지 왔다면 current가 None될 때까지 데이터를 못 찾은 것이다.
		# 찾고자 하는 데이터가 없다는 의미이다.
		return None # 데이터를 찾지 못함.

	# 데이터를 가진 노드 탐색
	def find(self, data):
		if not self.head: return None
		current = self.head
		while current:
			if current.data == data:
				return current
			current = current.next
		# 못 찾았다.
		return None

	# 모든 데이터를 리스트 형태로 담아서 반환하는 메서드
	def traversal(self)->list:
		if not self.head: return None
		# 반환할 리스트를 담은 변수
		result = list()

		# 데이터를 확인할 노드를 담을 변수
		current = self.head
		# 현재 노드가 None이 아니라면 데이터를 리스트에 담는다.
		while current:
			result.append(current.data)
			current = current.next
		# 여기까지 왔다는 건, 모든 데이터를 확인했다는 의미이다.
		return result
	
	# 모든 데이터를 "->"형태를 기준으로 나열하여 연결관계를 출력하는 메서드
	def display(self)->None:
		datas = self.traversal()
		# datas에 담긴 값은 숫자값이므로 join으로 연결할 수가 없다.
		# 때문에 모든 요소에 함수를 적용하는 map()함수를 사용해야 해
		# 문자열로 바꿔주어야 한다.
		datas_str = map(str, datas)
		# .join()함수는 해당 문자열을 구분자로 하여 여러 값을 연결해주는 함수다.
		print("->".join(datas_str))

if __name__ == "__main__":
	obj = LinkedList()
	obj.append(1)
	obj.append(2)
	obj.append(3)
	obj.append(4)
	obj.append(5)
	obj.delete(3) # 1->2->4->5
	current = obj.head
	# 데이터 순회하여 리스트로 반환
	datas = obj.traversal()
	print(datas)
	#while current:
	#	print(current.data, end="->")
	#	current = current.next
	#print("None")
	# 데이터 탐색
	found = obj.find(4)
	print("found data: ", found) # 4
	print("found next: ", found.next.data) # 4-> 5

	# display로 노드 간의 관계를 출력
	obj.display()