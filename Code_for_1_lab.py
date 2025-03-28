def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def get_input():
    while True:
        try:
            a, b, c = map(int, input("Введите три натуральных числа a, b, c: ").split())
            if a <= 0 or b <= 0 or c <= 0:
                print("Ошибка: числа должны быть натуральными (≥1). Попробуйте снова.")
                continue
            return a, b, c
        except ValueError:
            print("Ошибка: введите ровно три целых числа через пробел.")

a, b, c = get_input()
g, x0, y0 = extended_gcd(a, b)

if c % g != 0:
    print("Impossible")
else:
    x = x0 * (c // g)
    y = y0 * (c // g)
    
    
    k = (x * g) // b
    x_pos = x - k * (b // g)
    y_pos = y + k * (a // g)
    
    if x_pos >= 0:
        print(x_pos, y_pos)
    else:
        
        x_pos += (b // g)
        y_pos -= (a // g)
        if x_pos >= 0:
            print("Решение: ", x_pos, y_pos)
        else:
            print("Impossible")
