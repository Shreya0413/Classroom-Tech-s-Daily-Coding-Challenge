str = input().strip()

for i in str:
    if str.count(i) == 1:   
        print(i)
        break
else:
    print("NO")
