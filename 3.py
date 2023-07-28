input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()
number = int(raw_read)
result = 0

result = number // 10

if (result*(result+1) == 0):
    result = 25
else:
    result = f"{result * ( result+1 )}25"

output.write(str(result))
input.close()
output.close()
