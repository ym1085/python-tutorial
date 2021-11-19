# @Date       : 21.11.19(금) 10:50
# @Author     : ymkim
# @Contents   : 모듈(Module) 호출부

# import ch_43_모듈
# ch_43_모듈.price(3) # 3명이서 영화 보러 갔을 때 가격
# ch_43_모듈.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# ch_43_모듈.price_soldier(5) # 5명의 군인이 영화 보러 갔을 떄

# 별칭 사용
# import ch_43_모듈 as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from 절 사용
# from ch_43_모듈 import *
# from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from 절 사용 , 원하는 함수만 호출
# from ch_43_모듈 import price, price_morning
# price(3)
# price_morning(5)

# from 절 사용 , 별칭 사용
from ch_43_모듈 import price_soldier as price
price(5)

