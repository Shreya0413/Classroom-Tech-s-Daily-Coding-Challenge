str_1 = input()
count = {}
for ch in str_1:
    if ch.isalnum():
        ch = ch.lower()  
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
for c in sorted(count):
    print(c, ":", count[c])
