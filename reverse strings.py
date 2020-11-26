def reverse_list(sentence):
    newstring = sentence.split()
    newstring.reverse()
    result = " ".join(newstring)
    return result
sent = input("Type a sentence: ")
print(reverse_list(sent))

