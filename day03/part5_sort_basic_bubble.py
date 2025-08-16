# part5_sort_basic_bubble.py
# 정렬 알고리즘
# 다수의 데이터를 어떻게 정렬할 것인가를 코드로 로직을 작성하는 방법
# 기본 정렬 알고리즘은 3가지가 있다.
# 1. 버블 정렬
# 2. 선택 정렬
# 3. 삽입 정렬
# 이중에서 버블 정렬은 "인접한 요소끼리 비교하여 더 작은 값이 왼쪽으로 위치하도록"
# "두 값의 자리를 바꾸는 방식의 정렬"을 가리킨다.
# 특징:
# 1. 제자리 정렬
# 	- 현재 요소의 개수만큼 안에서만 교환이 이루어지기 때문에 추가적인 공간이 필요하지 않다.
# 2. 안정 정렬
# 	- 정렬 전의 순서를 정렬 후에도 유지한다.
def bubble_sort(arr:list, show:bool=True):
	# 용어 정리
	# path: 첫번째 요소부터 마지막 요소까지 한 바퀴를 도는 것을 패스라고 부른다.
	# 교환: 정렬을 위해서 두 요소의 위치(순서값)를 맞교환하여 바꾸는 것을 가리킨다.
	
	# 전체 요소의 개수를 구한다.
	n = len(arr)

	# 전체 요소를 순회하며 인접한 요소끼리 비교 후 서로 교환한다.
	for i in range(n): # 0부터 n-1까지의 숫자를 i에 담아 반복
		if show: print(f"{i+1}/{n}") # 현재횟수/전체횟수
		# 최적화, 조기 종료를 위한 swapped 변수 선언
		swapped = False
		# 각 패스마다 끝에서부터 i+1개의 원소는 이미 정렬되어 있다고 판단하여
		# n-(i+1)번째 요소까지만 비교한다.
		for j in range(0, n-(i+1)):
			# 인접한 두 요소(원소)를 비교하여 순서가 잘못되어 있으면
			# 서로 교환(swap)
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				# 교환이 일어났음을 표현하는 변수
				swapped = True
				if show: print(arr)
		
		# 이번 패스에 교환이 없었다면 swapped가 False를 유지할 것이다.
		# 그러면 모두 정렬되었다고 판단하고 조기종료
		if swapped is False:
			break
	return arr

if __name__ == "__main__":
	# 정렬 전 데이터 생성
	arr = list(range(10))
	# 섞기
	import random
	random.shuffle(arr)
	print(arr) # 정렬 전 리스트 출력
	print("=" * 20)
	# ========================
	arr = bubble_sort(arr)
	print("=" * 20)
	print(arr)