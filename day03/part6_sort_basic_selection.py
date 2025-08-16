# part6_sort_basic_selection.py
# 선택 정렬(selection sort)
# 선택 정렬이란, 전체 요소 중 가장 작은 값을 찾아서
# 정렬된 요소 바로 뒤의 요소와 교환하는 방식으로 정렬하는 알고리즘이다.

def selection_sort(arr:list, show:bool=True):
	# 전체 요소의 길이를 구한다.
	n = len(arr)
	# 전체 순회를 한다.
	for i in range(n):
		# 현재 인덱스를 최소값의 인덱스로 설정
		min_idx = i
		# i+1부터 끝까지 순회하며 최소값의 인덱스 찾기
		for j in range(i+1, n):
			# 만약에 j번째 요소의 값이 min_idx 요소의 값보다 작다면
			# min_idx의 값을 j로 바꾼다.
			if arr[j] < arr[min_idx]:
				min_idx = j
		# 내부 for문이 종료되면 가장 작은 값을 가진 요소의 인덱스값이
		# min_idx에 저장된다.

		# 가장 작은 값을 가진 요소의 값과 i번째 요소의 값을 교환
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
		# 교환이 일어난 뒤의 전체 요소를 출력
		if show: print(arr)
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
	arr = selection_sort(arr)
	print("=" * 20)
	print(arr)