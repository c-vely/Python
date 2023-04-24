'''
문자열 인덱싱 
'''

# 1. letter가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letter = 'python'
print(letter[0], letter[2])

# 2. 아래의 문자열에서 '홀'만 출력하세요.
string = '홀짝홀짝홀짝'
print(string[::2])



'''
문자열 슬라이싱
'''

# 1. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = '24가 2210'
print(license_plate[-4:])

# 2. 문자열을 거꾸로 뒤집어 출력하세요.
string = 'PYTHON'
print(string[::-1])



'''
문자열 치환
'''

# 1. 아래의 전화번호에서 하이픈('-')을 제거하고 출력하세요.
phone_number = '010-1111-2222'
number_replace = phone_number.replace('-', ' ')
print(number_replace)



'''
문자열 다루기
'''

# 1. 위의 전화번호를 모두 붙여 출력하세요.
number_delate = phone_number.replace('-', '')
print(number_delate)

# 2. url에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = 'http://sharebook.kr'
url_split = url.split('.')
print(url_split[-1])



'''
문자열은 immutable
'''

# 1. 실행결과를 예상해보세요.
lang = 'python'
#lang[0] = 'P'
#print(lang) <-- 문자열은 변경이 안되기에 오류 발생



'''
replace  메서드
'''

# 1. 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
string_change = string.replace('a', 'A')
print(string_change)

# 2. 실행결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)  # <-- 변경된 값이 나오는 것이 아닌, 원본이 출력된다.
