"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def sum_of_sale(items_sold):
      sum_sale=0
      for item in items_sold:
           sum_sale = sum_sale + item
      sum_sale_avg = sum_sale/len(items_sold)
      return sum_sale, sum_sale_avg

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    all_sum_of_phones=0
    all_sum_avg_phones=0
    for one_phones in phones:
        sum_of_phones, avg_sum_of_sales = sum_of_sale(one_phones['items_sold'])
        all_sum_of_phones+=sum_of_phones
        all_sum_avg_phones+=avg_sum_of_sales
        print(f'сумма продаж {one_phones["product"]}: {sum_of_phones}')
        print(f'средняя сумма продажb {one_phones["product"]}: {round(avg_sum_of_sales,2)}')
    print(f'Cуммарное количество продаж всех тeлефонов: {all_sum_of_phones}')
    print(f'Cреднее количество продаж всех телефонов: {round(all_sum_avg_phones/len(phones),2)}')



if __name__ == "__main__":
    main()
