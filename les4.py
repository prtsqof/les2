import re, sys, os, random, copy


#Task 1 Eeasy
print("." * 50, "task 1 Easy", "." * 50)

a = random.sample(range(10), 5) #Получаем случайный список из чесел в пять элементов
print(a, "List random")

b = [i*i for i in a] #Возводим случайный список из a в квадратный корень
print(b, "Result")

#Tast 2 Easy
print("." * 50, "task 2 Easy", "." * 50)
"""
first_fruit = ["Апельсин", "Ранетки", "Фазалис", "Дыня", "Слива", "Авакадо", "Мандарин", "Арбуз", "Черри", "Папайа", "Яблоко", "Киви"]
print(len(first_fruit))
print(first_fruit[1])

"""

list1 = ["Апельсин", "Ранетки", "Фазалис", "Дыня", "Слива", "Авакадо", "Мандарин", "Арбуз", "Черри", "Папайа", "Яблоко", "Киви"]
"""
randomNumb = 6
random = random.sample(list1, randomNumb)
list2 = random
list3 = random
print(list2)
print(list3)
"""

list2 = list(set(list1[:6]))
list3 = list(set(list1[:6]))

print(list2)
print(list3)


#Task 3 Easy
print("." * 50, "task 3 Easy", "." * 50)

items = list(range(-100, 100))
#random.shuffle(items)
print(items, "*" * 10, "item generate")

itemNew = []
for i in items:
	if i % 3 == 0:
		itemNew.append(i)
	elif i > 0:
		itemNew.append(i)
	elif i % 4 != 0:
		itemNew.append(i)
	else:
		pass
		

print(itemNew, "*" * 10, "item task")