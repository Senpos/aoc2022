# yoinked from https://gist.github.com/hovsater/f70c8f778759d8cfc797fdad614b1c80
def is_fully_contained(a, b):
    return (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])


count = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        first, second = [[int(i) for i in interval.split("-", maxsplit=1)] for interval in line.split(",")]
        if is_fully_contained(first, second):
            count += 1
print(count)
