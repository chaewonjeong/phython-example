# 일반 유닛
# 부모 클래스
class Unit:
    # __init__ : 생성자
    def __init__(self, name, hp):
        # 멤버변수 : 클래스 내에서 정의된 변수
        self.name = name
        self.hp = hp
        print("{0}유닛이 생성되었습니다.".format(self.name))


# 공격 유닛 : 일반 유닛을 상속받아서 만들어짐
# 자식 클래스
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


# 다중 상속
# 부모클래스를 2개이상 상속받는것
# 공중유닛
# 드랍쉽 : 공중 유닛, 수송기, 공격불가능

# 날 수 있는 기능을 가진 클래스
class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "5시")
