# 뒷자리만 출력
license_plate = '24rk 2210'
print(license_plate[-4:])

# 오프셋 이용
string = '홀짝홀짝홀짝'
print(string[::2])

# 거꾸로 출력
string = 'PYTHON'
print(string[::-1])

# 치환
phone_number = '010-1111-2222'
phone_number = phone_number.replace('-', ' ')
print(phone_number)

# split
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])