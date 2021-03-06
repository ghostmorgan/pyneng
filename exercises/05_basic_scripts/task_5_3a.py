# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]





#Ввод информации от пользователя
mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")

#словарь для выбора какой шаблон использовать и какой задавать вопрос
templates = {"access": {"access": access_template, "question": "Введите номер VLAN: "}, "trunk": {"trunk": trunk_template, "question": "Введите разрешенные VLANы: "}}

#Ввод информации от пользователя
vlans = input(templates[mode]['question'])

#форматирование шаблона в зависимости от того что ввел пользователь
res_temp = "\n".join(templates[mode][mode]).format(vlans)

#шаблон вывода итогового результата на экран
print_template = f"""
interface {interface}
{res_temp}
"""

print(print_template)