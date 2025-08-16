# part3_queue_class.py
# 클래스와 list 자료구조를 이용하여 Queue 구현하기
# 내부적으로 데이터는 list에 담아서 관리하며
# 클래스의 역할은 데이터를 삽입하고 제거할 때
# 어떤 데이터를 삽입/제거할지를 결정하는 역할만 한다.

# 클래스 만들기
class Queue():
	def __init__(self, data=None):
		# 만약에 전달받은 초기데이터가 있다면 리스트에 담고 생성
		# 없으면 빈 리스트 생성하여 self.datas에 담기
		if data:
			self.datas = [data]
		else:
			self.datas = list()
	
	# 데이터 삽입(마지막에 데이터 추가)
	def enqueue(self, data):
		# 전달받은 데이터를 self.datas의 마지막 요소로 추가
		self.datas.append(data)
		# chaining 기법을 위한 self 반환
		return self

	# 데이터 추출(먼저 들어온 데이터를 제거)
	def dequeue(self):
		return self.datas.pop(0)

	def __str__(self):
		return f"queue: {self.datas}"

if __name__ == "__main__":
	# 객체화
	que = Queue()
	# 데이터 추가
	# 백슬래시\는 해당 코드 줄이 아직 안 끝났음을 의미한다.
	que.enqueue(1)\
	.enqueue(2).enqueue(3)
	# 데이터 제거 및 확인
	data = que.dequeue()
	print(data) # 1
	print(que)  # queue: [2, 3]