

with open("day-002/input.txt", "r") as file:
    pz_input = file.readlines()

outcome_score = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

loses_config = {
    "A": "C",
    "B": "A",
    "C": "B",
}

wins_config = {
    v: k for k, v in loses_config.items()
}

shape_score = {
    "A": 1,
    "B": 2,
    "C": 3,
}

total_score = 0

for item_index in range(0, len(pz_input)):
    item = pz_input[item_index].rstrip("\n")
    if item[2] == "X":
        result_shape_score = shape_score[loses_config[item[0]]]
    elif item[2] == "Y":
        result_shape_score = shape_score[item[0]]
    elif item[2] == "Z":
        result_shape_score = shape_score[wins_config[item[0]]]
    result_round_score = outcome_score[item[2]]
    total_score += result_shape_score + result_round_score

print(total_score)
