file = 'provpoäng.txt'
list = []

with open(file) as f:
    for i in f:
        if len(i) > 1:
            list.append(int(i))

list.sort()

print(f"Sorterade lista: {list}")
print(f"Antal poäng i listan: {len(list)} st.")
print(f"Medelvärdet av alla poäng är: {sum(list)/len(list):.1f}")
