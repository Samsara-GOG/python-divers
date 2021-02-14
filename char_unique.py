letters = ["A","D", "A", "B", "C", "A", "D", "B", "D", "C", "E"]

def remove_duplicates(test):
    dupli = []
    for i in test:
        if i not in dupli:
            dupli.append(i)
    dupli.sort()
    return dupli

print(remove_duplicates(letters))
