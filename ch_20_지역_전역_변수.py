# @Date       : 21.11.18(목) 13:01
# @Author     : ymkim
# @Contents   : 지역변수, 전역변수

# 군대
gun = 10
def checkpoint(solders) :
    global gun # 전역 공간에 있는 gun을 사용
    gun = gun - solders
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, solders) :
    gun = gun - solders
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))