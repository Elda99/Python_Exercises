class Person(object):
    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        self.get_fullname()
        print(self.full_name)
    def get_fullname(self):
            self.full_name = self.first_name + " " + self.last_name


class Student(Person):
    def __init__(self, first_name, last_name,status):
        Person.__init__(self,first_name, last_name)
        self.status = status
    def disp_status(self):
        print(self.full_name,self.status)

a = Student ('Elda','Koci','-st')
a.display()
a.disp_status()
