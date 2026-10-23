import math

# Задание 1: 
a, b, c = map(float, input().split())
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print(f"{V:.2f} {S:.2f}")

# Задание 2: 
R = float(input())
L = 2 * math.pi * R
S = math.pi * R**2
print(f"{L:.2f} {S:.2f}")

# Задание 3: 
a, b = map(float, input().split())
print(f"{(a + b) / 2:.2f}")

# Задание 4: 
a, b = map(float, input().split())
print(f"{math.sqrt(a * b):.2f}")

# Задание 5: 
a, b = map(float, input().split())
a2, b2 = a**2, b**2
print(f"{a2 + b2:.2f} {a2 - b2:.2f} {a2 * b2:.2f} {a2 / b2:.2f}")

# Задание 6: 
a, b = map(float, input().split())
abs_a, abs_b = abs(a), abs(b)
print(f"{abs_a + abs_b:.2f} {abs_a - abs_b:.2f} {abs_a * abs_b:.2f} {abs_a / abs_b:.2f}")

# Задание 7: 
a, b = map(float, input().split())
c = math.hypot(a, b)  
P = a + b + c
print(f"{c:.2f} {P:.2f}")

# Задание 8: 
R1, R2 = map(float, input().split())
S1 = math.pi * R1**2
S2 = math.pi * R2**2
S3 = abs(S1 - S2)  
print(f"{S1:.2f} {S2:.2f} {S3:.2f}")

# Задание 9: 
L = float(input())
R = L / (2 * math.pi)
S = math.pi * R**2
print(f"{R:.2f} {S:.2f}")

# Задание 10: 
S = float(input())
R = math.sqrt(S / math.pi)
D = 2 * R
L = 2 * math.pi * R
print(f"{D:.2f} {L:.2f}")

# Задание 11: 
x1, x2 = map(float, input().split())
print(f"{abs(x2 - x1):.2f}")

# Задание 12: 
A, B, C = map(float, input().split())
AC = abs(C - A)
BC = abs(C - B)
print(f"{AC:.2f} {BC:.2f} {AC + BC:.2f}")

# Задание 13: 
A, B, C = map(float, input().split())
AC = abs(C - A)
BC = abs(C - B)
print(f"{AC * BC:.2f}")

# Задание 14:
x1, y1, x2, y2 = map(float, input().split())
w = abs(x2 - x1)
h = abs(y2 - y1)
P = 2 * (w + h)
S = w * h
print(f"{P:.2f} {S:.2f}")

# Задание 15: 
x1, y1, x2, y2 = map(float, input().split())
distance = math.dist((x1, y1), (x2, y2))  
print(f"{distance:.2f}")
