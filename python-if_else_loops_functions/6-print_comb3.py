#!/usr/bin/python3
for i in range(0, 8):
    for j in range(0, 10):
        if i == j or j - i < 1:
            continue
        print("{}{}, ".format(i, j), end="")
print(89)
