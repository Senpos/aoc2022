def is_overlap(a, b):
    return b[0] <= a[1] and b[1] >= a[0]


count = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        first, second = [[int(i) for i in interval.split("-", maxsplit=1)] for interval in line.split(",")]
        if is_overlap(first, second):
            count += 1
print(count)
