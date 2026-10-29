# while2
A = 17
B = 3
count = 0
while A >= B:
    A -= B
    count += 1
print("Количество отрезков:", count)

# while4
N = 27
is_power_of_3 = True
while N > 1:
    if N % 3 != 0:
        is_power_of_3 = False
        break
    N //= 3
if N != 1:
    is_power_of_3 = False
print(is_power_of_3)

# while5
N = 16
K = 0
while N > 1:
    N //= 2
    K += 1
print("Показатель степени K:", K)

# while6
N = 5
factorial = 1.0
while N > 0:
    factorial *= N
    N -= 2
print("Двойной факториал:", factorial)

# while7
N = 17
K = 1
while K * K <= N:
    K += 1
print("Наименьшее K:", K)

# while9
N = 10
K = 1
power = 3
while power <= N:
    power *= 3
    K += 1
print("Наименьшее K:", K)

# while10
N = 30
K = 0
power = 1
while power * 3 < N:
    power *= 3
    K += 1
print("Наибольшее K:", K)

# while12
N = 10
K = 0
total_sum = 0
while total_sum + (K + 1) <= N:
    K += 1
    total_sum += K
print("Наибольшее K:", K)
print("Сумма:", total_sum)

# while13
A = 2.1
K = 0
total_sum = 0.0
while total_sum <= A:
    K += 1
    total_sum += 1 / K
print("Наименьшее K:", K)
print("Сумма:", round(total_sum, 4))

# while14
A = 2.1
K = 0
total_sum = 0.0
while total_sum + 1 / (K + 1) < A:
    K += 1
    total_sum += 1 / K
print("Наибольшее K:", K)
print("Сумма:", round(total_sum, 4))
