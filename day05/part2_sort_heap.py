# part2_sort_heap.py
# 힙정렬(Heap Sort)
# 힙 정렬은 힙 구조를 활용하여 정렬하는 정렬 알고리즘이다.
# 힙 구조란, 이진트리 상에 요소를 배치한 뒤,
# 부모노드와 자식노드를 비교하여 더 큰 값이 위에 위치하게 하는
# 힙속성을 만족하는 이진트리를 가리킨다.
# 힙속성을 만족하면 루트 노드는 전체 요소 중 가장 큰 값이 위치하게 된다.
# 이렇게 heapify가 완성되면 루트노드의 값을 마지막 요소와 교환한 뒤
# 힙 구조의 길이를 1 줄이면
# 정렬된 뒷부분의 요소를 배제하고 힙구조를 유지하게 된다.
# 이를 반복하면 뒷부분에 큰 값이 위치하는 정렬이 완성되게 된다.

# 힙 속성 유지를 위한 heapify 함수 구현
# 데이터 리스트arr와 힙 크기heap_size, 현재 노드의 인덱스를 매개변수로 받는다.
def heapify(arr:list, heap_size:int, current_index:int, show=True):
    # 현재 노드를 가장 큰 인덱스로 취급
    largest = current_index
    # 왼쪽 자식의 인덱스 계산(2i + 1)
    left_index = 2 * current_index + 1
    # 오른쪽 자식의 인덱스 계산(2i + 2)
    right_index = 2 * current_index + 2

    # 왼쪽 자식이 힙 크기 범위 내에 있고, 현재 largest보다 그 값이 큰 경우
    # 가장 큰 인덱스(largest)의 값을 왼쪽 노드의 인덱스로 바꿔준다.
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index
    # 오른쪽 노드에도 같은 방식으로 적용
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index
    # 두 조건문을 하나로 연결(elif)하지 않는 이유는
    # 왼쪽 자식이 largest보다 큰데, 오른쪽 자식이 왼쪽 자식보다도 큰 경우
    # 오른쪽 자식이 largest가 되어야 하기 때문에
    # 각각 독립적으로 largest와 비교되어야 한다.

    # largest의 인덱스가 current_index와 달라졌다면
    # 교환이 필요한 것이므로 교환을 진행한다.
    if show: print("large:", largest)
    if show: print("curr: ", current_index)
    if largest != current_index:
        if show: print("curr, largest:", arr[current_index], arr[largest])
        # 두 요소의 값을 교환
        arr[current_index], arr[largest] = arr[largest], arr[current_index]
        
        # 교환된 자식 노드에서 다시 heapify를 수행하여 최대 힙 속성 유지
        heapify(arr, heap_size, largest, show)
    if show: print("arr:", arr)

# 위의 힙구조화(heapify) 함수를 사용하기 위해서 힙정렬 함수를 작성해야 한다.
def heap_sort(arr:list, show:bool=True):
    # 데이터의 길이 추출
    length = len(arr)

    # 최대 힙 구성단계
    # 마지막 비단말노드(자식이 있는 노드)부터 시작하여 루트노드까지
    # heapify를 수행
    # 이때 마지막 비단말노드의 인덱스는 length//2 - 1
    # -> 마지막 요소의 부모 노드 인덱스가 곧 마지막 비단말노드의 인덱스이다.

    # 각 요소에 대해서 heapify를 진행
    for i in range(length//2-1, -1, -1):
        # 비단말노드 인덱스(length//2-1)부터 0번째 요소까지 
        # 역으로 거슬러 올라가야 하기 때문에 -1씩 증가한다.
        # 0번째 요소까지 진행하려면 stop을 -1로 설정해야 한다.
        heapify(arr, length, i, show=show)
    if show: print("first heap ", arr)
    # 정렬 단계
    # 힙에서 최대값(루트노드)를 하나씩 꺼내어 배열 끝부터 채움
    for i in range(length - 1, 0, -1):
        # 루트(최대값)를 현재 힙의 마지막 요소와 교환
        arr[0], arr[i] = arr[i], arr[0]
        # 루트 노드에 대해서 heapify를 수행하여 최대 힙 속성 복구
        heapify(arr, heap_size=i, current_index=0, show=show)
        if show: print(i, arr)
    # for문이 끝나는 것은 힙 구조의 길이가 1이 되는 순간일 것이다.
    # 즉, 가장 작은 값이 0번째 요소에 위치하는 순간 반복문은 종료된다.

    # 반환
    return arr

if __name__ == "__main__":
    import random 
    data = list(range(10))
    random.shuffle(data)
    print("origin: ", data)
    sorted_data = heap_sort(data)
    print("sorted:", sorted_data)