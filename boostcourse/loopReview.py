# 문자열 거꾸로 출력
sentence = "I love you"
reverse_sen = ""

for char in sentence:
    print(f"REVERSE #1  {reverse_sen}")
    reverse_sen = char + reverse_sen
    print(f"REVERSE #2  {reverse_sen}")
    
    
# 십진수 -> 2진수 변환
decimal = 10
result = ''
while (decimal > 0):
    remainder = decimal % 2
    print("remainder = decimal % 2 : ", remainder)
    decimal = decimal // 2
    print("decimal = decimal// 2 : ", decimal)
    result = str(remainder) + result
    print("result = str(remainder) + result: ", result)
print("result : ", result)
