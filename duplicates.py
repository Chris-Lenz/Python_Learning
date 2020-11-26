
def dupl(list):
    newlist = []
    for item in list:
        if item not in newlist:
            newlist.append(item)
    return newlist


print(dupl([3,54,234,54,23,3,432,432]))
print(dupl(["cherry", "apple", "cherry", "melon", "apple"]))
