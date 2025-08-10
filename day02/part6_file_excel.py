# part6_file_excel.py
# 파이썬으로 엑셀파일 다루기
# pip install openpyxl pandas matplotlib
# 위 명령어를 터미널에 입력하여 필요한 패키지들을 다운로드 받자.
# openpyxl은 파이썬으로 엑셀을 다룰 수 있도록 도와주는 패키지다.
import openpyxl

# 엑셀은 workbook > sheet라는 단위로 나뉘어져 있다.
# 때문에 새로운 워크북을 만들어서 그 안의 시트를 직접 조작하는 방식으로 진행된다.
def write_to_xlsx():
  # 워크북 만들기
  wb = openpyxl.Workbook()
  # 워크북의 시트를 활성화한다.
  sheet = wb.active
  # 시트의 각 데이터에는 딕셔너리처럼 접근을 해야 한다.
  # 이때 키값(key)은 A1, B3와 같은 좌표방식으로 해당 셀을 가리킬 수 있다.
  # 데이터 입력
  sheet['A1'] = '이름'
  sheet['B1'] = '나이'
  sheet['A2'] = "홍길동"
  sheet['B2'] = 30
  # 엑셀에서 사용하는 함수나 기타 기능들을 문자열 형태로 전달하면
  # 사용할 수 있다.
  sheet['C1'] = '=A1' # 'A1에 있는 값을 표시해라'를 명령어로 적어놓은 것이다.

  # 해당 워크북을 특정 파일명으로 저장
  wb.save('test.xlsx')
  return wb

if __name__ == "__main__":
  obj = write_to_xlsx()
  sheet = obj.active
  # 데이터를 읽어올 때에는
  # sheet의 특정 셀에 접근하여
  # .value를 통해 해당 셀의 값을 받아올 수 있다.
  name = sheet['A2'].value
  print(name)