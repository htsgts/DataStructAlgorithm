# part4_stack_class.py
# stack 자료구조를 list를 활용하여 클래스로 구현하기
# .append를 통해서 데이터를 추가하고
# .pop(-1)을 통해서 마지막에 삽입된 데이터를 추출하는 방식으로 진행된다.

class Stack():
	def __init__(self, data=None):
		# 데이터는 리스트로 작성
		if data:
			self.datas = [data]
		else:
			self.datas = list()

	# 데이터 삽입. 이때 마지막 요소로 추가된다.
	def put(self, data):
		self.datas.append(data)
		return self

	# 데이터 추출. 이때 마지막으로 삽입된 요소가 반환된다.
	def get(self):
		# 마지막 요소를 pop(-1)로 반환하고
		return self.datas.pop(-1)
		# 남은 데이터는 마지막 요소가 사라진 데이터들일 것이다.
	
	# self에 해당하는 객체를 print() 했을 때 출력할 문자열 정의
	def __str__(self):
		return f"stack: {self.datas}"

if __name__ == "__main__":
	stack = Stack()
	stack.put(1)
	stack.put(2)
	stack.put(3)
	# 데이터 추출
	data = stack.get() # 3
	print(data)
	print("current: ", stack)

	# 중간에 데이터 삽입
	stack.put(4)

	# 데이터 추출 -> 마지막에 삽입된 4를 반환
	data = stack.get()
	print(f"data: {data}") # 4
	print("current: ", stack) # 1, 2