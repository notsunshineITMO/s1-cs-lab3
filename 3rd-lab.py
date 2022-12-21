import re
from random import randint

print('--------------------------------------------\nЗАДАНИЕ 1\n--------------------------------------------\n')
'''
        ЗАДАНИЕ 1 (60 баллов)
                                '''
# :<O
eyes = ':;X8='
noses = '-<-{<{'
mouths = r'()O|\/P'
pattern = ':<O'


def smile_gen(element):
    n = randint(0, len(element) - 1)
    return element[n:n + 1:] if element[n:n + 1:] != '{' else element[n - 1:n:] + element[n:n + 1:]


def test1():
    global pattern
    # Test
    for n in range(5):
        print(f'TEST #{n + 1}')
        test_string = ''
        # Создание строки с n количеством смайликов
        for i in range(randint(100, 2500)):
            test_string += smile_gen(eyes) + smile_gen(noses) + smile_gen(mouths)
        print('Строка: ', test_string)
        check_by_count = test_string.count(pattern)
        check_by_re_findall = len(re.findall(pattern, test_string))
        msg = f'В строке содержится {check_by_re_findall} смайликов ":<O" ' + f'- Test {n + 1} is okay.' if check_by_count == check_by_re_findall else f'- Test {n + 1} is false.'
        print(msg, '\n')


test1()

print('--------------------------------------------\nЗАДАНИЕ 2\n--------------------------------------------\n')
'''
        ЗАДАНИЕ 2 (18 баллов)
                                '''
# isu % 6 = 3
test_texts = [
    'Студент Вася вспомнил, что на своей лекции Балакшин П.В. упоминал про старшекурсников, которые будут ему помогать: Анищенко А.А. и Машина Е.А.',
    'Можете вписать имя знаменитого джаваненавистника и любителя поспрашивать про jvm- Петренко Н.А.',
    'Меня зовут Правдин К.В., я преподаватель НОЦ Математики в Университете ИТМО.',
    'В группе P3121 учатся Махмудова М.А., Логунова А.А., Митина Т.О. и другие.',
    'В ГКЧП входили Крючков В.А., Янаев Г.И., Бакланов О.Д., Павлов В.С, Пуго Б.К., Стародубцев В.А., Тизяков А.И. и Язов Д.Т..']


def test2():
    for n in range(5):
        print(f'TEST #{n + 1}')
        print('Предложение:', test_texts[n])
        match = re.findall(r'[А-ЯЁ]\w+\W\w.\w\W', test_texts[n])
        match.sort()
        for last_name in match:
            print(last_name[:-4:])
        print()


test2()

print('--------------------------------------------\nЗАДАНИЕ 3\n--------------------------------------------\n')
'''
        ЗАДАНИЕ 3 (22 балла)
                                '''
# isu % 4 = 1
test_texts = [
    'Классное слово – обороноспособность, которое должно идти после слов: трава и молоко.',
    'Король провёл публичную казнь на глазах у всех.',
    'Ворон сидел в траве и клевал кукурузу.',
    'Работа не волк, волк это ходить, работа это ворк.',
    'Крысы любят сыр, но не любят котов.'
]

def test3():
    for n in range(5):
        print(f'TEST #{n + 1}')
        print('Предложение:', test_texts[n])
        vowels = 'аеёиоуыэюя'  # vowels
        co = 'б-джзй-нп-тф-ъь'  # consonants and other
        reg = []
        for i in range(len(vowels)):
            reg.append('[' +co+ ']*(?:' +vowels[i]+ '[' +co+']*)*' +vowels[i]+ '[' +co+ ']*')
        #print(reg)
        match = re.findall(r'\b('+"|".join(reg)+r')\b', test_texts[n], re.I)
        match.sort(key=len)
        for word in match:
            print(word)
        print()

test3()
