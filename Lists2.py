b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = [n1 for n1 in a for n2 in b if n1 == n2]
    
print (new_list)
