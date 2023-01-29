# 3.
a = 10
float(a)
print(type(a))


# 4.
name = "Apple"
price = 5600
number = 7
print("{2}, {1}, {0}".format(number, name, price))


# 5.
test_list = ['치킨', '피자', '삼겹살', '족발', '초밥', '소주']
print(test_list[1::2])


# 6.
for data in test_list[::2]:
    if len(data) == 3:
        print(data)
    
        
# 7.
def print_greedings(t):
    t ="Hello."
    print("In Fn : ", t)
    
x = "Hi."
print_greedings(x)
print("Out Fn : ", x) 


# 8. 
string = "#You #Only #Live #Once."
print(string.replace("#", ""))


# 9.
a, b, *c = (14, 21, 25, 39, 46, 57)
print(c)


# 10.
data_list = [0, 1, 2, 3, 4, 5]

def f(x):
    return x ** 5

new_list = []
for value in data_list:
    new_list.append(f(value))
print(data_list)
print(new_list)