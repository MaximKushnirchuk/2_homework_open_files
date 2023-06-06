'''Задача №2
Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
get_shop_list_by_dishes(dishes, person_count)
На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
Обратите внимание, что ингредиенты могут повторяться'''

from pprint import pprint
with open('recipes.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    for dishes in f :
         num = int(f.readline())
         list_deash = []
         for i in range(num) :
              eat, colvo, ed_izmer = f.readline().strip().split(' | ')
              list_deash += [{'ingredient_name' : eat, 'quantity' : colvo, 'measure' : ed_izmer}]
         cook_book[dishes.strip()] = list_deash
         f.readline()

def get_shop_list_by_dishes(dishes, person_count) :
    '''Функция выдает словарь с названием ингредиентов и его количества для блюда'''        
    res = {}
    for one_deash in dishes :
        for product in cook_book[one_deash] :
            if product['ingredient_name'] not in res :
                res[product['ingredient_name']] = {'measure' : product['measure'], 'quantity' : int(product['quantity'])*person_count}
            else : res[product['ingredient_name']]['quantity'] += (int(product['quantity'])*person_count)
    return pprint(res)

'''Проверка работы функции get_shop_list_by_dishes'''
list_deash = ['Фахитос']
get_shop_list_by_dishes(list_deash, 2)
print('-'*25)
list_deash = ['Омлет']
get_shop_list_by_dishes(list_deash, 3)
print('-'*25)
list_deash = ['Фахитос', 'Омлет']
get_shop_list_by_dishes(list_deash, 4)


