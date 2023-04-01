# 일반 유닛
class Unit:
    # __init__ : 생성자
    def __init__(self, name, hp):
        # 멤버변수 : 클래스 내에서 정의된 변수
        self.name = name
        self.hp = hp
        print("{0}유닛이 생성되었습니다.".format(self.name))


# 공격 유닛 : 일반 유닛을 상속받아서 만들어짐


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # 일반 유닛에서 만들어진 생성자를 호출해서 name과 hp를 정의
        Unit.__init__(self, name, hp)
        # 추가로 공격력을 정의
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


# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
