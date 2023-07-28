input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()

number = raw_read.split('\n')[0]
array = raw_read.split('\n')[1].split(' ')
result = 0

even_numbers = ''
not_even_numbers = ''

for i in array:
    if int(i) % 2 == 0:
        even_numbers += i + ' '
    elif int(i) % 2 != 0:
        not_even_numbers += i + ' '

result = f"{not_even_numbers}\n{even_numbers}"

if len(even_numbers.strip().split(' ')) >= len(not_even_numbers.strip().split(' ')):
    result += f"\nYES"
else:
    result += f"\nNO"

output.write(str(result).strip())
input.close()
output.close()
