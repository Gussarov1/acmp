input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()
numbers = raw_read.split(' ')
result = int(numbers[0]) + int(numbers[1])

output.write(str(result))
input.close()
output.close()
