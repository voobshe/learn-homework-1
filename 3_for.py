"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов

* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

# def main():
# """
#     Эта функция вызывается автоматически при запуске скрипта в консоли
#     В ней надо заменить pass на ваш код
#     """
#     pass
    
# if __name__ == "__main__":
#     main()

sales =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_average(solded_items):
    items_sum = 0
    for items in solded_items:
        items_sum += items
    solded_items_avg = items_sum / len(solded_items)
    return solded_items_avg, items_sum

def main():
# 
    total_product_sales = 0 
    all_products_solded_avg = 0



    for one_product in sales:
        one_product_solded_avg, one_product_solded_total = count_average(one_product['items_sold'])
        print(f"Суммарное количество продаж {one_product['product']} {one_product_solded_total}, а среднее количество проданных {one_product['product']} {int(one_product_solded_avg)}")
        total_product_sales += one_product_solded_total
        all_products_solded_avg += one_product_solded_avg

    print(f"Суммарное количество продаж всех товаров {total_product_sales}, среднее количество продаж всех товаров {int(all_products_solded_avg/ len(sales))} ")

if __name__ == "__main__":
    main()