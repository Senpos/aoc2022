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
    "X": rock,
    "Y": paper,
    "Z": scissors,
}

win_outcomes = {
    rock: paper,
    paper: scissors,
    scissors: rock,
}


def get_winner(me, opponent):
    if me == opponent:
        return draw
    if win_outcomes[me] == opponent:
        return loss
    return win


total_score = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        opponent, _, me = line.partition(" ")

        me = shapes[me]
        opponent = shapes[opponent]

        score = get_winner(me, opponent)
        total_score += me
        total_score += score

print(total_score)
