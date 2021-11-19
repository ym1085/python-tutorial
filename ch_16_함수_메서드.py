# @Date       : 21.11.18(목) 12:00
# @Author     : ymkim
# @Contents   : Function & Method, 전달값, 반환값

# 계좌 생성
def open_account() :
    print("새로운 계좌가 생성되었습니다.")

open_account()

print()

# 입금
def deposite(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

# 출금
def withdraw(balance, money) :
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

# 저녁에 출금 - 수수료가 붙는다
def withdraw_night(balance, money) :
    commission = 100 # 수수료 100원
    print(balance, money)
    return commission, balance - money - commission

balance = 0
balance = deposite(balance, 1000)
#balance = withdraw(balance, 500)

# print(balance)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


