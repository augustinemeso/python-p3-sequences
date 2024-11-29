# sequences.py

def print_fibonacci(length):
    fib_sequence = []
    
    if length > 0:
        fib_sequence.append(0)
    if length > 1:
        fib_sequence.append(1)
    
    for i in range(2, length):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    
    print(fib_sequence)

# Test the function by calling it with a sample length
print_fibonacci(10)
