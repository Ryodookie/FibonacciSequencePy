# Write a function to generate a Fibonacci sequence up to a specified number of terms. 

def listElements(length):
    sequence = [0,1]
    
    while len(sequence) < length:
        num = sum(sequence[-2:])
        sequence.append(num)

    return sequence

iterationNumber = 12
fibonacciSequence = listElements(iterationNumber)

print(fibonacciSequence)