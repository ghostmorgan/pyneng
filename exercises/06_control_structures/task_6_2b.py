# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите ip-адрес в формате 10.0.1.1: ")

unassigned = '0.0.0.0'
local_broadcast = '255.255.255.255'


while True:
    octets = ip.split('.')
    correct_ip = len(octets) == 4

    if len(octets) != 4:
        correct_ip = False
    else:
       for octet in octets:
           if not (octet.isdigit() and int(octet) in range(256)):
               correct_ip = False
               break

    if not correct_ip:
        print("Неправильный IP-адрес")
        ip = input("Введите ip-адрес в формате 10.0.1.1: ")
        continue
    else:
        octet_num = [int(i) for i in octets]

        if ip == unassigned:
            print('unassigned')
        elif ip == local_broadcast:
            print('local broadcast')
        elif octet_num[0] in range(1, 224):
            print('unicast')
        elif octet_num[0] in range(224, 240):
            print('multicast')
        else:
            print('unused')
    break