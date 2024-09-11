my_dict = {'Дмитрий': 1976 , 'Олег': 1975,'Маша':1989}
print(my_dict)
print(my_dict['Олег'])
print(my_dict.get('Степан'))
my_dict.update({'Катя': 2001, 'Юля': 2005})
del my_dict['Олег']
print(my_dict)

my_set = {1,2,1,'Кинжал',2.5}
print(my_set)
my_set.update({'Персик',(0.3,8,15)})
print(my_set.discard('Кинжал'))
print(my_set)
