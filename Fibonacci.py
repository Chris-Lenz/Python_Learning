
def fib(len):
    seq = [1,1]
    n = 0
    while n < len:
        sum = seq[-1] + seq[-2]
        seq.append(sum)
        n += 1
    return seq
print(fib(int(input("Enter a length of the sequence: "))))
