# part8_sort_basic.py
# 지금까지 배운 기본 정렬 알고리즘 함수들을
# 이 파일로 import하여 실행시간을 측정해보자.
from part5_sort_basic_bubble import bubble_sort
from part6_sort_basic_selection import selection_sort
from part7_sort_basic_insertion import insertion_sort
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from day04.part3_sort_adv_quick import quick_sort
from day05.part1_sort_merge import merge_sort
from day05.part2_sort_heap import heap_sort

# 실행시간 측정을 위한 time 패키지 임포트
import time

# 전달된 함수에 arr 데이터를 전달해서 실행이 끝나기까지 걸리는 시간을 측정하는
# 함수
def timing(func, arr:list, name:str="no"):
	"""
	@param func: 실행할 내부함수
	@param arr: 내부함수에 전달할 정렬되지 않은 데이터
	@param name: 함수의 명칭을 출력할 때 사용할 문자열
	"""
	# 현재 시간을 저장할 변수
	start = time.time() # 현재 시간을 가져오는 함수
	# 전달받은 함수에 전달받은 데이터를 전달하여 실행
	func(arr, False)
	# 실행하는 데 걸린 시간을 측정
	end = time.time()
	# 끝난 시간으로부터 시작했던 시간을 빼면 걸린 시간이 나온다.
	print(f"{name} 함수\n\t걸린 시간: {(end-start):.2}")

if __name__ == "__main__":
	import random
	n = 900
	arr = list(range(n))
	random.shuffle(arr)

	timing(bubble_sort, arr, "bubble")
	timing(selection_sort, arr, "selection")
	timing(insertion_sort, arr, "insertion")
	timing(quick_sort, arr, "quick")
	timing(merge_sort, arr, "merge")
	timing(heap_sort, arr, "heap")
