win = 6
draw = 3
loss = 0

rock = 1
paper = 2
scissors = 3

shapes = {
    "A": rock,
    "B": paper,
    "C": scissors,
}

advised_outcomes = {
    "X": loss,
    "Y": draw,
    "Z": win,
}

outcomes = {
    win: {
        rock: paper,
        paper: scissors,
        scissors: rock,
    }
}
outcomes[loss] = {v: k for k, v in outcomes[win].items()}


def get_advised_shape(opponent_shape, advised_outcome):
    if advised_outcome == draw:
        return opponent_shape
    return outcomes[advised_outcome][opponent_shape]


total_score = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        opponent_shape, _, advised_outcome = line.partition(" ")

        opponent_shape = shapes[opponent_shape]
        advised_outcome = advised_outcomes[advised_outcome]

        my_shape = get_advised_shape(opponent_shape, advised_outcome)

        total_score += my_shape
        total_score += advised_outcome

print(total_score)
