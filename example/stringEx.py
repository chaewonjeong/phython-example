python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java")) #비파괴적  변화

index = python.index("n")
print(index)

index = python.index("n", index + 1)  # index + 1 다음 위치 찾기
print(index)

print(python.find("Java"))  # 없다면 -1 반환
# print(python.index("Java"))   없다면 오류

print(python.count("n"))
