import math

# Begin23
A, B, C = map(float, input().split())
A, B, C = C, A, B
print(A, B, C)

# Begin24
A, B, C = map(float, input().split())
A, B, C = B, C, A
print(A, B, C)

# Begin26
x = float(input())
y = 4 * (x - 3)**6 - 7 * (x - 3)**3 + 2
print(y)

# Begin27
A = float(input())
A2 = A * A
A4 = A2 * A2
A8 = A4 * A4
print(A2, A4, A8)

# Begin28
A = float(input())
A2 = A * A
A3 = A2 * A
A5 = A3 * A2
A10 = A5 * A5
A15 = A10 * A5
print(A2, A3, A5, A10, A15)

# Begin30
alpha = float(input())
degrees = alpha * 180 / 3.14
print(degrees)

# Begin31
TF = float(input())
TC = (TF - 32) * 5 / 9
print(TC)

# Begin32
TC = float(input())
TF = TC * 9 / 5 + 32
print(TF)

# Begin33
X, A, Y = map(float, input().split())
price_per_kg = A / X
price_for_Y = price_per_kg * Y
print(price_per_kg, price_for_Y)

# Begin34
X, A, Y, B = map(float, input().split())
price_choco = A / X
price_iris = B / Y
ratio = price_choco / price_iris
print(price_choco, price_iris, ratio)

# Begin35
V, U, T1, T2 = map(float, input().split())
S = V * T1 + (V - U) * T2
print(S)

# Begin36
V1, V2, S, T = map(float, input().split())
total_distance = S + T * (V1 + V2)
print(total_distance)

# Integer2
M = int(input())
print(M // 1000)

# Integer3
bytes_count = int(input())
print(bytes_count // 1024)

# Integer4
A, B = map(int, input().split())
print(A // B)
