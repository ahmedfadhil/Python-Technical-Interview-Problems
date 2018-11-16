# appraoach 1: using Python's "bin" function
num = 5
one_sum = 0
bin_rep = bin(num)[2:]

for i in bin_rep:
    one_sum += int(i)
print(one_sum)

# appraoach 2: without Python's "bin" function
num = 5
one_sum = 0
while num:
    one_sum += num & 1
    num >>= 1
print(one_sum)
