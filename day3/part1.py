from string import ascii_letters

priorities = {char: priority for priority, char in enumerate(ascii_letters, start=1)}

priorities_sum = 0
with open("input.txt") as f:
    for rucksack in f:
        rucksack = rucksack.strip()
        compartment1 = set(rucksack[len(rucksack) // 2 :])
        compartment2 = set(rucksack[: len(rucksack) // 2])
        duplicated_type = compartment1.intersection(compartment2).pop()
        priorities_sum += priorities[duplicated_type]
print(priorities_sum)
