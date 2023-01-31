import view

predmet = {
    "Петров Компотов" : {
        "Математика": [4,4,3,3,4],
        "Информатика": [3,3,3,4,'Н'],
        "Русский": [4,5,'Н',4,5],
        "География": ['Н',5,3,4,5]
    },
    "Валентина Усова": {
        "Математика": [3,2,1,5,2],
        "Информатика": [5,5,5,5,5],
        "Русский": [5,5,5,5,5],
        "География": [5,5,5,5,5]
    },  
    "Лиза Вагурина":{
        "Математика": [3,2,1,5,2],
        "Информатика": [3,3,3,5,2],
        "Русский": [3,2,1,5,2],
        "География": [3,3,3,3,2]
    }
}

def add_get():
    return print(predmet)

def add_get_predmet():
    for i, j in predmet.items():
        j[view.get_predmet()] = []

def add_get_student():
    predmet[view.get_name()] = {}

def add_get_mark():
    predmet[view.get_name()][view.get_predmet()].append(int(view.get_mark()))

def add_student_list():
    return print(predmet.keys())

def add_student_mark():
    return print(predmet.get(view.get_name()))