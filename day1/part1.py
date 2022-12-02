max_ = 0
with open("input.txt") as f:
    acc = 0
    for line in f:
        if line == "\n":
            if acc > max_:
                max_ = acc
            acc = 0
        else:
            acc += int(line)
print(max_)
