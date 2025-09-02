# part3_GUI_tkinter.py
# GUI(Graphical User Interface)
# GUI는 사용자와 마우스, 키보드 등의 여러 기기를 통해서
# 상호작용할 수 있는 그래픽적인 UI를 제공하는 것을 가리킨다.
# 단순히 텍스트와 명령어를 키보드 입력을 통해서 상호작용하는
# CLI와는 반대되는 개념이라고 할 수 있다.

# 파이썬에서는 기본GUI 라이브러리로 tkinter를 제공한다.
# tkinter는 기본적으로 설치되어 있기 때문에 버전이나 의존성관리가 필요없어서
# 빠른 개발, 간단한 개발과 프로토타이핑에 특화되어 있다.
import tkinter as tk
from tkinter import messagebox as msgbox

# GUI에서 모든 내용은 Window라는 최상위 객체에서 시작한다.
# 이때, window 중에서도 처음으로 나오고 메인으로 작용하는 윈도우를
# root라고 부른다.
# window -> frame -> widget

# 메인 윈도우 root 생성
root = tk.Tk() # 메인 창을 다루는 클래스의 객체화

# 메인 창의 제목 세팅
root.title("Tkinter 첫번째 프로그램")

# 메인 창의 창 크기 초기 세팅
width, height = 640, 320
root.geometry(f"{width}x{height}")

# 위젯(widget)
# 위젯이란, 구조적인 형태를 잡는 것이 아니라
# 텍스트를 보여주거나 기능적인 동작을 수행하는 요소들을 가리킨다.

# 라벨 위젯(Label)
# 전달된 텍스트를 단순히 보여주기 위해 배치하는 요소이다.
label = tk.Label(
	root, # 해당 라벨이 배치될 상위 요소
	text="라벨로 작성한 텍스트", # text=해당 라벨에 표시할 문자열
	font=("Arial", 14) # 폰트 종류와 크기를 튜플로 전달한다.
)
# 위젯은 만든 걸로 끝나는 것이 아니라, 배치방식와 위치를 결정해주어야 한다
# .pack()
label.pack()
# pack 방식뿐만 아니라, grid 방식도 존재한다.
# .grid()
# 정해진 좌표 값을 넣으면 해당 위치에 배치되는 방식이다.

# 간단한 버튼 위젯 추가하기
# 버튼을 동작시켰을 때 실행할 동작을 미리 정의해두자.
def button_click():
	# entry 텍스트 박스에 작성한 내용을 문자열로 받아와서
	var = entry.get()

	# 출력 여부를 결정하는 변수 가져오기
	is_display = check_var.get()

	# 남성/여성 선택지의 숫자값을 받아와서 원하는 메시지를 띄울 수 있다.
	choice = btn_variable.get()
	gender = "남성" if choice == 0 else "여성"

	# 출력 내용에 추가한다.
	if is_display: msgbox.showinfo(title="환영",
						message=f"{var}환영합니다.\
						 버튼 클릭 완료\n성별: {gender}",)

# 버튼 만들기
button = tk.Button(root, text="클릭", command=button_click,
				   bg="lightblue")
button.pack()

# 입력박스 만들기
# entry 엔트리 위젯은 텍스트를 입력하기 위한 공간을 제공한다.
entry = tk.Entry(root, width=20)
entry.pack()

# 체크박스 버튼
# 연결된 요소끼리 다중선택을 가능하게 하는 버튼의 한 종류다.
# 이 체크박스의 상태값은 체크를 했냐(T), 안했냐(F) 둘 중 하나의 값을 가진다.
# 이 값을 프로그램 내에서 공유하고 활용하려면 그 값을 담을 변수가 필요하다.
check_var = tk.BooleanVar()
# 체크박스 생성. 체크박스의 상태값을 저장할 BooleanVar 변수를 같이 전달하여
# 상태값을 접근할 때 해당 변수를 통해서 할 수 있다.
# 설명: root 윈도우 안에 알림받기라는 텍스트가 적힌 체크 박스를 만드는데,
# 체크 여부의 상태값은 전달받은 check_var를 통해서 접근할 수 있다.
checkBox = tk.Checkbutton(root, text="알림 받기", variable=check_var)
checkBox.pack()

# 라디오버튼
# 여러 선택지가 있을 때 이중 하나만 고르도록 강제하는 버튼을 의미한다.
# 다수의 선택지를 써야 하므로 라디오 버튼은 하나만 있으면 안 된다.
# 또, 해당 버튼을 눌렀을 때 변화하는 값을 다른 변수에 저장하여 사용해야 하므로
# 해당 변수 또한 필요하다.

# 라디오 버튼 변수 
btn_variable = tk.IntVar() # 숫자 값을 담을 tk 변수

radioBtn_1 = tk.Radiobutton(root, text="남성", variable=btn_variable,
							value=0,
							)
radioBtn_2 = tk.Radiobutton(root, text="여성",
							variable=btn_variable,
							value=1,
							)
radioBtn_1.pack()
radioBtn_2.pack()


# 메인 루프 실행
# GUI프로그램은 사용자의 입력을 대기하여 입력을 받았을 때
# 그 입력에 따른 명령어를 수행하는 역할을 한다.
# 즉, 언제 입력이 있을지 모르고, 몇 번의 입력이 이루어진 뒤에 종료할지 모른다.
# 때문에 자체적으로 while문 안에 무한 루프되어 무한히 대기 -> 입력 -> 실행 -> 대기
# 루틴을 그리게 된다.
# 종료 버튼을 누르기 전까지는 무한히 루틴이 반복된다.
root.mainloop()