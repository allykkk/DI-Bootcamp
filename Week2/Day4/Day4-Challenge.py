matrix_string = "7i3 Tsi h%x i # sM  $a  #t% ^r! "

matrix_list = []
for i in range(0, len(matrix_string), 4):
    matrix_list.append(matrix_string[i:i + 4])
# print(matrix_list)

# If do not care about space
whole_message = ""
for j in range(3):
    column_message = ""
    for item in matrix_list:
        if item[j].isalpha():
            column_message += item[j]
    whole_message = whole_message + column_message
print(whole_message)

# -----------------------------------------------------------------
# If we care about space
whole_message2 = ""
for j in range(3):
    column_message = ""
    for item in matrix_list:
        column_message += item[j]
    whole_message2 = whole_message2 + column_message
# print(whole_message2)

final_result = ""
group_size = 0
for char in whole_message2:
    if char.isalpha():
        if group_size == 2:
            final_result += " "
        group_size = 0
        final_result += char
    else:
        if group_size == 2:
            continue
        else:
            group_size += 1

print(final_result)
