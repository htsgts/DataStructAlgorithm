# part3_sort_merge_class.py
# 병합 정렬 클래스
# 병합 정렬은 두 가지의 함수 외에도 여러 유틸성 기능들이 많이 필요하다
# 때문에 클래스로 구현을 하면 복잡한 내용도 체계적으로 구현할 수 있다.

# 최대힙 클래스
# 최대힙 클래스는 데이터를 삽입했을 때 자동으로 heapify가 동작하여 
# 최대힙 속성을 유지하도록 동작해야 한다.

class Max_heap():
	def __init__(self):
		# 데이터를 담을 힙 리스트
		self.heap = []
	
	# 인덱스를 전달했을 때, 부모 노드의 인덱스를 반환
	def parent(self, i):
		return (i-1) // 2
	
	# 인덱스를 전달했을 때 왼쪽 자식 인덱스를 반환
	def left(self, i):
		return 2 * i + 1

	# 인덱스를 전달했을 때 오른쪽 자식 인덱스를 반환
	def right(self, i):
		# return self.left(i) + 1
		return 2 * i + 2
	
	# 부모 노드가 있는지(루트 노드 여부)를 반환
	def has_parent(self, i):
		return self.parent(i) >= 0
	# 왼쪽 자식 노드가 있는지 여부를 확인
	def has_left(self, i):
		return self.left(i) >= 0
	# 오른쪽 자식 노드가 있는지 여부를 확인
	def has_right(self, i):
		return self.right(i) >= 0
	
	# 삽입과 삭제를 하면서 내부적으로 최대힙속성을 유지하는 로직이 포함된다.
	# 데이터 삽입 연산
	def insert(self, value):
		# 1. 배열 끝에 요소 추가
		self.heap.append(value)

		# 2. 힙 속성을 만족할 때까지 heapify 수행
		# 새로운 요소가 추가된 현재 힙트리의 길이를 기준으로
		# heapify를 진행
		# 이 heapify 메서드는 클래스 내부에서만 호출하는 함수이기 때문에
		# 메서드명 앞에 언더바_를 하나 붙여준다.
		self._heapify_up(len(self.heap)-1)

	def _heapify_up(self, index:int):
		# 전달받은 인덱스로부터 heapify를 수행한다.
		# 이때 부모가 존재하고, 현재 값이 부모의 값보다 클 때
		if self.has_parent(index) and\
			self.heap[index] > self.heap[self.parent(index)]:
			# 부모노드의 인덱스 추출
			parent_index = self.parent(index)
			# 부모 노드와 자식 노드의 값을 맞교환
			self.heap[index], self.heap[parent_index] =\
				self.heap[parent_index], self.heap[index]
			# 재귀적으로 heapify를 수행
			self._heapify_up(parent_index)

	# 데이터 삭제 연산
	# 1. 가장 큰 값을 추출하고 전체 힙에서 제거
	def extract_max(self):
		# 만약에 self.heap의 길이가 0이라면, 데이터가 없으므로 None을 반환
		if len(self.heap) == 0: return None

		# 1. 루트 노드의 값 저장
		max_value = self.heap[0]
		# 2. 마지막 요소를 루트로 이동
		self.heap[0] = self.heap[-1]
		# 마지막 요소를 제거
		self.heap.pop()

		# 3. 힙 속성을 만족할 때까지 하향 조정
		if len(self.heap) > 0:
			self._heapify_down(0)
		
		return max_value

	# 2. 하향식 heapify
	def _heapify_down(self, index):
		# 전달받은 인덱스를 가장 큰 값으로 초기화
		largest = index
		# 왼쪽 자식과 비교
		print(index)
		if self.has_left(index):
			if self.heap[self.left(index)] > self.heap[index]:
				largest = self.left(index)

		# 오른쪽 자식과 비교
		if self.has_right(index):
			if self.heap[self.right(index)] > self.heap[index]:
				largest = self.right(index)
		
		# 가장 큰 인덱스가 기존의 index와 달라졌다면
		if largest != index:
			# 가장 큰 값을 가진 인덱스의 값과
			# 현재 노드(루트 노드)의 값을 교환
			self.heap[index], self.heap[largest] =\
				self.heap[largest], self.heap[index]
			# 재귀적으로 하향 조정
			self._heapify_down(largest)

if __name__ == "__main__":
	heap = Max_heap()
	data = [1, 3, 2, 5, 1]
	# [heap.insert(e) for e in data]
	for e in data:
		heap.insert(e)
		print(heap.heap)
	data = [3, 5, 1, 8, 9]
	for e in data:
		heap.insert(e)
		print(heap.heap)
	# 최대값만 추출하여 리스트에 0번째에 insert를 하면
	# 정렬된 리스트가 나온다.
	result = []
	for i in range(len(heap.heap)):
		result.insert(heap.extract_max())
	print("result:", result)
		