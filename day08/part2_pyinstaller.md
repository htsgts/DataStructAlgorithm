part2_pyinstaller.md
# 독립실행형 파일 생성
- 파이썬으로 작성한 코드를 파이썬이나 라이브러리 등의 설치 없이 코드를 어느 환경에서든 실행하고자 할 때 사용하는 방법이다.
- 설치방법
	`pip install pyinstaller`
- 실행방법
	`pyinstaller 
		--onefile # 하나의 파일로 압축하여 출력
		--noconsole # cmd창(터미널창)을 띄우지 않는 옵션
		--add-data "<원본경로>:<실행형파일기준경로>" # 필요한 이미지나 다른 파일을 같이 포함시키는 것
		--icon=<아이콘 파일 경로>
		<진입점코드파일.py> # 프로그램을 실행하는 메인 진입점(entry point)
		
	`
