# part2_stack_basic.py
# Stack 자료구조
# stack은 이름 그대로 '데이터를 쌓아나가는 방식'을 자료구조로 표현한 것을 가리킨다.
# 먼저 들어온 데이터가 아래에 깔리기 때문에
# 나중에 들어온 데이터가 먼저 나가는 방식(LIFO)이다.
# 리스트에서 구현할 때에는
# 데이터 추가는 append, 데이터 추출은 pop(-1)로 구현할 수 있다.

def stack():
	# 기본 데이터 저장 구조는 리스트를 사용한다.
	stack = list()
	# 데이터 추가
	stack.append("함수1")
	stack.append("함수2")
	stack.append("함수3")
	# 함수3 완료
	func = stack.pop(-1)
	print(func)
	print("stack: ", stack)

	# 함수4 실행
	stack.append("함수4")
	print("stack: ", stack)

	# 함수2 완료
	func = stack.pop(-1)
	print(func)
	print("stack: ", stack)
	# 함수1 완료
	func = stack.pop(-1)
	print(func)
	print("stack: ", stack)

if __name__ == "__main__":
	stack()
	pass
