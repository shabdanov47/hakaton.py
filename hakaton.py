           #задача:1:
"""
o= input('''
Введите математическую операцию, которую вы хотите выполнить:
+ для сложения
- на вычитание
* для умножения
/ для деления
''')

n_1=int(input("введите цифру 1: "))
n_2=int(input("введите цифру 2: "))

if o== "+":
	print('{}+{}='.format(n_1,n_2))
	print(n_1+n_2)
elif o=="-":
	print('{}-{}='.format(n_1,n_2))
	print(n_1-n_2)
elif o=="*":
	print('{} * {} = '.format(n_1, n_2))
	print(n_1 * n_2)
elif o=="/":
	print('{} / {} = '.format(n_1, n_2))
	print(n_1 / n_2)
	if n_1==0 or n_2==0:
		print('{} / {} = '.format(n_1, n_2),"деление на ноль невозможен")

else:
	print("не правильный оператор,попробуйте еще раз")
	"""
	               #задача:3:
'''
n=int(input("введите одну сторону квадрата: "))
s=n*4
print("площадь квадрата",s)
'''
                  #задача:2:
'''A=5
B=4
C=6
n=(A+B+C)
A=A+B
B=C-A
C=n
print(A,B,C)'''
                #задача#4
'''sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
a=set(sequence_0)
if len(sequence_0)==len(a):
	print("все элементы уникальны")
else:
	print("Последовательность не уникальна.")
b=set(sequence_1)
if len(sequence_1)==len(b):
	print("все элементы уникальны")
else:
	print("Последовательность не уникальна.")
c=set(sequence_2)
if len(sequence_2)==len(c):
	print("все элементы уникальны")
else:
	print("Последовательность не уникальна.")
d=set(sequence_3)
if len(sequence_3)==len(d):
	print("все элементы уникальны")
else:
	print("Последовательность не уникальна.")'''