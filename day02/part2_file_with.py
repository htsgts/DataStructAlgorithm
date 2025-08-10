# part2_file_with.py
# with문을 사용한 파일 처리
# 파일을 읽거나 쓰려면 open을 이용해서 열고
# close로 닫아주어야 했다.
# 이를 자동으로 도와주는 with문이 있는데
# with문을 이용하면 신경써서 close()를 해줄 필요가 없어진다.

# 파일 쓰기
def read_file(file_name:str, mode:str='w'):
  # with open() as 파일객체명
  # 위와 같은 with문의 형식을 사용하면
  # 따로 close()를 사용할 필요없이 
  # 파일의 입출력 처리를 한 뒤 자동으로 닫힌다.
  with open(file_name, mode) as file:
    lines = file.readlines()
  for i, line in enumerate(lines):
    print(f"{i+1}. {line}", end="")

if __name__ == "__main__":
  read_file("test.txt", 'r')