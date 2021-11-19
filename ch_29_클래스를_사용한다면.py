# @Date       : 21.11.18(목) 15:34
# @Author     : ymkim
# @Contents   : 클래스를 사용하여 객체지향적 프로그래밍 진행

class Unit :
     
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

print()

# 레이스
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

print()

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 파이썬에서는 변수(맴버변수)를 추가해 사용이 가능하다

if wraith2.clocking == True :
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))