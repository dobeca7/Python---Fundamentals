importance = []
while True:
    to_do_notes = input()
    if to_do_notes == "End":
        break
    notes = to_do_notes.split("-")
    priority = int(notes[0])
    task = notes[1]
    importance.append([priority, task])

sorted_importance = []
for tasks in sorted(importance):
    sorted_importance.append(tasks[1])
print((sorted_importance))


