def main():
    s = 0
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
    left = []
    right = []
    for i in range(len(lines)):
        left.append(int(lines[i].split(" ")[0]))
        right.append(int(lines[i].split(" ")[-1]))
    left.sort()
    right.sort()
    for i in range(len(left)):
        s = s + abs(left[i] - right[i])
    print(s)


main()
