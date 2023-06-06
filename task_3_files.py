'''Задача №3
В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны, пример для выполнения домашней работы можно взять тут

Необходимо объединить их в один по следующим правилам:
- Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
- Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем'''
with open('1.txt', 'r', encoding='utf-8') as f :
    text_1 = f.readlines()
    text_1.insert(0, f'{len(text_1)}\n')
    text_1.insert(0, '1.txt\n')
with open('2.txt', 'r', encoding='utf-8') as f :
    text_2 = f.readlines()
    text_2.insert(0, f'{len(text_2)}\n')
    text_2.insert(0, '2.txt\n')
with open('3.txt', 'r', encoding='utf-8') as f :
    text_3 = f.readlines()
    text_3.insert(0, f'{len(text_3)}\n')
    text_3.insert(0, '\n3.txt\n')

all_lis = []
all_lis += text_1, text_2, text_3
all_lis.sort(key=len)

with open('all_text.txt', 'a', encoding='utf-8') as f :
    for one_text in all_lis :
        for one_string in one_text :
            f.write(one_string)






# # for last_string in all_lis :
# #     last_string[-1].strip()
# #     last_string[-1] += '\n'        
# # print(all_lis)

