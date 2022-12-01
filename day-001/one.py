

with open("day-001/input.txt", "r") as file:
    pz_input = file.readlines()

reindeer_collected = []
one_reindeer = []
for item_index in range(0, len(pz_input)):
    if item_index == len(pz_input) - 1:
        one_reindeer.append(int(pz_input[item_index].rstrip("\n")))
        reindeer_collected.append(one_reindeer)
        one_reindeer = []
    elif pz_input[item_index] == "\n":
        reindeer_collected.append(one_reindeer)
        one_reindeer = []
    else:
        one_reindeer.append(int(pz_input[item_index].rstrip("\n")))


max_reindeer = max([sum(reindeer) for reindeer in reindeer_collected])

print(max_reindeer)
