def delivery(cost, other_item=None, first_item=None):
    if cost == 1:
        return first_item
    else:
        return round(first_item + other_item * (cost - 1), 2)


first_item = 10.95
other_item = 2.95
cost = int(input("Введите количество товаров: "))
print('Стоимость доставки: ', delivery(cost))
