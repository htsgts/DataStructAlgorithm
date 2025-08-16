# part7_sort_basic_insertion.py
# 삽입 정렬(Insertion Sort)
# 삽입 정렬은 정렬된 좌측 요소들과 정렬이 되지 않은 우측 요소들로 구분하여
# 정렬되지 않은 첫번째 요소를 정렬된 요소들 사이에 적절한 위치를 찾아서
# 인접한 값과 비교하여 교환하는 방식으로 위치를 찾아간다.
# 1. 제자리정렬: 추가적인 변수가 필요하지 않다.
# 2. 안정정렬: 같은 값끼리의 순서를 유지한다.

def insertion_sort(arr:list, show:bool=True):
	# 요소의 길이
	n = len(arr)
	# 순회
	# 0번째 요소는 이미 정렬된 값으로 취급하여 1번째 요소부터 정렬을 시작한다.
	for i in range(1, n): # 1로 시작
		key = arr[i] # 현재 삽입/정렬할 숫자를 임시로 저장
		# 현재 숫자의 이전 위치
		j = i-1
		while j >= 0 and key < arr[j]:
			# 이전 위치의 순서값이 0보다 크고(인덱스 오류 방지)
			# 삽입하려는 값이 이전 위치의 순서값보다 작은 동안
			# 기존 정렬되어 있던 key보다 큰 값들을
			# 반복적으로 오른쪽으로 이동
			arr[j+1] = arr[j]
			j -= 1 # 포커싱을 왼쪽으로 한칸 이동
			if show: print(arr)
		# key의 값이 j번째 값보다 작지 않으면 while문이 종료된다. -> 적절한 위치를 찾았다.
		# 혹은 j인덱스가 -1이면 종료된다. -> key가 가장 작은 값
		arr[j+1] = key
		if show:
			print("=" * 4)
			print(arr)
			print("=" * 4)
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
	arr = insertion_sort(arr)
	print("=" * 20)
	print(arr)