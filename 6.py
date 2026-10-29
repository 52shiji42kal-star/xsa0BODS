# err2
A = input("Введите первое число: ")
B = input("Введите второе число: ")
a = int(A)
b = int(B)
try:
    result = a / b
    print(round(result, 1))
except ZeroDivisionError:
    print("Делить на ноль нельзя")

# err5
text = input("Введите строку: ")
index_str = input("Введите индекс: ")
index = int(index_str)
try:
    print(text[index])
except IndexError:
    print("Нет такого символа")

# err6
text = input("Введите строку: ")
index_str = input("Введите индекс: ")
try:
    index = int(index_str)
    print(text[index])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")

# err7
while True:
    user_input = input("Введите целое число: ")
    try:
        number = int(user_input)
        print(number)
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")

# err9
age_str = input("Введите возраст: ")
age = int(age_str)
try:
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
    print("Принято:", age)
except ValueError as e:
    print("Отклонено:", e)

# err11
A = input("Введите первое число: ")
B = input("Введите второе число: ")
try:
    a = float(A)
    b = float(B)
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")

# err12
user_input = input("Введите целое число: ")
try:
    number = int(user_input)
    print(number)
except Exception as e:
    print(e)
    print(type(e))
