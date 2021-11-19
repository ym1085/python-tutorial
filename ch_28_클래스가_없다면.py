# @Date       : 21.11.18(목) 15:24
# @Author     : ymkim
# @Contents   : 클래스 실습, 스타그래프트를 통해

'''
1. 파이썬 역시 자바와 마찬가지로 '객체지향 언어' 다
2. 자바에서의 클래스(Class)와 파이썬의 클래스(Class)의 차이점 숙지
'''

# 스타그래프트를 객체지향적으로 설계한 후에 프로그램 생성
# 마린 : 공격 유닛, 군인, 총을 쓸 수 있음

name = "마린"
hp = "40"
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

print()

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드가 있음

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage) :
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)