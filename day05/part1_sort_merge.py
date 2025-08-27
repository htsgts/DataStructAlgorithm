# part1_sort_merge.py
# 병합 정렬(Merge Sort)
# 병합 정렬은 재귀 함수와 분할 정복 알고리즘을 활용하여
# 정렬하는 방법이다.
# 다만, 퀵 정렬과 다른 점은 pivot이라는 기준이 없는 것과
# 두 개의 리스트를 병합하는 그 방법이 따로 있다는 점이다.
# 그래서 함수를 두 가지로 나눠야 하는데
# 1. 전체를 분할하고 배치하는 merge_sort()
# 2. 배치된 두 리스트를 하나의 리스트로 병합하여 반환하는 merge()

# 병합 정렬
# 1. 재귀적으로 함수를 호출하기 때문에 기본케이스를 먼저 작성한다.
# 2. 리스트를 두 개로 쪼갠다.
# 3. 재귀적으로 함수를 호출한다
# 4. 각각 정렬된 좌우 리스트를 하나의 리스트로 병합하여 반환한다.
def merge_sort(arr:list, show:bool=True):
    # 리스트의 길이를 담을 변수
    length = len(arr)
    # 기본케이스
    # 만약 리스트의 길이가 1 이하라면 리스트를 그대로 반환한다.
    if length <= 1: return arr

    # 원본 리스트를 둘로 쪼갠다
    # 이때 인덱스 중 중앙값인 인덱스를 기준으로 좌우로 나눈다.
    left = arr[:length//2]
    right = arr[length//2:]

    # 쪼갠 좌우의 리스트를 재귀적으로 merge_sort를 호출하여
    # 다시 좌우에 담아준다.
    left = merge_sort(left, show)
    right = merge_sort(right, show)
    if show:
        print("left: ", left)
        print("right: ", right)

    # 좌우 리스트를 하나로 병합하면서 정렬하는 함수를 호출한다.
    # 병합 및 정렬된 새로운 리스트를 반환한다.
    return merge(left, right)

# 두 리스트를 전달받아서 각 요소를 비교한 다음
# 새로운 리스트에 추가하여 하나로 병합한 뒤 반환하는 함수
def merge(left:list, right:list):
    # 각각의 리스트는 이미 각자 안에서의 요소들이 모두 정렬된 상태라는
    # 가정 하에 진행된다.

    # 1. 두 개의 리스트는 이미 정렬된 상태이기 때문에 0번째 요소는
    # 각 리스트에서 가장 작은 값일 것이다.
    # 각 리스트의 요소를 가리킨 인덱스 값을 담을 변수를 선언해준다.
    left_index, right_index = 0, 0

    # 반환할 병합 리스트 변수를 만들어준다.
    result = [] # list()

    # 2. 두 리스트의 인덱스를 증가시켜가며
    # 각 리스트의 해당 요소끼리 크기를 비교하여 더 작은 값을
    # 새로운 병합 리스트에 추가시켜 나간다.
    # 언제까지? 두 리스트 중 하나라도 모든 요소를 다 소모하면.

    # 왼쪽 리스트의 인덱스가 왼쪽 리스트 요소 개수보다 작은 동안
    # 혹은 오른쪽에도 동일하게 적용
    # print("left length: ", len(left))
    # print("right length: ", len(right))
    # 둘 다 인덱스의 길이가 요소의 개수보다 많으면 안 되기 때문에
    # and로 조건식을 연결해주어야 한다.
    while left_index < len(left) and right_index < len(right):
        # print("left index:", left_index)
        # print("right index:", right_index)
        # 현재 인덱스 요소의 값을 서로 비교하여
        # 더 작은 값을 새로운 리스트에 추가(append)한 뒤
        # 더 작은 값이 속한 인덱스의 값을 1 증가시킨다

        # 각 리스트의 현재 보고 있는 요소를 변수에 담아준다.
        left_value = left[left_index]
        right_value = right[right_index]

        # 두 값을 비교하여 더 작은 값을 새로운 리스트에 담아준다.
        if left_value <= right_value:
            # 왼쪽 리스트 요소의 값이 더 작으므로 리스트에 담아준다.
            result.append(left_value)
            # 왼쪽 리스트의 요소를 추출했으므로 다음 요소를 보기 위해
            # 인덱스를 증가시킨다.
            left_index += 1
        else: # left_value > right_value
            result.append(right_value)
            right_index += 1
    # 여기까지 왔다는 건, while문을 탈출했다는 것이다.
    # 두 리스트 중 하나라도 모든 요소를 소모했다는 것이다.
    # 그러면 미처 담지 못한 요소들(남은 요소)을 result 리스트에 추가해야 한다.
    # 남은 리스트 요소를 result에 요소 하나씩으로 추가하려면
    # extend를 사용해야 한다.
    # 그런데 어느 쪽이 요소가 남았는지 알 수 없으므로,
    # 두 경우 모두 실행한다.
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

if __name__ == "__main__":
    import random
    data = list(range(30))
    random.shuffle(data)
    print(data)
    sorted_data = merge_sort(data, False)
    print(sorted_data)