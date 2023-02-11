# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n, m = int(input('Введите число N: ')), int(input('Введите число M: '))
# lst_n = list(int(input(f"Введите элемент первого списка чисел {i + 1}: ")) for i in range(n))
# lst_m = list(int(input(f"Введите элемент второго списка чисел {i + 1}: ")) for i in range(m))
# print(f'Список N: {lst_n}')
# print(f'Список M: {lst_m}')
# lst_x = list(e for e in lst_n if e in lst_m)
# print(sorted(set(lst_x)))



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# n = int(input("Введите количество кустов: "))
# list_berry = list(int(input("Введите количество ягод на кустах: ")) for i in range(n))
# list_berry = list_berry + list_berry[:2]
# max_berry = 0
# for i in range(n):
#     max_berry = max( max_berry, list_berry[i] + list_berry[i+1] + list_berry[i+2] )
# print("Максимально количество собранных ягод:", max_berry)