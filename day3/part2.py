from itertools import islice
from string import ascii_letters

priorities = {char: priority for priority, char in enumerate(ascii_letters, start=1)}


def chunkify(iterable, size):
    it = iter(iterable)
    while chunk := tuple(islice(it, size)):
        yield chunk


priorities_sum = 0
with open("input.txt") as f:
    for group in chunkify(f, 3):
        badge = set.intersection(*[set(rucksack.strip()) for rucksack in group]).pop()
        priorities_sum += priorities[badge]
print(priorities_sum)
