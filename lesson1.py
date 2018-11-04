print("Задача 1")

a = "разработка"
print(a)
print(type(a))

b = "сокет"
print(b)
print(type(b))

c = "декоратор"
print(c)
print(type(c))


a = "\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0"
print(a)
print(type(a))

b = "\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82"
print(b)
print(type(b))

c = "\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80"
print(c)
print(type(c))



print("\nЗадача 2")

a = b"class"
print(a)
print(type(a))

b = b"function"
print(b)
print(type(b))

c = b"method"
print(c)
print(type(c))



print("\nЗадача 3")

print("Строки 'класс' и 'функция' нельзя записать в байтовом формате, потому-что байты могут содержать только символы ASCII.")
print(b"attribute")
print(type(b"attribute"))
print(b"type")
print(type(b"type"))



print("\nЗадача 4")

a = "разработка"
a = a.encode('utf-8')
print(a)
a = a.decode('utf-8')
print(a)

b = "администрирование"
b = b.encode('utf-8')
print(b)
b = b.decode('utf-8')
print(b)

c = "protocol"
c = c.encode('utf-8')
print(c)
c = c.decode('utf-8')
print(c)

d = "standard"
d = d.encode('utf-8')
print(d)
d = d.decode('utf-8')
print(d)




print("\nЗадача 5")

import subprocess
args = ['ping', 'youtube.com']
proc = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in proc.stdout:
    print(line)
    print(line.decode('cp866'))

args = ['ping', 'yandex.ru']
proc = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in proc.stdout:
    print(line)
    print(line.decode('cp866'))




print("\nЗадача 6")

import locale

print(locale.getpreferredencoding())

with open('test_file.txt', 'w') as f:
    f.write("сетевое программирование\nсокет\nдекоратор")
    
with open('test_file.txt', 'r', encoding='utf') as f:
    print(f.readlines())


