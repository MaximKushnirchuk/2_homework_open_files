'''Задача №1'''

import json
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
res = json.dumps(cook_book, indent=2)
print(res)