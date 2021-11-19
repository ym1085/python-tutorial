# @Date       : 21.11.17(수) 20:28
# @Author     : ymkim
# @Contents   : Map

# Map == Obj
cabinet = {
    3 : "유재석",
    100 : "김태호"
}

# @ api["key"]
print(cabinet[3])
print(cabinet[100])
print("Hi")

print()

# @ api.get("key")
print(cabinet.get(3))
print(cabinet.get(100))
print(cabinet.get(1002)) # None
print(cabinet.get(1002), "사용 가능") # None일 경우 사용 가능 출력

print("\n")

# keyword in
print(3 in cabinet) # True
print(5 in cabinet) # False

print("\n")

# 손님
cabinet = {
    "A-3" : "유재석",
    "B-100" : "김태호"
}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"

print()
print(cabinet["A-3"])
print(cabinet["B-100"])

print()

# 간 손님
del cabinet["A-3"]
print(cabinet)

print()

# Key 들만 출력
print(cabinet.keys())

print()

# Value 들만 출력
print(cabinet.values())

print()

# key, value 쌍으로 출력
print(cabinet.items())

