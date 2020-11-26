def skip_elements(elements):
    c = 0
    newlist=[]
    for c, value in enumerate(elements, c):
        
        if c%2 ==0:
            newlist.append(value)
    return newlist


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
