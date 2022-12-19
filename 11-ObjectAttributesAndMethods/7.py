# class definition
class Student():
    
    # class variables
    universitet = "UEK Kraków"
    id=100000
    def __init__(self, name, surname, field_of_study):
        self.name = name
        self.surname= surname
        self.id=Student.id
        self.field_of_study = field_of_study
        Student.id+=1
    
    def __str__(self):
        return f"{self.name} {self.surname} ({self.id}) {self.field_of_study} {Student.universitet}"

# program
student1 = Student("Anna","Maj","Applied Informatics")
print(student1)
student1 = Student("Anna","Maj","Applied Informatics")
print(student1)
student1 = Student("Anna","Maj","Applied Informatics")
print(student1)





