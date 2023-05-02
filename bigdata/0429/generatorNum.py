import random

def generatingNum():
    numbers = []
    i = 0

    while (i < 5):
        number = random.randint(1, 46)
        if number is not numbers:
            numbers.append(number)
            i += 1
        else:
            pass
    
    return numbers
