def student_data(_sid, _name, _class, student_id = True, student_name = False, student_class = False):
    if student_id:
        print(_sid)
    if student_name:
        print(_name)
    if student_class:
        print(_class)

student_data(22106026, "Parth", "CSE DS")
student_data(22106026, "Parth", "CSE DS", student_name = True)
student_data(22106026, "Parth", "CSE DS", student_class = True)