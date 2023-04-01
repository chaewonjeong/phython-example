import pickle

# 따로 파일을 close해줄 필요가 없다.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


# 파일 쓰고 읽기를 간단하게 처리할 수 잇다.
with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())
