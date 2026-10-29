# file1
import os

S = "test.txt"
try:
    with open(S, "w"):
        pass
    print(True)
except Exception:
    print(False)

# file3
filename = "progression.txt"
A = 2.0
D = 1.5
with open(filename, "w") as f:
    for i in range(10):
        f.write(f"{A + i * D}\n")

# file4
import os

files = ["1.txt", "2.txt", "3.txt", "4.txt"]
count = 0
for name in files:
    if os.path.exists(name):
        count += 1
print(count)

# file8
import os

f1 = "first.txt"
f2 = "second.txt"
with open(f1, "r") as f:
    lines = f.readlines()
with open(f2, "w") as f:
    f.write(lines[0])
    f.write(lines[-1])

# file9
import os

f1 = "file1.txt"
f2 = "file2.txt"
existing = f1 if os.path.exists(f1) else f2
missing = f2 if existing == f1 else f1

with open(existing, "r") as f:
    lines = f.readlines()
with open(missing, "w") as f:
    f.write(lines[-1])
    f.write(lines[0])
