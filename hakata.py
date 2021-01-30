n = int(input("Введите четырехзначное число: " ))
a = n // 1000
b =  (n // 100)%10
c = (n//10)%10
d = n%10
v = [a,b,c,d]

c = list(reversed(sorted(v)))
if v == c:
  print("да, число по убыванию")
else:
  print("нет, не по убыванию")