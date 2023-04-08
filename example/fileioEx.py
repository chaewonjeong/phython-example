score_file = open("files\score.txt", "w", encoding="utf-8")

print("수학 : 80", file=score_file)
print("수학 : 80", file=score_file)
print("수학 : 80", file=score_file)
print("수학 : 80", file=score_file)
print("수학 : 80", file=score_file)
print("영어 : 60", file=score_file)
score_file.close()

# 작업 경로 확인하기
# import os
# print(os.getcwd())


# uphand
# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("\n과학 : 80")
# score_file.close()


# 파일 읽기
score_file = open("files\score.txt", "r", encoding="utf-8")
# print(score_file.read())

# 한 줄씩 읽기
# print(score_file.readline(), end="")
# print(score_file.readline())


# 입력파일의 라인이 몇줄인지 모를때
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")


# list에 값을 넣어서 출력
lines = score_file.readlines()  # list형태로 저장
for line in lines:
    print(line)
