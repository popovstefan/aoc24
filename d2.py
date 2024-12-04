import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd2.txt"))


def p1():
    solution = 0
    for line in puzzle_input:
        elements = [int(x) for x in line.split()]
        increase = 0
        decrease = 0
        big_diff = 0
        for inx, current in enumerate(elements[1:]):
            previous = elements[inx]
            diff = abs(current - previous)
            if diff > 3 or diff < 1:
                big_diff += 1
                break
            if current > previous:
                increase += 1
            if current < previous:
                decrease += 1
            if increase > 0 and decrease > 0:
                break
        if (increase > 0 and decrease > 0) or big_diff > 0:
            continue
        else:
            solution += 1
    print(solution)


def p2():
    def is_safe(report):
        """Check if a report is safe."""
        n = len(report)
        if n < 2:
            return True  # Trivially safe if there are fewer than 2 levels

        diffs = [report[i] - report[i - 1] for i in range(1, n)]
        # Check if the differences are all within 1 to 3 or -3 to -1
        if all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs):
            return True
        return False

    def can_be_safe_with_removal(report):
        """Check if a report can be made safe by removing one level."""
        n = len(report)
        for i in range(n):
            # Create a new report by removing the ith level
            new_report = report[:i] + report[i + 1:]
            if is_safe(new_report):
                return True
        return False

    def count_safe_reports(data):
        """Count the number of safe reports, considering the Problem Dampener rule."""
        safe_count = 0

        for report in data:
            if is_safe(report) or can_be_safe_with_removal(report):
                safe_count += 1
        return safe_count

    lines = []
    for line in puzzle_input:
        lines.append([int(x.strip()) for x in line.split()])
    print(count_safe_reports(lines))


p2()
