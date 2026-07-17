num = int(input())
half_num = num // 2
for i in range(half_num, 0, -1):
    print(i, end=" ")
for i in range(1, half_num + 1):
    print(-i, end=" ")
print()