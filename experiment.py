Array = ["x","o","o","x","x","x"]

hits = 0

for item in Array:
    if item == "x":
        hits += 1
    else:
        continue

print(hits)

