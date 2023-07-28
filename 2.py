input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()
number = int(raw_read)

result = 0

if number >= 1:
    for i in range(1, number + 1):
        result += i
else:
    for i in range(number, 2):
        result += i

output.write(str(result))
input.close()
output.close()