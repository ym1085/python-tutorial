# @Date       : 21.11.18(목) 15:04
# @Author     : ymkim
# @Contents   : with문 실습

# import pickle

# with open("profile.pickle", "rb") as profile_file: # 파일명, 읽기모드
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8") as study_file :
#     study_file.write("파이썬을 얄심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file :
    print(study_file.read())