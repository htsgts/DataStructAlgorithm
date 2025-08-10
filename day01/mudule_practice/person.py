# person.py

# 사람에 대한 클래스 작성
# 다른 파일에서 이 파일의 클래스를 가져다가 사용
class Person:
	def __init__(self, name: str, age: int, address: str=None):
		self.name = name
		self.age = age
		self.address = address
	
	def print_info(self):
		print(f"이름: {self.name}\n나이: {self.age}")
		# 주소값을 입력한 적이 있으면
		# None이 아닐 것이므로 실행된다.
		if self.address: print(f"주소: {self.address}")

path = "C:/"


if __name__ == "__main__":
	hong = Person("홍길동", 30) # 주소 입력 안함
	# print_info()를 hong에서 사용하면
	# 주소를 제외한 정보가 출력된다.
	hong.print_info()
	hong.address = "일산동구"
	hong.print_info()