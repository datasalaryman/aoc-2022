

with open("day-002/input.txt", "r") as file:
    pz_input = file.readlines()

shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

round_score = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

total_score = 0

for item_index in range(0, len(pz_input)):
    item = pz_input[item_index].rstrip("\n")
    result_shape_score = shape_score[item[2]]
    result_round_score = round_score[item]
    total_score += result_shape_score + result_round_score

print(total_score)
