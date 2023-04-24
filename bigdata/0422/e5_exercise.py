'''
upper 메서드
'''

# 1. 문자을 대문자로 변경하세요.
ticker = 'btc_trw'
ticker_upper = ticker.upper()
print(ticker_upper)



'''
lower 메서드
'''

# 1. 모두 소문자로 변경하라.
ticker_lower = ticker.lower()
print(ticker_lower)



'''
captalize 메서드
'''

# 1. 첫글자만 대문자로 변경하세요.
str = 'hello'
str_capitalze = str.capitalize()
print(str_capitalze)



'''
endswith 메서드
'''

# 1. 파일 이름이 문자열로 저장되어 있을 때, 'xlsx'로 끝나는지 확인하세요.
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

# 2. 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
print(file_name.endswith('xlsx' or 'xls'))



'''
startwith 메서드
'''

# 1. 파일이름이 '2020'로 시작하는지 확인하세요.
file_name = '2020_보고서.xlsx'
print(file_name.startswith('2020'))



'''
split 메서드
'''

# 1. 다음 문자열을 btc와 krw로 나눠보세요.
ticker = 'btc_krw'
ticker_split = ticker.split('_')
print(ticker_split)

# 2. 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
data = '2020-05-01'
data_split = data.split('-')
print(data_split)



'''
rstrip 메서드
'''

# 1. 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
str_num = '039490   '
str_num_rsplit = str_num.rsplit()
print(str_num_rsplit)

