import pickle

'''
pickle이란.
텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장하는 것,
raw text에 있는 내용을 프로그램을 돌릴 때 마다 파싱하여 필요한 부분을 뺀다면
비효율 적임, 그래서 미리 필요한 부분을 딕셔너리, 리스트, 튜플 이던 저장을 해놓는 것
근데 문자열이 아닌 객체를 파일에 쓸 수 없기에, pickle  모듈을 이용해 그 객체 자체를 바이너리로 저장하는 것이다.
'''

profile_file = open("files\profile.pickle", "wb")
profile = {"이름": "박명수", "나이": 20, "취미": ["축구", "골프", "야구"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("files\profile.pickle", "rb")
profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
