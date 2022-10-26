from random import randint
def get_unique_list_numbers() -> list[int]:
    arr = []
    x = 0
    while len(arr) < 15:
        x = randint(-10, 10)
        if x not in arr:
            arr.append(x)
        else:
            x = randint(-10, 10)
    return (arr)
    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
