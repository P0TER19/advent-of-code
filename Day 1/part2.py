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
    for i in range(len(left)):
        count = right.count(left[i])
        s = s + left[i] * count
    print(s)


main()
