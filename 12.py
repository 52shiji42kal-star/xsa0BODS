# string2
N = 65
print(chr(N))

# string3
C = 'B'
print(chr(ord(C) - 1), chr(ord(C) + 1))

# string4
N = 5
letters = ""
for i in range(N):
    letters += chr(ord('A') + i)
print(letters)

# string5
N = 5
letters = ""
for i in range(N):
    letters += chr(ord('z') - i)
print(letters)

# string7
text = "Hello"
print(ord(text[0]), ord(text[-1]))

# string8
N = 7
C = '*'
print(C * N)

# string9
N = 6
C1 = 'A'
C2 = 'B'
result = ""
for i in range(N // 2):
    result += C1 + C2
print(result)

# string12
S = "Code"
N = 3
stars = '*' * N
print(stars.join(S))

# string14
text = "Hello WORLD!"
count = 0
for char in text:
    if 'A' <= char <= 'Z':
        count += 1
print("Количество прописных латинских букв:", count)

# string15
text = "Привет WORLD мир!"
count = 0
for char in text:
    if ('a' <= char <= 'z') or ('а' <= char <= 'я') or (char == 'ё'):
        count += 1
print("Количество строчных латинских и русских букв:", count)
