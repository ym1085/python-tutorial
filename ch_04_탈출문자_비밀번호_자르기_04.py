# @Date       : 21.11.17(수) 18:00
# @Author     : ymkim
# @Contents   : 탈출 문자 및 비밀번호 자르기 예제

# print("백문이 불여일견 \n백견이 불여일타")
# print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
# \r : 커서 맨 앞으로 문자열 이동
# \b : 백스페이스 (한 글자 삭제)
# \t : 탭
print("C:\\Users\\")
print("Red Applie\rPine")
print("Redd\bApple")
print("Red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "|" 로 구성

#             (nav)       (5)     (1)     (!)
# 예) 생성된 비밀벊 : nav51!

# 1. http:// 자른다
# 2. .com 자른다
# 3. naver => nav + str.len(domain_name) + str.count("e") + "!"

# 💣 내가 작성한 예제
url = "http://naver.com"

domain_name = url.split("//")[1].split(".")[0]
password = domain_name[0:3] + str(len(domain_name)) + str(domain_name.count("e")) + "!"
print("Site password = " + password)

# 🌈 강사분이 작성한 예제
url = "http://naver.com"
url = "http://youtube.com"
url = "http://google.com"

my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")]
#print("MY_STR = " + my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("Site password with teacher = " + url + ", " + password);

# Quiz) URL에서 경로와 파일명을 분리
# 1. 게임덱스에서 문자열 swap해서 했던 것 같은데, 기억이 잘 안나네
# 2. URL 경로에서 파일명을 뽑아내는 예제, 메서드(함수) 따로 만들어서 사용하는 방법도 생각하면 좋을 듯

original_url = "http://www.naver.com/test/study/myfilename.doc"

arr_split_url = original_url.split("/")
print("Confirm Split URL  = " + str(arr_split_url))

arr_split_url_length = len(arr_split_url)               # URL 쪼개서 길이 구한다
print("URL Length = " + str(arr_split_url))

arr_file_name = arr_split_url[arr_split_url_length - 1] # 파일명 추출
print("Check File Name = " + arr_file_name)

file_name = arr_file_name.split(".") # 확장자 기준으로 쪼갠다
print(file_name[0]) # 파일명
print(file_name[1]) # 확장자

# def splitOriginalURL(str url):
#     str split_url = ""
#     str split_file_name = ""
#     str file_name = ""
#     int split_url_len = 0
    
#     if url != null :
#         print("OK!")
                
