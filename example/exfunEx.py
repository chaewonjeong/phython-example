# list of python modules index 구글검색

# glob : 경로 내의 폴더/파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))


# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리 표시
# folder = "sample_dir"
# if os.path.exists(folder):
#    print("이미 존재하는 폴더입니다.")
#    os.removedirs(folder)
#    print(folder, "폴더를 삭제했습니다.")
# else:
#    os.mkdir(folder)
#    print(folder, "폴더를 생성하였습니다.")
# print(os.listdir()) #glob과 유사


# time : 시간 관련 함수
import time
import datetime

print(time.localtime())
print(time.strftime("%Y-%m-%d %H: %M"))
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)  # 100일 저장

print("우리가 만나지 100일은", today + td)
