import view
import add

def master():
    add.add_get() 
    while True:   
        match view.get_operation():
            case 1: add.add_get_student()
            case 2: add.add_get_predmet()
            case 3: add.add_get_mark()
            case 4: add.add_student_list()
            case 5: add.add_student_mark()
            case 6: break