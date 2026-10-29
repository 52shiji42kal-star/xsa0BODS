# proc17
def roots_count(a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
        return 2
    elif D == 0:
        return 1
    return 0

equations = [(1, -3, 2), (1, 2, 1), (1, 1, 5)]
for a, b, c in equations:
    print(f"Уравнение ({a}, {b}, {c}): корней =", roots_count(a, b, c))

# proc18
def circle_s(r):
    return 3.14 * (r**2)

radii = [2, 4.5, 10]
for r in radii:
    print(f"Радиус {r}: площадь =", circle_s(r))

# proc20
def triangle_p(a, h):
    b = ((a / 2)**2 + h**2)**0.5
    return a + 2 * b

triangles = [(6, 4), (10, 12), (3, 2)]
for a, h in triangles:
    print(f"Основание {a}, высота {h}: периметр =", round(triangle_p(a, h), 2))

# proc21
def sum_range(a, b):
    if a > b:
        return 0
    total = 0
    for i in range(a, b + 1):
        total += i
    return total

A, B, C = 2, 5, 8
print("Сумма от A до B:", sum_range(A, B))
print("Сумма от B до C:", sum_range(B, C))

# proc23
def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

points = [(2, 3), (-4, 5), (-1, -6)]
for x, y in points:
    print(f"Точка ({x}, {y}): четверть =", quarter(x, y))

# proc24
def even(k):
    return k % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for num in numbers:
    if even(num):
        count += 1
print("Количество четных чисел:", count)

# proc25
def is_square(k):
    if k <= 0:
        return False
    root = int(k**0.5)
    return root * root == k

numbers = [4, 5, 9, 11, 16, 20, 25, 30, 36, 40]
count = 0
for num in numbers:
    if is_square(num):
        count += 1
print("Количество полных квадратов:", count)

# proc26
def is_power5(k):
    if k <= 0:
        return False
    while k % 5 == 0:
        k //= 5
    return k == 1

numbers = [5, 10, 25, 30, 125, 150, 625, 700, 5, 1]
count = 0
for num in numbers:
    if is_power5(num):
        count += 1
print("Количество степеней пятерки:", count)

# proc27
def is_power_n(k, n):
    if k <= 0 or n <= 1:
        return False
    while k % n == 0:
        k //= n
    return k == 1

N = 3
numbers = [3, 6, 9, 12, 27, 30, 81, 90, 3, 1]
count = 0
for num in numbers:
    if is_power_n(num, N):
        count += 1
print(f"Количество степеней числа {N}:", count)

# proc29
def digit_count(k):
    if k <= 0:
        return 0
    return len(str(k))

numbers = [5, 23, 456, 7890, 12345]
for num in numbers:
    print(f"Число {num}: количество цифр =", digit_count(num))
