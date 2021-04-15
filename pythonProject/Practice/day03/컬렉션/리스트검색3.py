food_list = ['맛나피자', '새로운피자', '대왕햄버거', '군대햄버거']
pizza_count = 0
burger_count = 0
for fin in food_list:
    sel = fin[-2:]
    print(sel)

    if sel == '피자':
        pizza_count += 1
    if sel == '버거':
        burger_count += 1

print('피자가게:', pizza_count, '햄버거가게:', burger_count)

pizza = 0
ham = 0

for i in food_list:
    if '피자' in i:
        pizza += 1
    if '햄버거' in i:
        ham += 1
print('피자:', pizza)
print('햄버거', ham)