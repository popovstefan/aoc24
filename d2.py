import os
from os import remove

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
    def preprocess_report(report):
        """
        Preprocess the report to remove the first sequence of equal elements.
        Returns the modified report.
        """
        for i in range(1, len(report)):
            if report[i] != report[i - 1]:
                return report[i:]  # Return the report starting from the first differing element
        return report  # If all elements are equal, return the report as-is

    def is_safe(report):
        """Check if a report is safe."""
        n = len(report)
        diffs = [report[i + 1] - report[i] for i in range(n - 1)]

        # Check if all differences are within 1 to 3 and are either all positive or all negative
        if all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs):
            return True
        return False

    def can_be_safe_with_removal(report):
        """Check if a report can be made safe by removing one level."""
        n = len(report)
        for i in range(n):
            # Remove one level and check if the remaining report is safe
            new_report = report[:i] + report[i + 1:]
            if is_safe(new_report):
                return True
        return False

    def count_safe_reports(data):
        """Count the number of safe reports including Problem Dampener rules."""
        safe_count = 0

        for report in data:
            preprocessed_report = preprocess_report(report)
            if is_safe(preprocessed_report) or can_be_safe_with_removal(preprocessed_report):
                safe_count += 1

        return safe_count

    lines = []
    for line in puzzle_input:
        lines.append([int(x) for x in line.split()])

    print(count_safe_reports(lines))


p2()
