def get_count_char(str_):
    str_clear = ''.join(str_.lower().split())
    slovarik = {}
    for i in str_clear:
        if i.isalpha():
            slovarik[i] = str_clear.count(i)
    return(slovarik)

def get_count_chars(str_):
    str_clear = ''.join(str_.lower().split())
    slovarik = {}
    for i in str_clear:
        if i.isalpha():
                a = str_clear.count(i)
                slovarik[i] = round(a * 100 / len(str_clear), 1)
    return (slovarik)

    # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_count_chars(main_str))