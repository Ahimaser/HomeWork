"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

print("Задание 1.")
list_1 = ['разработка', 'сокет', 'декоратор']
for x in list_1:
    print(f"{x} - тип {type(x)}")
    print(f"{ascii(x)} - тип {type(ascii(x))}")



"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
print("Задание 2.")
list_1 = ['class', 'function', 'method']
for x in list_1:
    byte_x = bytes(x, 'utf-8')
    print(f"{x}: {byte_x} - в байтовом формате, "
          f"тип {type(byte_x)}, длина - {len(byte_x)}")


"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
print("Задание 3.")
list_1 = ['attribute', 'класс', 'функция', 'type']
for x in list_1:
    byte_x = bytes(x, 'UTF-8')
    try:
        if len(byte_x) > len(x):
            raise ValueError(
                f'Слово "{x}" невозможно записать байтовом формате')
        else:
            print(f"{byte_x} - тип {type(byte_x)}")
    except ValueError:
        print(f'Слово "{x}" невозможно записать байтовом формате')


"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
print("Задание 4.")
list_1 = ['разработка', 'администрирование', 'protocol', 'standard']
list_2 = [x.encode('utf-8') for x in list_1]
list_3 = []
for x in range(len(list_2)):
    print(list_2[x])
    list_3.append(list_2[x].decode('utf-8'))
print(list_3)


"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
print("Задание 5.")
import subprocess
import chardet


yandex = ['ping', 'yandex.ru']
yand_ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
print('yandex.ru')
for line in yand_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

youtube = ['ping', 'youtube.com']
yout_ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)
print('youtube.com')
for line in yout_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))