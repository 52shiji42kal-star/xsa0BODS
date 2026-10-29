# for2
A = 3
B = 8
N = 0
for i in range(A, B + 1):
    print(i)
    N += 1
print("Количество:", N)

# for4
price = 150.5
for kg in range(1, 11):
    cost = kg * price
    print(kg, "кг =", cost)

# for5
price = 150.5
for i in range(1, 11):
    kg = i / 10
    cost = kg * price
    print(kg, "кг =", round(cost, 2))

# for6
price = 150.5
for i in range(12, 21, 2):
    kg = i / 10
    cost = kg * price
    print(kg, "кг =", round(cost, 2))

# for8
A = 2
B = 5
product = 1
for i in range(A, B + 1):
    product *= i
print("Произведение:", product)

# for9
A = 2
B = 5
total_sum = 0
for i in range(A, B + 1):
    total_sum += i ** 2
print("Сумма квадратов:", total_sum)

# for11
N = 3
total_sum = 0
for i in range(0, N + 1):
    total_sum += (N + i) ** 2
print("Сумма:", total_sum)

# for12
N = 4
product = 1.0
for i in range(1, N + 1):
    factor = 1.0 + i / 10
    product *= factor
print("Произведение:", round(product, 4))

# for13
N = 4
total_sum = 0.0
sign = 1
for i in range(1, N + 1):
    term = 1.0 + i / 10
    total_sum += sign * term
    sign = -sign
print("Значение выражения:", round(total_sum, 2))

# for15
A = 2.5
N = 3
result = 1.0
for i in range(N):
    result *= A
print("Результат:", result)
