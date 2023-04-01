import sys

print("phyton", "java", sep=",", end="?")
# sep
# end : 문장의 끝글자르 바꾸기, 기본은 줄바꿈 문자
print("무엇이 더 재밌을까요?")

# log 처리시
print("phyton", "java", file=sys.stdout)
# 표준 출력으로 처리

print("phyton", "java", file=sys.stderr)
# 에러로 처리


# 출력 포멧
scores = {"수학": 0, "영어": 50, "코딩": 100}  # 딕셔너리
# .items() : key, value 짝으로 출력
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4))
    # ljust(8) : 8칸을 확보하고 왼쪽 정렬
    # rjust(4) : 4칸을 확보하고 오른쪽 정렬
    # str(score) : score는 int형이니 형변환후 rjust


# 은행 대기순번표
# 001, 002, 003
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))


# 표준 입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
# input으로 값을 받게 되면 항상 문자(str)로 저장된다.
print("입력하신 값은 " + answer + "입니다.")
