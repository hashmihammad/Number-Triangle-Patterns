num = int(input())
new_num = num + 1
print("\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n\n\n")

for i in range(1, new_num):
    for j in range(i):
        print(j+1, end=" ")
    for k in range(num - i):
        print(" ", end=" ")
    for k in range(num - i):
        print(" ", end=" ")
    for j in range(i):
        print(i, end=" ")

    print()
