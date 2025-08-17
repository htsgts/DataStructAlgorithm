# part3_sort_adv_quick.py
# 퀵 정렬(Quick sort) with Pivot
# 퀵 정렬은 분할정복 알고리즘을 바탕으로 만들어진 고급 정렬 알고리즘이다
# 분할정복 알고리즘을 기반으로 하기 때문에 재귀적으로 함수를 사용하는 것이 특징이다.
# 특히, 피벗(pivot)이라는 개념을 두어서 이를 기준으로 작은 값과 큰 값을 좌우로 분류하여
# 이를 재귀적으로 실행하는 것이 핵심적인 로직이다.
# 이 재귀실행에서 기본케이스는 길이가 1이하일 때 그 값을 그대로 보내는 것으로 한다.

def quick_sort(arr:list, show:bool=True):
	# 기본 케이스: arr의 길이가 1이하일 때, 그 값을 그대로 반환한다.
	if len(arr) <= 1:
		return arr
	
	# 피벗 선택
	# 0번째 요소를 피벗으로 선택
	pivot = arr[0]

	# pivot을 기준으로 하여 작은 값과 같은 값, 큰 값을 구분해 저장한다.
	left = [e for e in arr if e < pivot]
	mid = [e for e in arr if e == pivot]
	right = [e for e in arr if e > pivot]

	# 분할된 대상들에 대해서 mid를 제외하고 나머지를 재귀적으로 실행한다.
	# 이때, 왼쪽 리스트에 대해서 퀵 정렬이 실행된 것과 mid와 오른쪽 리스트를
	# 하나로 합쳐서 반환하면 최종적으로 정렬이 완료된 하나의 리스트가 반환된다.
	result = quick_sort(left, show) + mid + quick_sort(right, show)
	if show: print(result)
	return result

if __name__ == "__main__":
	import random # 요소를 섞기 위한 패키지 임포트
	arr = list(range(20)) # 데이터 만들기
	random.shuffle(arr) # 요소 섞기
	print(arr) # 섞은 데이터 출력
	result = quick_sort(arr) # 퀵 정렬
	print(result) # 정렬된 데이터 출력