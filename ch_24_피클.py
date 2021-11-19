# @Date       : 21.11.18(목) 14:4
# @Author     : ymkim
# @Contents   : 파일 입출력

'''
피클(Pickle)?
1.
2.
'''

import pickle
 
# w: 쓰기, b: 바이너리
# pickle을 사용하려면 반드시 바이너리를 지정해야 한다
# profile_file = open("profile.pickle", "wb")
# profile = {
#     "이름" : "박명수",
#     "나이" : 30,
#     "취미" : [
#         "축구",
#         "골프",
#         "코딩"
#     ]
# }

# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# 피클 사용하여 파일 내용 불러오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
print(type(profile))
profile_file.close()