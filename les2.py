import math
import os
import psutil
import sys
import shutil

#Task1 easy

a = ["Анонас", "Яблоко", "Киви", "Банан", "Абрикос"]
#line_new = '{:>12} {:>12} {:>12} {:>12} {:>12}'.format(a[0], a[1], a[2], a[3], a[4])
#line_new = '{:>12}  {:>12}  {:>12}'.format(a[0], a[1], a[2])
#for line_new in a:
 #   print('{:12g}'.format(a))
#пол дня всяких стремных решений
i = ''
for i, a in enumerate(a):
	print(i + 1, '{:>15}'.format(a[0:]))


#Task2 easy
#from itertools import groupby
b = ["1", "6", "3", "4", "5"]
c = ["1", "3", "4"]
#new_x = [el for el, _ in groupby(b,c)]
#doubles = []
#for i, elem in enumerate(b + c):
 #   if i != 0:
  #      if elem == old:
   #         doubles.append(elem)
    #        old = None
     #       continue
    #old = elem
    #print(doubles)
result=list(set(b) - set(c))
print(result)

#Task 3 easy
o = [1, 2, 3, 4, 5]
pop = []
for i in o:
	if i % 2 == 0:
		pop.append(i / 4)
	else:
		pop.append(i * 2)
print(pop)
o2 = [234, 21221, 1124512, 22312567]
pop2 = []
pop2 = [i / 4 if i % 2 == 0 else i * 2 for i in o2]
print(pop2)

numbersSame = int(input('Enter same numbers: '))
listNumbers = []
for el in range(numbersSame):
	listNumbers.append(.randint('-100', '100'))
print(listNumbers)

#Task 1 hard

first = int(input("Напишите день: "))
if first > 32:
	print("un correct main")
	False
else:
	True
	pass




second = int(input("Введите месяц: "))
if second > 12:
	print("un correct main")
	False
else:
	pass
	True
third = int(input("Введите год: "))
if third < 1910:
	print("un correct main")
	False
	if third > 2019:
		print("un correct main")
		False
else:
	True
	pass

date = [first, second, third]
print(first, second, third)


#Task 1 NORMAL
import math
numb = [4, 10, 22, -20, 119, 17, 8]
result = [int(i) for i in range(max(numb)) if int(i) ** 2 in numb]
print(result)

numbers = [4, 10, 22, -20, 119, 17, 8]
result = [int(math.sqrt(i)) for i in numbers if i > 0 and math.sqrt(i).is_integer()]
print(result)

numbers = [4, -5, 80, 9, -25, 25, 4]
result = [int(i) for i in range(max(numbers)) if int(i) ** 2 in numbers]
print(result)


#Task2 NORMAL 

from datetime import datetime
d = input('Enter a date(mm/dd/yyy)')
d = datetime.strptime(d, "%m/%d/%Y")
print(d.strftime("%B %d, %Y")) 
#Only works in English

#var2
strong_date = input('Enter the date form: dd.mm.yyyy: ')
#strong_date = '22.04.2015' if we needs to do task from specific date
dateList = strong_date.split('.')
slovM = {
'01': 'января',
'02': 'феврал',
'03': 'марта',
'04': 'апреля',
'05': 'мая',
'06': 'июня',
'07': 'июля',
'08': 'августа',
'09': 'сентября',
'10': 'октября',
'11': 'ноября',
'12': 'декабря',
}
slovD = {
'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
'06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
'11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
'16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
'21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
'25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
'29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое',
}
for key in slovD:
	if dateList[0] == key:
		dateList[0] = slovD[key]

for key in slovM:
	if dateList[1] == key:
		dateList[1] = slovM[key]

comp = dateList[0] + ' ' + dateList[1] + ' ' + dateList[2] + ' ' "года"
print(comp)

#Task3 NORMAL

numbersSame = int(input('Enter same numbers: '))
listNumbers = []
for el in range(numbersSame):
	listNumbers.append(random.randint('-100', '100'))
print(listNumbers)
