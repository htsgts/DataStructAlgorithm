# part3_file_csv.py
# csv 파일로의 입출력
# csv란, 쉼표(,)로 구분된 데이터를 나열하여
# 표처럼 표현하는 데이터 전송 형식 중 하나다.
# 이러한 csv 파일을 읽고 쓰려면 기본적으로 제공되는
# csv 패키지를 import해야 한다.
import csv

def write_to_csv(mode:str='w'):
  file_name = 'test.csv'
  # csv 파일을 엑셀로 읽고 쓰려면 utf-8-sig 인코딩으로 읽고 쓰기를 해야 한다.
  # 일반적인 다른 인코딩 방식으로 읽기/쓰기를 하는 경우
  # 한글이 깨져 보일 수 있다.
  with open(file_name, mode, encoding='utf-8-sig',
            newline="" # csv에 새로운 row 쓰기 후 줄바꿈을 넣지 않는 옵션
            ) as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['이름', '나이', '성별', '성인여부'])
    csv_writer.writerow(['홍길동', 30, 'M', True])
    csv_writer.writerow(['홍당무', 10, 'F', False])

# csv 파일 읽기
# 읽기를 할 때에는 csv파일을 쓸 때 사용했던 인코딩 방식으로
# 읽기를 해야 내용이 깨지지 않는다.
def read_csv_file(
    file_name:str, 
    mode:str='r', 
    encoding:str='utf-8-sig'
  ):
  with open(file_name, mode, encoding=encoding) as file:
    csv_reader = csv.reader(file)
    lines = list(csv_reader)
    for row in lines:
      print(row)

if __name__ == "__main__":
  # write_to_csv()
  read_csv_file("test.csv")
  pass