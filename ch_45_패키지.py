# @Date       : 21.11.19(금) 10:52
# @Author     : ymkim
# @Contents   : 패키지 실습

'''
패키지
1. 하나의 폴더에 모듈을 모아둔 것
2. 파이썬 패키지를 만들어 누구나 사용할 수 있도록 구성
'''

# import travel.thailand
# import travel.thailand.ThailandPackage
# from travel.thailand import ThailandPackage

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 🌈 해당 파일을 어디에서 가져오는지 확인하는 구문
import inspect 
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

