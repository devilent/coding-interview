def problem1_4(s):
    d = dict()
    oddCount = 0
    for i in s:
        if i == ' ':
            continue
        ch = i.lower()
        if d.get(ch) is not None:
            d[ch] += d[ch]
        else:
            d[ch] = 1
        if d[ch] % 2 != 0:
            oddCount += 1
        else:
            oddCount -= 1
   
    return oddCount <= 1