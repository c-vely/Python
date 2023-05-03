Pi = 3.141592

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print('mymod.py를 최상위 모듈로 실행했습니다.')
    
if __name__ == "__main__":
    main()
else:
    print('mymod.py이 모듈이름: ' + __name__)