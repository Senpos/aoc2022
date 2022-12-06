import re


with open("input.txt") as f:
    data = f.read()

drawing, procedure = data.split("\n\n", maxsplit=1)

lines = drawing.splitlines()
# we don't really need stack identifiers (1, 2, 3, ...)
lines.pop()

rows = [re.findall(r".(.). ?", line) for line in lines]
# rotate
stacks = [
    [cell for cell in row if cell != " "]
    for row in zip(*rows[::-1])
]

moves = procedure.splitlines()
for move in moves:
    how_many, from_, to = map(int, re.findall(r"\d+", move))
    from_ -= 1
    to -= 1

    moving = [stacks[from_].pop() for _ in range(how_many)]
    stacks[to].extend(moving)

msg = "".join([stack[-1] for stack in stacks])
print(msg)
