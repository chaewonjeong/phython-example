# 딕셔너리는 중괄호로 선언함
# 키: 값 형태를 쉼표(,)로 연결해서 만든다.
# 키는 문자열, 숫자, 불등으로 선언할 수 있다. 하지만 일반적으로 문자열로 선언한다.

# dict1 = {
#    "name": "어벤져스 엔드게임",
#    "type": "히어로 무비"
# }
#
# 딕셔너리 요소에 접근하기
# print(dict1)
#
# 딕셔너리 요소에 접근할 때는 리스트처럼 딕셔너리 뒤에 대괄호[]를 입력하고 내부에 인덱스처럼 키를 입력한다.
# 딕셔너리 선언은 중괄호{}, 요소 접근은 대괄호[]
#
# print(dict1["name"])
# print(dict1["type"])
#
#
# cabinet = {2: "유재석", 100: "김태호"}
#
# print(cabinet)
# print(cabinet.get(2))
#
# key가 사전에 있는지 학인하는 방법 in연산자 사용
#
# print(2 in cabinet)
# print(100 in cabinet)
# print(102 in cabinet)
# print(cabinet.get(2))


dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "피리핀"
}

key = input("접근하고자하는 키를 입력하시오>>")

if key in dictionary and key != "ingredient":
    print(dictionary[key])
elif key == "ingredient":
    idx = input("접근하고자 하는 인덱스를 입력하시오>>")
    print(dictionary["ingredient"][int(idx)])


dictionary["price"] = 5000

print(dictionary)
