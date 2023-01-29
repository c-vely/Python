def addition(x, y):
    return x + y


def multiplication(x, y):
    return x * y


def divided_by_2(x):
    return x/2


def main():
    print(15 == addition(10, 5))
    print(addition(10, 100))
    
# python Shell에서 import 했을 때, cmd 창에서 바로 실행 x / python trapezoid.py하면 실행 o
if __name__ == "__main__":
    main()