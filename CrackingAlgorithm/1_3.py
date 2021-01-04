def problem1_3(text, n):
    s = list(text)
    l1 = n - 1
    l2 = len(s) - 1
    while l1 >= 0:
        if s[l1] == ' ':
            s[l2] = '0'
            s[l2 - 1] = '2'
            s[l2 - 2] = '%'
            l2 -= 3
        else:
            s[l2] = s[l1]
            l2 -= 1
        l1 -= 1
    return "".join(s)