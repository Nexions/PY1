import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(name) -> list[dict]:
    # TODO реализовать конвертер из csv в json
    with open(name, 'r') as f:                              # читаем файл csv
        s = []                                              # создаем пустой список
        for i in f.readlines():                             # читаем файл построчно
            s.append(i.split())                             # добавляем разделенную строку в список
        z = s[0]                                            # "вытаскиваем" название столбцов
        zstr ="".join(z)                                    # соединяем в строку
        zspisok = zstr.split(",")                           # делим по разделителю в список
        full = []                                           # создаем пустой список (для словарей)
        for j in range(1,len(s)):                           # перебираем все строки файла (кроме первой)
            z1 = s[j]                                       # каждый элемент строки присвваивем переменной
            z1str =''.join(z1)                              # добавляем эти элементы в строку
            z1spisok = z1str.split(",")                     # делим строку на список
            zdict = {}                                      # создаем пустой словарь
            b = 0                                           # переменная для перебора элементов списка
            for j in zspisok:                               # перебираем элементы списка (столбцов)
                zdict[j] = z1spisok[b]                      # добавляем в словарь значения (столбец - значение)
                b += 1                                      # добавляем к переменной 1, что бы перейти в следующую строку
            full.append(zdict)                              # добавляем словарь в список
        return full                                         # возвращаем список словарей

csv_to_list_dict(INPUT_FILE)
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# явно не оптимальное решение, на лучшее пока нет опыта и знаний видимо))


# import json                                               без принципа DRY =)))
#
# INPUT_FILE = "input.csv"
#
#
# def csv_to_list_dict(name) -> list[dict]:
#     # TODO реализовать конвертер из csv в json
#     with open(name, 'r') as f:
#         s = []
#         n = {}
#         for i in f.readlines():
#             s.append(i.split())
#         z = s[0]
#         zstr ="".join(z)
#         zspisok = zstr.split(",")
#         z1 = s[1]
#         z1str =''.join(z1)
#         z1spisok = z1str.split(",")
#         zdict = {}
#         b = 0
#         for j in zspisok:
#             zdict[j] = z1spisok[b]
#             b += 1
#         z2 = s[2]
#         z2str = ''.join(z2)
#         z2spisok = z2str.split(",")
#         z2dict = {}
#         c = 0
#         for k in zspisok:
#             z2dict[k] = z2spisok[c]
#             c += 1
#         z3 = s[3]
#         z3str = ''.join(z3)
#         z3spisok = z3str.split(",")
#         z3dict = {}
#         q = 0
#         for l in zspisok:
#             z3dict[l] = z3spisok[q]
#             q += 1
#         z4 = s[4]
#         z4str = ''.join(z4)
#         z4spisok = z4str.split(",")
#         z4dict = {}
#         r = 0
#         for p in zspisok:
#             z4dict[p] = z4spisok[r]
#             r += 1
#         full = []
#         full.append(zdict)
#         full.append(z2dict)
#         full.append(z3dict)
#         full.append(z4dict)
#         return full
# csv_to_list_dict(INPUT_FILE)
# print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
