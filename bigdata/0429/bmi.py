def calc(weight, height):
    h = height * 0.01 #cm -> m로 변경
    result = weight / (h * h)
    return result

def result(value):
    result = ''
    if value < 18.50:
        result = '저체중'
    elif value < 22.90:
        result = '정상'
    elif value < 24.90:
        result = '과체중'
    elif value > 24.90:
        result = '비만'
    return result