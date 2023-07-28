input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()

numbers = raw_read.split(' ')

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
result = str(max(numbers))

output.write(result)
input.close()
output.close()
