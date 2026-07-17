n = int(input())
result = []
for i in range(1, n + 1):
    if i % 5 != 0 and i % 7 != 0:
        result.append(str(i))
print(" ".join(result))