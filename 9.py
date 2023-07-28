input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()

number = raw_read.split('\n')[1].split(' ')

summary = 0
multiplication = 1

for i in range(len(number)):
    number[i] = int(number[i])
    if number[i] > 0:
        summary += number[i]

maximum = number[0]
minimum = number[0]

maximum_index = 0
minimum_index = 0

for i in range(len(number)):

    if number[i] > maximum:
        maximum = number[i]
        maximum_index = i

    if number[i] < minimum:
        minimum = number[i]
        minimum_index = i

for i in range(min(maximum_index, minimum_index) + 1, max(maximum_index, minimum_index)):
    multiplication *= number[i]

output.write(f"{summary} {multiplication}")
input.close()
output.close()
