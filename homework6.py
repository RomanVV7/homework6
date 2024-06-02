#работа со словарями
my_dict = {'Roman':1989,'Artem':1990,'Nadezda':1995}
print(my_dict)
my_dict['Arina'] = 2012 #добавили новую пару в словарь
print(my_dict['Roman'])
print(my_dict['Arina'])
my_dict.update({'Max' : 1991,'Slava' : 1988}) #добавили 2 новые пары
print(my_dict)
print(my_dict.pop('Roman')) #вывели из словарю пару и вывели ее значение на экран
print(my_dict)

#работа с множествами
my_set = {1,3,5,7,3,1,9}
print(my_set)
my_set.update({11,13})  #добавили 2 элемента в множество
my_set.remove(3) #удалили 1 элемент
print(my_set)
