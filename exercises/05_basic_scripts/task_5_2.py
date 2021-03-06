# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
template_network = "{0:<10}{1:<10}{2:<10}{3:<10}\n{0:08b}  {1:08b}  {2:08b}  {3:08b}"
template_mask = "{0:<10}{1:<10}{2:<10}{3:<10}\n{0:08b}  {1:08b}  {2:08b}  {3:08b}"

ip_network = input("Введите IP-сеть в формате: 10.1.1.0/24: ")
ip_network = ip_network.split('/')
network = ip_network[0].split('.')

mask = "1" * int(ip_network[1]) + "0" * (32 - (int(ip_network[1])))
list_mask = list()
list_mask.append(int(mask[:8], 2))
list_mask.append(int(mask[8:16], 2))
list_mask.append(int(mask[16:24], 2))
list_mask.append(int(mask[24:], 2))

print("\nNetwork: \n" + template_network.format(
    int(network[0]), int(network[1]), int(network[2]), int(network[3])
))

print("\nMask: \n/" + ip_network[1] + "\n" + template_mask.format(
    int(list_mask[0]), int(list_mask[1]), int(list_mask[2]), int(list_mask[3])
))