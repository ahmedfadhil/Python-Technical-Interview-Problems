# Using XOR to find a unique number in an array
numbers = [1,2,2,3,1]

answer =0
for i in range(len(numbers)):
    answer ^=numbers[i]
print(answer)