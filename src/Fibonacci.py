# Write a piece of code to generate a Fibonacci sequence up to a specified number of terms. 
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
# For example: 0, 1, 1, 2, 3, 5, 8, ...

sequence = [0,1]

while len(sequence) < 12:
    num = sum(sequence[-2:])
    sequence.append(num)

print(sequence)