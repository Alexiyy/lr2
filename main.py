import math

a = int(input('Введите a:\n'))
b = int(input('Введите b:\n'))
c = int(input('Введите c:\n'))

if a < 0:
    print ('Переменная "a" не может быть меньше нуля, введите заново:\n')
    a = int(input())

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    x1 = (-b - math.sqrt(discriminant)) / (2*a)
    x2 = (-b + math.sqrt(discriminant)) / (2*a)
    print ('Первый корень: '+str(x1)+'\nВторой корень: '+str(x2))

elif discriminant == 0:
    x1 = -b / 2*a
    print('В данном уравнении только один корень, он равен: '+str(x1))

elif discriminant <= 0:
    print ('Корней нет.')
