# list17
A = [5, 2, 9, 1, 7]
print("По возрастанию:", sorted(A))
print("Исходный список:", A)

# list19
strings = ["апельсин", "киви", "банан", "груша"]
sorted_by_len = sorted(strings, key=len)
longest = max(strings, key=len)
print("По возрастанию длины:", sorted_by_len)
print("Самая длинная строка:", longest)

# list21
A = [-3, 5, 0, 12, -8, 7]
positive_elements = [x for x in A if x > 0]
print("Положительные элементы:", positive_elements)
print("Количество:", len(positive_elements))

# list22
A = [2, 5, 3, 5, 8]
D = 5
multiplied = [x * D for x in A]
count_D = len([x for x in A if x == D])
print("Умноженные на D:", multiplied)
print("Количество равных D:", count_D)

# list23
A = [-10, 3, -5, 8, -1]
sorted_by_abs = sorted(A, key=abs, reverse=True)
print("По убыванию модуля:", sorted_by_abs)

# list25
A = [10, 45, 12, 89, 34]
sorted_unique = sorted(list(set(A)))
second_largest = sorted_unique[-2]
print("Второй по величине элемент:", second_largest)

# list26
A = [2, 8, 4, 10, 6]
avg = sum(A) / len(A)
larger_than_avg = [x for x in A if x > avg]
print("Элементы больше среднего:", larger_than_avg)
print("Среднее арифметическое:", avg)

# list28
strings = ["яблоко", "банан", "ягода", "груша", "якорь"]
letter = "я"
filtered_strings = [s for s in strings if s and s[0] == letter]
print(f"Строки на букву '{letter}':", filtered_strings)

# list29
A = [15, 2, 88, 24, 9, 41]
K = 3
K_largest = sorted(A, reverse=True)[:K]
print(f"{K} наибольших элементов:", K_largest)

# list30
strings = ["python", "code", "list", "task"]
lengths = [len(s) for s in strings]
total_length = sum(lengths)
print("Список длин строк:", lengths)
print("Суммарная длина всех строк:", total_length)
