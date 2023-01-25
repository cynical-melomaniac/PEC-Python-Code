def student_list(_sid, _name, _class, student_id = False, student_name = False, student_class = False):
    if student_id:
        print(_sid)
    if student_name:
        print(_name)
    if student_class:
        print(_class)

student_list(22106026, "Parth", "CSE DS", student_id = True)
student_list(22106026, "Parth", "CSE DS", student_name = True)
student_list(22106026, "Parth", "CSE DS", student_class = True)