def color(a):
    b = '\u001b[' + str(a) + 'm'
    return b


def flag_thailand():
    for i in range(6):
        if i == 0 or i == 5:
            print(color(41) + '  ' * 13 + color(0))
        elif i == 1 or i == 4:
            print(color(47) + '  ' * 13 + color(0))
        else:
            print(color(44) + '  ' * 13 + color(0))


flag_thailand()
print('  ' * 20)

massive = [0, 1, 2, 4, 7, 10, 14]


def yzor():
    for i in massive:
        print(color(47) + '  ' * (15 - i) + color(40) + ' ' * 7 + color(47) + ' ' * 4 * i + color(40) + ' ' * 7 + color(
            47) + '  ' * (15 - i) + color(0))


yzor()
print('  ' * 20)


def graph():
    for i in range(9):
        print(f'{9 - i} |' + color(40) + '    ' * i + color(44) + '    ' + color(40) + '    ' * (8 - i) + color(0))
    print(f'    1/9|1/8|1/7|1/6|1/5|1/4|1/3|1/2| 1 ')


graph()
import csv

cnt_bigger_50 = cnt_less_50 = cnt = 0
with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        cnt += 1
        if cnt >= 2 and float(row[7].replace(',', '.')) > 50:
            cnt_bigger_50 += 1
        else:
            cnt_less_50 += 1
print(f'{cnt_bigger_50}-кол-во книг,цена которых более 50 руб\n{cnt_less_50}-менее 50 руб\nМасштаб диаграммы 1:1000')


def diagr():
    for i in range(1, 6):
        if i % 2 != 0:
            print('    |' + color(40) + '  ' * 10 + color(0))
        elif i == 2:
            print('>50 |' + color(46) + '  ' * (cnt_bigger_50 // 1000) + color(40) + '  ' * (
                    10 - cnt_bigger_50 // 1000) + color(0))
        elif i == 4:
            print('<50 |' + color(46) + '  ' * (cnt_less_50 // 1000) + color(40) + '  ' * (
                    10 - cnt_less_50 // 1000) + color(0))
    print(f'      1|2|3|4|5|6|7|8|9')


diagr()
import time
import os
def getdot(val):
    a=['','.','..','...']
    return a[val]
while True:
    l=0
    while l<4:
        os.system('title Loding %s'%(getdot(l)))
        os.system('cls')
        print('\n\n\n\n\t\t\tLoading%s'%(getdot(l)))
        l+=1
        time.sleep(1)