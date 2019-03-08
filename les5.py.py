import sys, os, math 



o = os.getcwd() #текущая дериктория по расположению исходного файла



print ("*" * 50, "Task 1 Easy", "*" * 50)

cheked = os.listdir(o)

def chekDir ():

    buffer = os.listdir()

    print('^' * 50)

    print('List dir:')

    for index, element in enumerate(buffer, start=1):

        if os.path.isdir(element):

            print('{}. {}'.format(index, element))



def delete():

    i = 1

    while i < 10:

        try:

            os.rmdir("dir_{}".format(i))

            print ('Deleted of new creating dir is true')

        except FileNotFoundError:

            print ('Not found')

        i+=1



def create():

    i = 1

    while i < 10:

        try:

            os.mkdir("dir_{}".format(i))

            print ('Create new dir is true')

        except FileExistsError:

            print ('Dir is already created')

        i+=1



que1 = input("Do u wont to create new dir 1-9? print y/z: ")

if que1 == 'y':

	create()   # вот тут не нужен print - вывод будет none

	chekDir()  # просто вызывай функции - они сами вывод делают

else:

	print("OK, chek out the new dir")



que2 = input("Do u wont to deleted new dir? print y/n: ")

if que2 == 'y':

	delete()  # тут тоже не нужен print

else:

	print("OK, chek out the new dir")



print(cheked)







print ("*" * 50, "Task 2 Easy", "*" * 50)



def chekDir ():

    buffer = os.listdir()

    print('List dir:')

    for index, element in enumerate(buffer, start=1):

        if os.path.isdir(element):

            print('{}. {}'.format(index, element))



chekDir()  # и тут без print





print ("*" * 50, "Task 3 Easy", "*" * 50)



import shutil



drirect = os.getcwd()

file = os.path.basename(__file__) 

print(file, drirect)

def copyFileInWorking():  # между именем функции и скобками не надо пробела

	#for __file__ in file:  - вот тут не нужен цикл - у тебя всего один объект

	shutil.copy(file, "copyFile.py")

print(copyFileInWorking())  # что ты тут хочешь вывести? функция ничего не возвращает - вывод будет "none"





print ("*" * 50, "Task 1 Hard", "*" * 50)





import os

import sys

print('sys.argv = ', sys.argv)





def print_help():

    print("help - получение справки")

    print("mkdir <dir_name> - создание директории")

    print("ping - тестовый ключ")





def make_dir():  # сюда желательно передавать dir_name в качестве аргумента - а то из данного куска кода - не понятно что за dir_name и откуда он берется

    if dir_name is None:

        print("Необходимо указать имя директории вторым параметром")

        return

    dir_path = os.path.join(os.getcwd(), dir_name)

    try:

        os.mkdir(dir_path)

        print('директория {} создана'.format(dir_name))

    except FileExistsError:

        print('директория {} уже существует'.format(dir_name))





def ping():

    print("pong")



do = {

"help": print_help,

"mkdir": make_dir,

"ping": ping

}



try:

    dir_name = sys.argv[2]

except IndexError:

    dir_name = None



try:

    key = sys.argv[1]

except IndexError:

    key = None





if key:

    if do.get(key):

        do[key]()

    else:

        print("Задан неверный ключ")

        print("Укажите ключ help для получения справки")



# ONE DO HOME CREATE CLONE

drirect = os.getcwd()

file = os.path.basename(__file__)

print(file, drirect)





def CopyFileInWorking2 ():
	  #for __file__ in file:
		shutil.copy(file, "1.py")

qCopy = input("Create copy ur file? y/n  ")

#for qCopy in qCopy:

if qCopy == 'y':
	CopyFileInWorking2()
else:
    print("Not ur day")

chekDir()

#TWO DELETE CLONE

def sortedFileInDirect():

    path = os.getcwd()

    listFromPath = [os.path.join(path, x) for x in os.listdir(path)]

    if listFromPath:

        DateListFromPath = [[x, os.path.getctime(x)] for x in listFromPath]

        SortedList = sorted(DateListFromPath, key = lambda x: x[1], reverse=True)

        return listFromPath

##
def deleteFileSorted():

    sorted_list = sortedFileInDirect()

    os.remove(sorted_list[1])


print(sortedFileInDirect())
dFile = input("Do u wont to kill CLONE? y/n  ")

"""

def deleteFileSorted ():

	delFile = os.remove(sortedFileInDirect())

	print(delFile)



print(deleteFileSorted())

"""

#for dFile in dFile:

if dFile == 'y':

    deleteFileSorted()

	#else: - нет смысла - если не отработает if - и так будет бездействие

		#pass