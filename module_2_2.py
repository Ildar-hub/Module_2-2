print('Введите три числа для сравнения')
first = int(input('Введите первое произвольное число: '))
second = int(input('Введите второе произвольное число: '))
third = int(input('Введите третье произвольное число: '))
if first == second and first == third and second == third:
    print(3) #Если все числа равны между собой, то вывести 3
elif first == second or first == third or second == third:
    print(2) #Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
else:
    print(0) #Если равных чисел среди 3-х вообще нет, то вывести 0