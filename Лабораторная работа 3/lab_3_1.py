src = not False and True or False and not True

# TODO расписать упрощение выражения
src = True and True or False and False # True and True or False and False
src = True or False # True or False
src = True # True
result = src  # TODO подставить результат выражения

print(src == result)
