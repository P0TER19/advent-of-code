def main():
    lines = []
    reports = []
    safe_report_count = 0
    with open("input.txt") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        count = 0
        reports = [int(report) for report in lines[i].split(" ")]
        for j in range(len(reports) - 1):
            if (reports[j] - reports[j + 1]) in [1, 2, 3]:
                count += 1
            elif (reports[j] - reports[j + 1]) in [-1,-2,-3]:
                count -=1
        if abs(count) == len(reports) - 1:
            safe_report_count += 1
    print("safe", safe_report_count)


main()
