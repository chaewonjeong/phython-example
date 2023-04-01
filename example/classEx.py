# 마린 : 공격 유닛, 군인, 총을 쏨
# name = "마린"
# hp = 40
# damage = 5
#
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(
#         name, location, damage))
#
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#


class Unit:
    # __init__ : 생성자
    def __init__(self, name, hp, damage):
        # 멤버변수 : 클래스 내에서 정의된 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


class AttackUnit:
    # self 는 자기 자신을 의미한다.
    # 클래스내에서 메서드 앞에는 항상 써준다.
    # self를 통해서 자기 자신에게 접근하는것
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # location 은 self없이 사용 -> 전달받은 값을 사용한다는 뜻
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입없습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
marine3 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


# 레이스 : 공중 유닛, 비생기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))


# 마인드 컨트롤 : 상대방의 유닛을 내 것으로 만드는 것
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True  # phyton 에서는 생성된 객체에 추가로 변수를 외부에서 만들어서 쓸 수 있다.

if wraith2.clocking == True:
    print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))

# 내가 선언하지 않은 변수는 당연히 안됨
# if wraith1.clocking == True:
#     print("{0}은 현재 클로킹 상태입니다.".format(wraith1.name))


# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
