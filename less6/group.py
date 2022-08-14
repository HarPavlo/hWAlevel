studentlist = ["Adam Scott", "Kayden Ross", "Hugo Davis", "Declan James", "Javier Collins", "Darius Butler",
               "Nikolas Young", "Judah Watson", "Princeton Jackson", "Anderson Richardson", "Grayson James",
               "Iver Carter", "Quenton Jackson", "Willis Evans", "Patton Kelly", "Saul Watson"]

group = {
    "Python": [],
    "FrontEnd": [],
    "FullStack": [],
    "Java": []
}

for m, j in enumerate(group.keys()):
    print(m + 1, "group - ", j)
for i in studentlist:
    group.setdefault(input(f"choose a group for a student {i}: "), []).append(i)
    group.setdefault(input(f"choose a group2 for a student {i}, else press enter: "), []).append(i)
    group.setdefault(input(f"choose a group3 for a student {i}, else press enter: "), []).append(i)
    group.setdefault(input(f"choose a group4 for a student {i}, else press enter: "), []).append(i)
for key, val in group.items():
    group.update({key: list(set(val))})
group.update({"": []})
_ = group.pop("")
for key, val in group.items():
    print(key, ': ', val)

grp = []
for val in group.values():
    grp += val
print("Students who study in several groups:        ", [n for n in studentlist if grp.count(n) >= 2])

print("Students not study on the group FrontEnd:    ", [n for n in studentlist if n not in group["FrontEnd"]])

print("Students study on the group Python or Java: ", list(set(group["Python"] + group["Java"])))
