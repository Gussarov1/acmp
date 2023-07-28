input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()
number = int(raw_read)
result = 0

result = f"{number}9{9-number}"

output.write(str(result))
input.close()
output.close()
