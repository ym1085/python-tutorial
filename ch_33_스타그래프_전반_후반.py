# @Date       : 21.11.18(목) 16:49
# @Author     : ymkim
# @Contents   : 스타그래프트 전반전

from random import *

# 일반 유닛 - Super Parent Class
class Unit :
     
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        print()

    def move(self, location) :
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}\n" \
            .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, speed, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

# 날 수 있는 기능을 가진 클래스
class Flyable :

    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed)) 

class FlyableAttackUnit(AttackUnit, Flyable) :

    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    # @Override : Java에서는 이런식으로
    def move(self, location) :
        self.fly(self.name, location)

# 마린
class Marine(AttackUnit) :

    def __init__(self) :
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 공격 속도 증가
    def stimpack(self) :
        if self.hp > 10 :
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else :
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit) :

    seize_developed = False # 시즈모드 개발여부

    def __init__(self) :
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self) :
        if Tank.seize_developed == False :
            return 
        
        # 현재 시즈모드가 아닐 떄 -> 시즈모드
        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드 일 때 -> 시즈모드 해제
        else :
            print("{0} : 시즈모드를 해제합니다".format(self.name))
            self.name /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit) :

    def __init__(self) :
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드

    def clocking(self) :
        if self.clocked == True :
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else :
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True

def game_start() :
    print("[알림] 새로운 게임을 시작합니다.")

def game_over() :
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 토장하셨습니다.")