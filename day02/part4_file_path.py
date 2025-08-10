# part4_file_path.py
# 파일의 상대경로(relative path)와 절대경로(abs path)
# 상대경로란, 현재 작업위치(wd)를 기준으로 경로를 작성하는 것이고
# 절대경로란, 드라이브 문자를 시작점으로 하여 파일의 경로를
# 작성하는 방식이다.

def write_file():
  # 상대경로에서 마침표.는 현재 위치를 가리키는 기호이다.
  # ./는 '현재 폴더 안의'라는 의미를 가진다.
  with open("./day02/test1.txt", 'w') as file:
    # 상대경로, 절대경로 무관하게, 존재하지 않는 폴더 안의 파일을
    # 대상으로 삼으면 오류가 발생한다.
    file.write("test")

def write_file_abs():
  # 절대경로로 파일을 지정하는 방법
  # 절대경로로 파일을 지정하려면 드라이브문자(C, D)로 경로를 시작하면 된다.
  with open("C:/test2.txt", 'w') as file:
    file.write("test")

if __name__ == "__main__":
  # write_file()
  write_file_abs()
  pass