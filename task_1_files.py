'''Задача №1
Должен получится следующий словарь'''
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
    print(cook_book)
    # print(len(cook_book))
    # print(type(cook_book))

with open('cook_book.json', 'w', encoding='utf-8') as f :
    json.dump(cook_book, f, indent=3)
with open('cook_book.json', 'r') as f :
     data = json.load(f)