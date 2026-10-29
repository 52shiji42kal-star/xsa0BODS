# list2
A = [10, 20, 30, 40, 50]
K = 2
print("Элемент A[K]:", A[K])
print("Последний элемент:", A[-1])
print("Число элементов перед K:", K)

# list3
A = [1, 2, 3, 4, 5, 6]
total_sum = sum(A)
product = 1
for i in range(0, len(A), 2):
    product *= A[i]
print("Сумма всех элементов:", total_sum)
print("Произведение с четными индексами:", product)

# list5
A = [1, 2, 3]
D = 99
A.append(D)
print("Новый список:", A)
print("Длина:", len(A))

# list7
A = [10, 20, 30, 40]
print("В обратном порядке:", A[::-1])
print("Исходный список:", A)

# list9
A = [10, 20, 30, 40, 50]
avg = sum(A) / len(A)
larger_elements = []
for x in A:
    if x > avg:
        larger_elements.append(x)
print("Элементы больше среднего:", larger_elements)
print("Количество:", len(larger_elements))

# list10
strings = ["яблоко", "груша", "банан", "киви", "апельсин"]
longest = strings[0]
shortest = strings[0]
for s in strings:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s
print(f"Самая длинная: '{longest}' (длина {len(longest)})")
print(f"Самая короткая: '{shortest}' (длина {len(shortest)})")

# list12
A = [10, 20, 30, 40]
K = 2
A.insert(K, 0)
print("Список после вставки:", A)
print("Длина:", len(A))

# list13
A = [10, 20, 30, 40]
removed = A.pop()
print("Удаленный элемент:", removed)
print("Полученный список:", A)

# list14
A = [5, 2, 5, 8, 5, 3]
D = 5
count_D = A.count(D)
if D in A:
    first_index = A.index(D)
else:
    first_index = -1
print("Число вхождений:", count_D)
print("Индекс первого вхождения:", first_index)

# list15
A = [10, 20, 30, 40, 50, 60]
odd_positions_elements = []
odd_sum = 0
for i in range(len(A)):
    position = i + 1
    if position % 2 != 0:
        odd_positions_elements.append(A[i])
        odd_sum += A[i]
print("Элементы на нечетных позициях:", odd_positions_elements)
print("Их сумма:", odd_sum)
