# В файле находиться N натуральных чиселзаписанных через пробел,
# среди чисел не хватает одного чтобы выполнить условие A[i] - 1 = A[i-1]. 
# # Найдите это число.

# with open('test.txt', 'r') as file:
#     a = list(map(int, file.read().split()))
#     for i in range(len(a) - 1):
#         if a[i] + 1 != a[i + 1]:
#             print(a[i] +1)

# Дан список чисел. Создайте список, в который попадают числа, описываемые 
# возрастающую последовательность. Порядок элементов менять нельзя.

# def f2():
#     lst = [1, 5, 2, 3, 4, 6, 1, 7]
#     lst_result = list()
#     for i in range(len(lst)):
#         current_lst = list()
#         current_lst.append(lst[i])
#         for j in range(i +1, len(lst)):
#             if current_lst[-1] < lst[j]:
#                 current_lst.append(lst[j])
#         lst_result.append(current_lst)
#     for i in lst_result:
#         print(*i)
                   
# f2()

# Напишите программу удаляющую из текста все слова содержащие "абв".

# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')


# Домашнее задание

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# import random

# name1 = input('Введите имя игрока 1: ')
# name2 = input('Введите имя игрока 2: ')
# igrok = random.randrange(1, 3)
# a = int(input('Введите колличество конфет: '))
# if igrok == 1:
#     print('Первый ход делает', name1)
# else:
#     print('Первый ход делает', name2)
# while a > 0:
#     if a > 28:
#         igrok1 = int(input('Ты можешь взять не больше 28 конфет, сколько конфет ты взял? '))
#         a = a - igrok1
#         if a > 28:
#             igrok2 = int(input('Ты можешь взять не больше 28 конфет, сколько конфет ты взял? '))
#             a = a - igrok2
#             if a <= 28:
#                 if igrok == 1:
#                     print('Осталось', a, 'штук, их забирает', name1, 'а значит победил', name1)
#                 else:
#                     print('Осталось', a, 'штук, их забирает', name2, 'а значит победил', name2)
#         else:
#             if igrok == 1:
#                 print('Осталось', a, 'штук, их забирает', name2, 'а значит победил', name2)
#             else:
#                 print('Осталось', a, 'штук, их забирает', name1, 'а значит победил', name1)

  

# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""

# from random import *
# import os

# def player_vs_bot():
#     candies_total = 2021
#     max_take = 28
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = 'Компьютер'
#     players = [player_1, player_2]
#     print(f'\nИграют {player_1} и  {player_2}.\n')
#     print('\nОпеределим кто первый начнет игру.\n')

#     lucky = randint(-1, 0)

#     print(f'{players[lucky+1]} ты ходишь первым !')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(f'\nХодит {players[lucky%2]}. \n: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\n Ну чтож ходи,  {players[lucky % 2]} \nНа кону {candies_total}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step

#     print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()
# Создайте программу для игры в ""Крестики-нолики"".

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('file_encode.txt', 'w') as data:
#     data.write('wwwwwwwwwwwwwwdddddddddddaaaaaaaaaaaffgggggggggghhhhhhhhh')

# with open('file_encode.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')