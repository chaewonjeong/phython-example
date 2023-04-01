# def profile(name, age, main_lang):
#    print("이름: {}\t나이: {}\t주사용언어:{}"
#          .format(name, age, main_lang))
#
#
# profile("유재석", 50, "python")
# profile("김태호", 45, "java")

def profile(name, age=18, main_lang="파이썬"):
    print("이름: {}\t나이: {}\t주사용언어:{}".format(name, age, main_lang))


profile("유재석")

# 키워드값 지정 가능
profile("김태호", main_lang="java", age=45)


# 가변인자
def profile_2(name, age, *language):
    # end=" " 문자열의 끝에 추가할 값
    print("이름: {}\t나이: {}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile_2("유재석", 50, "python", "c++", "java")
profile_2("김태호", 50, "python", "c++", "java", "javascript")
