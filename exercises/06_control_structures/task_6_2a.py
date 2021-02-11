# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input("Введите ip-адрес в формате 10.0.1.1: ")

unassigned = '0.0.0.0'
local_broadcast = '255.255.255.255'

octets = ip.split('.')

last_octets = [item for item in octets if item.isdigit()]

first_octet = ip.split('.')[0]

for octet in octets:
   if octet.isdigit() == False:
      print('Неправильный IP-адрес')
   elif int(octet) < 0 or int(octet) > 255:
      print('Неправильный IP-адрес')
   elif ip.count('.') != 3 or len(last_octets) != 4:
      print('Неправильный IP-адрес')
   else:
      if ip == unassigned:
         print('unassigned')
      elif ip == local_broadcast:
         print('local broadcast')
      elif 1<= int(first_octet) <= 224:
         print('unicast')
      elif 224 <= int(first_octet) <= 240:
         print('multicast')
      else:
         print('unused')
   break