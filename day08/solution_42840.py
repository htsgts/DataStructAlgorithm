# solution_42840.py
# 1번 수포자가 찍는 방식:
# 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식:
# 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식:
# 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은
# 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지
# 배열에 담아 return 하도록
# solution 함수를 작성해주세요.

# 제한 조건
# 가장 높은 점수를 받은 사람이 여럿일 경우,
# return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

def solution(answers):
    answer = []
    # 기본 구성 정보를 작성한다.
    # 방법은 생각나는대로 고르고, 코드를 작성하다가 
    # 만약에 문제를 푸는 데 적절하지 않은 방식이었다면
    # 다른 방법을 고민한다.
    supoza = [
        [1, 2, 3 , 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	]
    # 1. 문제를 어떻게 접근할지 고민하는 내용을 글로 작성해본다.
    # 2. 작성한 내용을 코드로 어떻게 번역할지 고민한다.
    # 3. 코드로 바꿨을 때 구분되는 부분을 줄 단위로 나눠서 문장을 구성한다.
    # 4. 나눠진 문장을 코드로 구현한다.
    # 정답여부를 각 수포자별로 담을 리스트 선언
    # 각 수포자가 맞힌 문제의 개수를 담을 것이다.
    results = [0, 0, 0]
    for i, e in enumerate(answers):
        # 주어진 정답을 가져올 때 그 인덱스를 수포자별 패턴의 길이만큼으로
        # 나누어서 나머지를 인덱스로 삼아 값이 같은지 비교한다.
        # 수포자별로 확인을 해야 하므로 이중반복문을 사용한다.
        for j, su in enumerate(supoza):
            namozi = i % len(su) # 각 수포자의 패턴 길이만큼으로 나눈 나머지만큼을
            # 인덱스로 삼는다.
            if e == su[namozi]:
                results[j] += 1
    # print(results) # [5, 0, 0]

    #for i, e in enumerate(results):
    #    if max(results) == e:
    #        answer.append(i+1)
    answer = [i+1 for i, e in enumerate(results) if max(results) == e]
    return answer

if __name__ == "__main__":
    answer1 = [1,2,3,4,5]
    answer2 = [1,3,2,4,2]
    result1 = solution(answer1)
    print(result1) # [1]
    result2 = solution(answer2)
    print(result2) # [1,2,3]