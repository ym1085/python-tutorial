# @Date       : 21.11.17(수) 22:22
# @Author     : ymkim
# @Contents   : For문 실습

'''
For문
1. 대기번호가 1 - 1000000000인 경우, 다 찍어줄 것인가
'''

# 일반 for문
for wasting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(wasting_no))

print()

# range 활용
# range(N ~ N-1)
# for wasting_no in range(1, 100): 
for wasting_no in range(1, 10):
    print("대기번호 : {0}".format(wasting_no))

print()

# 2:09:27 - https://www.youtube.com/watch?v=kWiCuklohdY
starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니니다".format(customer))

print()

'''
참고 URL : https://seethefuture.tistory.com/82
'''

# 일반 구구단, 중첩 for문 사용
# print("🚀 구구단 시작")
# for i in range(2, 10):
#     print(f"바깥쪽 for문 {i}")

#     for j in range(1, 10):
#          print(f'{i} x {j} = {i * j}')
#          if (j == 9):
#              print("------------")

print()

# 사용자에게 입력값 받아서 구구단 시작
# num = int(input("🚀 몇 단을 입력하실건가요? ")) # 8

# if num > 0 and num < 10 :
#     for i in range(1, 10) : # range(n, n-1)
#         print(num, "x", i , "=", num * i)
# else :
#     print("다시 입력해주세요.")
