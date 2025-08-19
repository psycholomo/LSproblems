class LaunchSchool:
    def __init__(self, name="Launch School"):
        self.name = name

        self.staff = []
    
    def add_staff(self, staff_member):
        self.staff.append(staff_member)
    
    def add_ta(self, ta):
        self.tas.append(ta)
    
    def get_all_people(self):
        return self.students + self.staff + self.tas

    def work(self):

        for obj in self.staff:
            if isinstance(obj, TA):
                obj.help_student
            elif isinstance(obj, Staff):
                obj.get_responsibilities                                          
                                                                                       
class TA():
    
    def help_student(self, student):
        self.students_helped.append(student)
    
class Staff():

    def get_responsibilities(self):
        return self.responsibilities.copy()

                                            