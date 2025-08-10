# part2_iter_enumerate.py
# 반복문 for에서 요소를 가져올 때 인덱스값도 가져오고 싶다면
# enumerate()에 이터러블 객체를 전달하면
# 인덱스i와 요소e를 동시에 가져올 수 있다(set타입 형태로 반환)

my_list = ["홍길동", "이", "김", "즙"]

# for문을 이용해서 요소 가져오기
for e in my_list:
  print(e)
# enumerate() 사용하기
for i, e in enumerate(my_list):
  print(f"i: {i}\t e: {e}")
  print(f"my_list[{i}]: {my_list[i]}")

for e in enumerate(my_list):
  print(e)