# solution_12909.py
# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
# 입출력 예
# s	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false
# 입출력 예 설명
# 입출력 예 #1,2,3,4
# 문제의 예시와 같습니다.
def solution(s):
    answer = True
    # 케이스1 주어진 문자열의 길이가 홀수이면 애초에 개수가 안 맞는다.
    # 케이스2 주어진 문자열의 마지막 문자가 여는 괄호면 닫는 게 없으므로
    # -> False
    case1 = len(s) % 2 == 1
    case2 = s[-1] == "(" or s[0] == ")"
    if case1 or case2: return False
	# 여는 소괄호가 나오면 값을 1 증가시키고
    # 닫는 소괄호가 나오면 값을 1 감소시킨다.
    # 마지막에 남는 값이 0이면 정상,
    # 0이 아니라면 비정상
    count = 0
    
    for e in s:
        #if e == "(": count += 1
        #else: count -= 1
        count += 1 if e == "(" else -1
        # 만약 음수가 나온다면 여는 소괄호 없이 닫는 소괄호가 나온 것이므로
        # False를 return 한다.
        if count < 0: return False
    # count가 0이면 True
    # count가 0이 아니면 False -> not으로 부정
    answer = not count
    return answer

def solution_stack(s):
    stack = []
    for e in s:
        # 만약 닫는 소괄호가 나왔는데
        if e == ")":
            if stack: # 스택이 있다면 마지막 여는 소괄를 제거하고
                stack.pop(-1)
            else: # 스택이 비어있다면 여는소괄호가 없는 것이므로
                # False를 반환한다.
                return False
        elif e == "(":
            stack.append(e)
    # 반복문이 끝났을 때 모든 요소를 소모했어야 하는데
    # 스택이 남아있다면 짝이 안 맞는 것이므로 False를 반환한다.
    return not bool(stack)

answers = [
    "()()", 	# T
    "(())()",	# T
    ")()(", 	# F
    "(()("		# F
]
for e in answers:
	print(solution(e))
print("=" * 10)
print([True, True, False, False] == [solution(e) for e in answers])
print([True, True, False, False] == [solution_stack(e) for e in answers])
      