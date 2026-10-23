# Boolean2
def boolean2(A: int) -> bool:
    return A % 2 != 0


# Boolean3
def boolean3(A: int) -> bool:
    return A % 2 == 0


# Boolean4
def boolean4(A: int, B: int) -> bool:
    return A > 2 and B <= 3


# Boolean5
def boolean5(A: int, B: int) -> bool:
    return A >= 0 or B < -2


# Boolean7
def boolean7(A: int, B: int, C: int) -> bool:
    return A < B < C or C < B < A


# Boolean8
def boolean8(A: int, B: int) -> bool:
    return A % 2 != 0 and B % 2 != 0


# Boolean9
def boolean9(A: int, B: int) -> bool:
    return A % 2 != 0 or B % 2 != 0


# Boolean10
def boolean10(A: int, B: int) -> bool:
    return (A % 2 != 0) != (B % 2 != 0)


# Boolean11
def boolean11(A: int, B: int) -> bool:
    return (A % 2) == (B % 2)


# Boolean13
def boolean13(A: int, B: int, C: int) -> bool:
    return A > 0 or B > 0 or C > 0


# Boolean15
def boolean15(A: int, B: int, C: int) -> bool:
    return (A > 0) + (B > 0) + (C > 0) == 2

# If1
def if1(num: int) -> int:
    if num > 0:
        num += 1
    return num


# If2
def if2(num: int) -> int:
    if num > 0:
        num += 1
    else:
        num -= 2
    return num


# If4
def if4(A: int, B: int, C: int) -> int:
    count = 0
    if A > 0: count += 1
    if B > 0: count += 1
    if C > 0: count += 1
    return count


# If5
def if5(A: int, B: int, C: int) -> tuple[int, int]:
    pos_count = 0
    neg_count = 0

    if A > 0: pos_count += 1
    elif A < 0: neg_count += 1

    if B > 0: pos_count += 1
    elif B < 0: neg_count += 1

    if C > 0: pos_count += 1
    elif C < 0: neg_count += 1

    return pos_count, neg_count
