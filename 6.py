input = open('input.txt', 'r')
output = open('output.txt', 'w')

raw_read = input.read()

str = raw_read
temp_array = []

if len(str.strip()) == 5:

    for i in str:
        temp_array.append(ord(i))

    if (65 <= temp_array[0] <= 72) and (49 <= temp_array[1] <= 56) and (65 <= temp_array[3] <= 72) and (49 <= temp_array[4] <= 56) and (temp_array[2] == 45):
        a1 = temp_array[0] + 2
        a2 = temp_array[0] - 2
        a3 = temp_array[0] + 1
        a4 = temp_array[0] - 1

        b1 = temp_array[1] + 2
        b2 = temp_array[1] - 2
        b3 = temp_array[1] + 1
        b4 = temp_array[1] - 1

        if ((a1 == temp_array[3] or a2 == temp_array[3]) and (b3 == temp_array[4] or b4 == temp_array[4])) or ((a3 == temp_array[3] or a4 == temp_array[3]) and (b1 == temp_array[4] or b2 == temp_array[4])):
            result = "YES"
        else:
            result = "NO"
    else:
        result = "ERROR"
else:
    result = "ERROR"


output.write(result)
input.close()
output.close()
