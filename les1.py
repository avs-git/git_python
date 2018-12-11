# UTF-8

import os
import sys
import shutil
import psutil     # сторонний


def file_remove(filename, filedir):
    if filedir == '': filedir = '.'
    full_name = os.path.join(filedir, filename)
    if os.path.exists(full_name):
        os.remove(full_name)
        print('Удалён' + str(full_name))
        return True
    else:
        print('Нет такого файла' + str(full_name))
        return False
    
def fileRemoveCount(filelist, filedir, count = 0):
    deleted_count = 0
    print(type(filelist))
    print('len=' + str(len(filelist)))
    if count == 1:
        file_remove(filelist, filedir)
        deleted_count += 1
    else:
        for f in filelist:
            file_remove(f, filedir)
            deleted_count += 1
    print("Мы старались. Удалено " + str(deleted_count) + " файлов")

def main():
    answer2 = ''

    while answer2.lower() != "q":
        print('\n1. Список файлов')
        print('2. Инфа по системе')
        print('3. Сдублировать файлы')
        print('4. Удалить какой-нибудь файл')
        print('5. Удалить дубликаты')
        print('-' * 8)
        print('q - выход')
        answer2 = input("\nВыбор: ")
        if answer2 == "1":
            print(os.listdir())
        elif answer2 == "2":
            print('uptime: ', psutil.boot_time())
            print('ядер: ', os.cpu_count())
            print('частота: ', psutil.cpu_freq())
            print('Пользователь: ', os.getlogin())
            print('вин: ', sys.getwindowsversion().major)
        elif answer2 == "3":
            print("Дублируем")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                new_file_name = file_list[i] + '.dupl'
                shutil.copy(file_list[i], new_file_name)
                i += 1
        elif answer2 == "4":  # удаление одного файла
            file_list = os.listdir()
            print("Удаляем")
            print('список файлов: ' + str(file_list))
            dir_to_remove = input("Директория для удаления: ")
            file_to_remove = input("Имя файла для удаления: ")
            fileRemoveCount(file_to_remove, dir_to_remove, 1)


        elif answer2 == "5":  # удаление дубликатов
            dir_to_remove = input("Директория для очистки дубликатов: ")
            if dir_to_remove == '': dir_to_remove = '.'
            file_list = os.listdir(dir_to_remove)
            deleted_count = 0
            dupl_list = list(filter(lambda x: x.endswith('.dupl'), file_list))

            fileRemoveCount(dupl_list, dir_to_remove)
            file_list = os.listdir()
            print("\nновый список: " + str(file_list))
        else:
            print("не попал по кнопкам")

if __name__ == "__main__":
    main()


