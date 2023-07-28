input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()
numbers = raw_read.split(' ')
result = ""

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

for i in range(-100, 101):

    if a * (i * i * i) + b * (i * i) + c * i + d == 0:
        result += str(i) + " "

result = result.strip()

output.write(result)
input.close()
output.close()
