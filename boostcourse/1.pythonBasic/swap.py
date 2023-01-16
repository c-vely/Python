def swap_value(x, y):
    temp = x
    x = y
    y = temp  
    

def swap_offset(offset_x, offset_y):
    temp = ex[offset_x]
    ex[offset_x] = ex[offset_y]
    ex[offset_y] = temp


def swap_reference(list_ex, offset_x, offset_y):
    temp = list_ex[offset_x]
    list_ex[offset_x] = list_ex[offset_y]
    list_ex[offset_y] = temp
    
# 변경 안 됨
ex = [1, 2, 3, 4, 5]
swap_value(ex[0], ex[1])
print(ex)

# a리스트의 전역 변수 값을 직접 변경
swap_offset(0, 1)
print(ex)

# a 리스트 객체의 주소값을 받아 값을 변경 (요렇게 쓰는 게 제일 좋음)
ex = [1, 2, 3, 4, 5]
swap_reference(ex, 3, 4)
print(ex)
