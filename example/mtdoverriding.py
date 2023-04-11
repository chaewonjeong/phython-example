# 메서드 오버로딩 : 부모 클래스에서 정의한 메서드 말고 자식클래스에서 정의한 메서드를 쓰고싶을때 메서드를 새롭게 정의해서 쓰고 싶을때
# 오버라이딩(overriding)이란 상속 관계에 있는 부모 클래스에서
# 이미 정의된 메소드를 자식 클래스에서 같은 시그니쳐를 갖는 메소드로 다시 정의하는 것이라고 할 수 있습니다.
# Unit class에서 정의된 move 메서드를 FlyableAttackUnit에서 재정의

# 일반 유닛
# 부모 클래스
class Unit:
    # __init__ : 생성자
    def __init__(self, name, hp, speed):
        # 멤버변수 : 클래스 내에서 정의된 변수
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))


# 공격 유닛 : 일반 유닛을 상속받아서 만들어짐
# 자식 클래스
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage,):
        # 일반 유닛에서 만들어진 생성자를 호출해서 name과 hp를 정의
        Unit.__init__(self, name, hp, speed)
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
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    # move 메서드에 대한 재정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)
print(vulture.speed)

# 배틀크루져 : 공중 유닛
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

battlecruiser.move("3시")
vulture.move("11시")
