

with open("day-001/input.txt", "r") as file:
    pz_input = file.readlines()

reindeer_collected = []
one_reindeer = []
for item in pz_input:
    if item != '\n':
        one_reindeer.append(int(item.rstrip("\n")))
    else:
        reindeer_collected.append(one_reindeer)
        one_reindeer = []

max_reindeer = max([sum(reindeer) for reindeer in reindeer_collected])

print(max_reindeer)
