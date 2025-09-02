# part1_pyqt5_basic.py
# pyQt5
# 현대적인 GUI 프로그래밍을 도와주는 라이브러리로
# 이미 많은 사람들이 사용하고 유용하다고 평가받은 프레임워크를
# 파이썬에서 사용할 수 있게 포팅한 버전이다.
# 현대적이고 세련된 UI를 꾸미고 여러 기능을 구현할 수 있지만
# 그만큼 배우기가 까다롭고 많은 기능을 모두 외우기가 힘들다.
# -> 학습곡선이 가파르다.
# pip install pyQt5
from PyQt5.QtWidgets import (
	QApplication,
	QWidget,
	QVBoxLayout,
	QHBoxLayout,
	QLineEdit
)
from PyQt5.QtWidgets import *

import sys # GUI 프로그램을 종료시킬 때 사용할 기본 라이브러리

# QWidget 클래스를 상속받아서 기본적인 메서드를 재정의하여 사용한다.
class MyFirstApp(QWidget):
	def __init__(self):
		# 부모 클래스의 생성자를 실행하는 부분
		super().__init__()
		self.initUI()

	# 프로그램이 실행되었을 때 프로그램의 제목이나 
	def initUI(self):
		# 프로그램의 제목을 설정
		self.setWindowTitle("이준상의 첫번째 pyQt5 프로그램")
		# 프로그램의 크기와 실행되는 위치 좌표 설정
		x, y, width, height = 0, 0, 300, 200
		# x는 화면상에서 왼쪽으로부터 오른쪽으로 이동한 거리를 말하며
		# y는 화면상에서 위에서부터 아래로 이동한 거리를 나타낸다.
		# 이때 기준은 메인 모니터 기준 좌상단 꼭짓점을 기준으로 한다.
		# width 가로 길이
		# height 세로 길이
		self.setGeometry(x, y, width, height)

		# 메인 레이아웃을 구성하는 내용을 작성한 메서드
		self.setMainLayout()

		# 해당 윈도우를 나타나게 하는 메서드
		self.show()

	# UI를 상단, 하단, 우측 세 개의 영역으로 나눠서 UI를 꾸며보자.
	# 1. 메인 레이아웃을 만들고 가로로 요소(위젯)를 배치한다.
	# 2. 메인 레이아웃 아래에 좌우 레이아웃을 만들고
	# 좌측 레이아웃은 세로로 배치하는 레이아웃으로 설정한다.
	# 1. 메인 레이아웃 만들기
	def setMainLayout(self):
		# 레이아웃 만들기
		self.mainlayout = QHBoxLayout()
		
		# 메인>좌측 레이아웃을 구성하는 메서드
		self.leftLayout = self.setLeftLayout()
		# 메인>우측 레이아웃을 구성하는 메서드
		self.rightLayout = self.setRightLayout()

		# 메인 레이아웃에 왼쪽과 오른쪽 자식 레이아웃을 추가
		self.mainlayout.addLayout(self.leftLayout)
		self.mainlayout.addLayout(self.rightLayout)
		# 윈도우 창에 메인 레이아웃 배치
		self.setLayout(self.mainlayout)


	def setLeftLayout(self):
		# 반환할 레이아웃
		# 이 안에 필요한 요소, 위젯들을 추가해서 반환해야 한다.
		leftLayout = QVBoxLayout()

		# 한 줄 입력 텍스트 박스
		self.input = QLineEdit()
		# 레이아웃에 해당 위젯 추가
		leftLayout.addWidget(self.input)

		return leftLayout
	
	def setRightLayout(self):
		# 레이아웃 생성
		rightLayout = QVBoxLayout()
		# 버튼 생성
		self.add_btn = QPushButton(text="클릭")
		# 생성된 버튼을 레이아웃에 추가
		rightLayout.addWidget(self.add_btn)

		return rightLayout

if __name__ == "__main__":
	# 프로그램 실행
	# QApplication을 시스템에 등록하여
	# 그 위에서 프로그램이 동작한다.
	app = QApplication(sys.argv)
	ex = MyFirstApp()
	sys.exit(app.exec_())


