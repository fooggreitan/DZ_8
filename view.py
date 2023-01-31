def get_operation():
    type = int(input(
        "\n1 - запись ученика\n2 - предмет\n3 - оценка\n4 - показ списка учеников\n5- показ листа оценок конкретного ученика\n6 - выход\n"
    ))
    return type
def get_predmet():
    name = input('Введите предмет: ')
    return name
def get_name():
    getclass = input('Введите имя и фамилию ученика: ')
    return getclass
def get_mark():
    mark = input(('Введите оценку по предмету: '))
    return mark