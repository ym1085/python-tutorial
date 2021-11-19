
# @Date       : 21.11.18(목) 12:27
# @Author     : ymkim
# @Contents   : 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     for lang in language :
#         print(lang, end = " ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JS")
# profile("김태호", 25, "Kotiln", "Swift")

def sum(*args) :
    result = 0
    for i in args :
        result += i
        print("result = {0} 입니다".format(result))
    return result

result = sum(1,2,3,4,5,6,7,8,9,10)
print("최종값 = {0}".format(result))