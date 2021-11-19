# @Date       : 21.11.17(수) 21:48
# @Author     : ymkim
# @Contents   : 파이썬 코딩대회 퀴즈

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 참석자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# 1. 댓글 작성자 20명
# 2. 아이디 1 - 20

# (활용 예제)
# from random import *
# lst = [ 1, 2, 3, 4, 5 ]
# print( lst )
# shuffle( lst ) # 데이터 섞기
# print( lst )
# print( sample( lst, 1 ) ) # list 중에서 한개를 뽑아라

'''
잊으면 안되느 부분
1. shuffle(인자) -> 객체 내에 존재하는 데이터를 무작위로 섞는다
2. sample(인자, 갯수) -> 객체 내에서 갯수만큼 데이터를 출력
'''

from random import *
users = range(1, 21)
users = list(users)

print()

shuffle(users)

winners = sample(users, 4)
#print(winners)

print("----당첨자 발표----\n")
print("치킨 당첨자 {0}".format(winners[0]))
print("치킨 당첨자 {0}".format(winners[1:]) + "\n")
print("----축하 합니다.----")