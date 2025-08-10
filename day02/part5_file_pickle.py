# part5_file_pickle.py
# 피클링(pickling)
# 피클링이란, 파이썬에서 다루는 변수, 함수, 클래스 객체 등
# 거의 대부분의 데이터를 바이너리 형식의 파일로 내보내서
# 다른 컴퓨터나 위치에서 파이썬에서 읽을 수 있는 형태로
# 읽어낼 수 있게 전달하는 패키징 방식이다.

# 피클 임포트
import pickle # 따로 설치할 필요가 없다.

def save_to_pickle(data, file_path:str,
                  mode:str='wb' # 바이너리 방식으로 쓰기
                  ):
  with open(file_path, mode) as file:
    # 피클링 방식으로 dump 해야 한다.
    pickle.dump(data, file)
  return file_path # 정상 저장시 파일 경로 반환

def load_from_pickle(file_path:str, mode:str='rb'):
  # 피클링된 파일로부터 객체를 언피클링하여
  # 파이썬 객체로 다룰 수 있게 바꾼다.
  with open(file_path, mode) as file:
    data = pickle.load(file)
  return data

import os
import sys
workspace_folder_path = os.path.dirname(os.path.dirname(__file__))
folder_path1 = os.path.join(workspace_folder_path, 'day01')
print(folder_path1)
# input()
sys.path.append(folder_path1) # 시스템 경로에 추가
from mudule_practice.person import Person
# 일부 경로를 직접 추가하는 경우, 파이썬에서
# 해당 경로를 제대로 인식하지 못할 수 있다.
# 하지만 코드는 정상적으로 동작한다.
print("문제없음")

if __name__ == "__main__":
  hong = Person("홍길동", 30, "일산동구")
  data = {
    '이름': "홍길동",
    "나이": 30,
    "성별": "M"
  }
  data = hong
  file_path = save_to_pickle(data, 'test.pkl')
  data = load_from_pickle(file_path)
  data.print_info()
