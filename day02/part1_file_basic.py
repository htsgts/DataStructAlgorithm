# part1_file_basic.py
# 파일 입출력 처리
# 파일을 읽어들이거나(read) 쓰기(write) 등의 동작을 하려면
# 파일의 경로를 이용하여 파일을 객체로 다뤄야 한다.
# 이때 사용하는 함수는 open(파일경로, 여는방식)으로
# 반환되는 파일 객체를 이용해 내용을 작성하거나 읽어올 수 있다.

# 1. 파일 쓰기
def write_file():
    # open을 이용해서 없는 파일명을 이용해 새로운 파일에 내용을 작성해보자.
    file = open("test.txt",
                'w'
                # 'a'
                )
    
	# 파일에 hello world를 입력하고 저장하자
    file.write("hello world\n반가워요")

	# 열었으면 닫아야 하므로 마지막에 file.close()를 먼저 작성해준다.
    file.close()

# 2. 파일 읽기
def read_file():
    # 파일은 r모드로 정확한 파일명을 이용하여 내용을 읽어오자.
    file = open("test.txt", 'r')
    
	# 파일을 읽어오는 메서드
    # 1. 전체 읽어오기
    # content = file.read()
    # print("content: \n", content)
    print("==========")
    
	# 2. 여러 줄을 이터러블 객체로 가져오기
    # 이 방법을 이용하면 한 줄씩 순차적으로 처리할 수 있다.
    lines = file.readlines()
    for i, line in enumerate(lines):
        print(f"{i+1}.{line}", end="")
	
	# 닫기는 기본
    file.close()

if __name__ == "__main__":
    write_file()
    read_file()