# proc2
def power_a234(a):
    return a**2, a**3, a**4

numbers = [2, 3, 4, 5, 6]
for num in numbers:
    p2, p3, p4 = power_a234(num)
    print(f"Число {num}: степень 2 = {p2}, степень 3 = {p3}, степень 4 = {p4}")

# proc4
def triangle_ps(a):
    P = 3 * a
    S = (a**2) * (3**0.5) / 4
    return P, S

sides = [3, 5, 8]
for side in sides:
    P, S = triangle_ps(side)
    print(f"Сторона {side}: Периметр = {P:.2f}, Площадь = {S:.2f}")

# proc5
def rect_ps(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    P = 2 * (width + height)
    S = width * height
    return P, S

rectangles = [(0, 0, 3, 4), (1, 1, 5, 4), (-2, -2, 2, 2)]
for x1, y1, x2, y2 in rectangles:
    P, S = rect_ps(x1, y1, x2, y2)
    print(f"Прямоугольник ({x1},{y1})-({x2},{y2}): Периметр = {P}, Площадь = {S}")

# proc7
def invert_digits(k):
    return int(str(k)[::-1])

numbers = [123, 4502, 9876, 500, 12]
for num in numbers:
    print(f"Исходное: {num} -> Перевернутое: {invert_digits(num)}")

# proc8
def add_right_digit(d, k):
    return int(str(k) + str(d))

K = 45
D1 = 3
D2 = 7
K = add_right_digit(D1, K)
print("Шаг 1:", K)
K = add_right_digit(D2, K)
print("Шаг 2:", K)

# proc9
def add_left_digit(d, k):
    return int(str(d) + str(k))

K = 45
D1 = 3
D2 = 7
K = add_left_digit(D1, K)
print("Шаг 1:", K)
K = add_left_digit(D2, K)
print("Шаг 2:", K)

# proc11
def minmax(x, y):
    if x < y:
        return x, y
    return y, x

A, B, C, D = 10, 4, 15, 2
min1, max1 = minmax(A, B)
min2, max2 = minmax(C, D)
final_min, _ = minmax(min1, min2)
_, final_max = minmax(max1, max2)
print("Минимум:", final_min)
print("Максимум:", final_max)

# proc13
def sort_dec3(a, b, c):
    lst = sorted([a, b, c], reverse=True)
    return lst[0], lst[1], lst[2]

set1 = (5, 12, 2)
set2 = (44, 1, 18)
print("Набор 1 по убыванию:", sort_dec3(*set1))
print("Набор 2 по убыванию:", sort_dec3(*set2))

# proc14
def shift_right3(a, b, c):
    return c, a, b

set1 = (1, 2, 3)
set2 = (10, 20, 30)
print("Сдвиг 1:", shift_right3(*set1))
print("Сдвиг 2:", shift_right3(*set2))

# proc15
def shift_left3(a, b, c):
    return b, c, a

set1 = (1, 2, 3)
set2 = (10, 20, 30)
print("Сдвиг 1:", shift_left3(*set1))
print("Сдвиг 2:", shift_left3(*set2))
