list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_num = list_numbers[0]
for current_num in list_numbers:
    if current_num >= max_num:
        max_num = current_num
res_list_ind = list_numbers[::-1].index(max_num)  # Индекс с в перевернутом списке
ind_num = -1-res_list_ind  # Индекс искомого значения
list_numbers[ind_num] = list_numbers[-1]
list_numbers[-1] = max_num

# TODO Оформить решение

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
