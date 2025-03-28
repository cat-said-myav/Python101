

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def find_items(items_list, item):
    if item in items_list:
        return items_list.index(item)


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_items(items_list,find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
