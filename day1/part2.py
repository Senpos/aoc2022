import heapq

totals = []
with open("input.txt") as f:
    acc = 0
    for line in f:
        if line == "\n":
            totals.append(acc)
            acc = 0
        else:
            acc += int(line)
res = max(heapq.nlargest(3, totals))
print(res)
