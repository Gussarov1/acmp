input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()
numbers = raw_read.split(' ')
result = 0

if (int(numbers[0]) * int(numbers[1])) == int(numbers[2]):
    result = "YES"
else:
    result = "NO"

output.write(result)
input.close()
output.close()
