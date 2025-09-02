# part1_gmail.py
# 파이썬을 이용하여 SMTP를 알고 그 라이브러리로 
# Gmail을 보낼 수 있다.
# SMTP(Simple Mail Transfer Protocol)
# 간단하게 이메일을 보낼 수 있도록 정해놓은 전달 규칙(프로토콜)
# 라이브러리 smtplib가 필요하다
import smtplib # 파이썬에서 기본으로 설치되기 때문에
# 추가적인 설치는 필요없다
# smtp는 메일을 보내기 위한 로켓, 발사대에 불과할 뿐이고
# 실제로 보내야 하는 내용은 mail을 통해 작성하고 탑재(payload)되어야 한다.

# email 라이브러리도 기본 설치이다
# 제목과 본문을 포함한 텍스트를 전달하기 위한 컨테이너
from email.mime.text import MIMEText

# Multipart란, 첨부파일을 의미한다.
from email.mime.multipart import MIMEMultipart

# 이러한 .env 파일의 환경변수 정보는 python-dotenv 라이브러리로
# 쉽게 사용할 수 있다.

# 환경변수(os)에 .env에 담겨 있는 환경변수 정보를 일괄적으로 등록시켜주는
# 함수다.
from dotenv import load_dotenv 

# load_dotenv를 통해서 등록된 환경변수를 불러오려면
# os 라이브러리를 통해서 가져와야 한다.
import os
load_dotenv() # .env 환경변수 로드. 따로 경로를 입력하지 않았다면
# 해당 프로젝트에서 .env 파일을 자동으로 찾아서 세팅한다.
# 만약 특정 경로에 있는 특정 env 파일을 로드하고 싶다면\
# 절대경로(C:/...) 혹은 현재 프로젝트를 기준으로 하는 상대 경로를 작성해주면 된다.
# load_dotenv("day07/dev.env") # .env 환경변수 로드

# 해당되는 키값에 담긴 값을 가져오는 코드
SENDER = os.getenv("SENDER")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# 이메일 전송을 위한 함수
# 필요한 정보(매개변수)
# - 보내는 사람의 이메일: str
# - 받는 사람의 이메일: str
# - 보내는 사람의 이메일에 접근할 수 있는 비밀번호(app password): str
# - 내용/제목: str
# - 내용/본문: str
def send_email(sender_email:str, 
			receiver_email:str, 
			password:str,
			subject:str,
			body_text:str
			):
	# 보내는 이메일, 받는 이메일, 제목 등 전체적인 구조 정보를 구성하는
	# MINEMultipart 객체에 해당 정보들을 담아준다.
	msg = MIMEMultipart()
	# msg["From"], msg["To"], msg["Subject"] = \
	#	sender_email, receiver_email, subject
	msg["From"] = sender_email
	msg["To"] = receiver_email
	msg["Subject"] = subject

	# 이메일 본문을 일반 텍스트(plain text) 형태로 부착(attach)
	msg.attach(MIMEText(body_text, "plain"))

	# Google의 SMTP 서버에 접속하여 보내는 이메일로 로그인한 뒤
	# app password로 로그인하여 이메일을 보내야 한다.
	# 이때, 로그인 실패, 전송 실패 등의 오류가 발생할 수 있으므로
	# 예외처리코드를 작성해야 한다.
	try:
		# Gmail SMTP 서버에 접속하기 위한 smtp 주소와 그 포트를 입력해주어야 한다.
		# 이 smtp 주소와 포트는 유명한 포털 사이트는 공개되어 있으므로
		# 해당 되는 주소와 포트를 사용하면 된다.
		# 보내는 사람이 속한 smtp 서버
		smtp_gmail = "smtp.gmail.com"
		# 전송을 위한 포트 번호
		smtp_port = 587
		server = smtplib.SMTP(smtp_gmail, smtp_port)
		# 해당 서버에 보안접속을 해야 한다.
		server.starttls() # TSL(Tranport Layer Security)
		
		# Gmail 계정으로 app password를 입력하여 로그인
		server.login(sender_email, password)

		# 이메일을 문자열로 변환하고 전송
		text = msg.as_string() # 문자열로 변환
		server.sendmail(sender_email, receiver_email, text)
		# ==== 여기까지 오류없이 왔으면 메일 전송이 완료된 것이다.
		print("이메일이 성공적으로 전송되었습니다.")
		print(f"보낸 사람: {sender_email}\n받는 사람: {receiver_email}")
	except Exception as e: # 만약 전송 작업 도중 오류가 발생한다면
		print(f"에러 발생: {e}")
	finally: # 전송 여부와 무관하게
		# 항상 smtp 서버 연결을 끊어주어야 한다.
		# 서버 연결 종료
		server.quit()

if __name__ == "__main__":
	sender = "miraclelee0613@gmail.com"
	receiver = "jslee7518@gmail.com"
	app_password = "bfzk zuql rpve kmwf"
	subject = "test1" # 제목
	body_text = "test1 내용" # 내용

	print(f"sender: {SENDER}")
	input("Enter to continue")
	send_email(sender, 
			receiver, 
			app_password,
			subject,
			body_text
			)