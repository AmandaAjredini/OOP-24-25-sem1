
class Module(object):
    def __init__(self, name: str, time: str, year: str, location: str, lecturer: str):
        self.name = name
        self.time = time
        self.year = year
        self.location = location
        self.lecturer = lecturer
        self.assignments = {}

    def add_assignment(self, assignment_name, deadline, marks):
        """Adds a new assignment with the given name, deadline, and marks percentage."""
        if assignment_name in self.assignments:
            print(f"Assignment '{assignment_name}' already exists. Use update_assignment to modify it.")
        else:
            self.assignments[assignment_name] = (deadline, marks)
            print(f"Assignment '{assignment_name}' added successfully.")

    def update_assignment(self, assignment_name, deadline=None, marks=None):
        """Updates an existing assignment's deadline and/or marks."""
        if assignment_name not in self.assignments:
            print(f"Assignment '{assignment_name}' does not exist. Please add it first.")
        else:
            current_deadline, current_marks = self.assignments[assignment_name]

            # If 'deadline' is provided (not None), update 'new_deadline' with it. Otherwise, keep the current deadline.
            if deadline is not None:
                new_deadline = deadline
            else:
                new_deadline = current_deadline

            # If 'marks' is provided (not None), update 'new_marks' with it. Otherwise, keep the current marks.
            if marks is not None:
                new_marks = marks
            else:
                new_marks = current_marks

            self.assignments[assignment_name] = (new_deadline, new_marks)
            print(f"Assignment '{assignment_name}' updated successfully.")

    def __str__(self):
        assignments_list = []

        for name, (deadline, marks) in self.assignments.items():
            assignment_str = f"Assignment Name: {name}\n"
            assignment_str += f"Deadline: {deadline}\n"
            assignment_str += f"Marks: {marks}%\n"

            assignments_list.append(assignment_str)
        assignments_str = "\n".join(assignments_list)


        return (f"Module:\n"
                f"Name: {self.name}\n"
                f"Time: {self.time}\n"
                f"Year: {self.year}\n"
                f"Location: {self.location}\n"
                f"Lecturer: {self.lecturer}\n"
                f"Assignments: \n{assignments_str if assignments_str else 'No Assignments yet.'}")

class Student(object):
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.modules = {} # Dictionary to store the modules the student is taking

    def add_module(self, module):
        """Adds a module to the student's list of modules."""
        if module.name in self.modules:
            print(f"Module '{module.name}' already added.")
        else:
            self.modules[module.name] = module
            print(f"Module '{module.name}' added to {self.name}'s semester.")

    def remove_module(self, module_name):
        """Removes a module from the student's list of modules."""
        if module_name in self.modules:
            del self.modules[module_name]
            print(f"Module '{module_name}' removed from {self.name}'s semester.")
        else:
            print(f"Module '{module_name}' not found.")

    def __str__(self):
        modules_str = "\n".join([str(module) for module in self.modules.values()])

        return (f"Student\n"
                f"Name: {self.name}\n"
                f"Student ID: {self.student_id}\n"
                f"Modules: \n{modules_str if modules_str else 'No modules registered yet'}")


# Main Scope
module1 = Module("OOP", "Monday, 9:00am", "24/25", "LG021", "Lucas Rizzo")
#print(module1)
module2 = Module("Maths", "Thursday, 14:00pm", "24/25", "LG020", "Blathnaid Sheridan")
#print(module1)

module1.add_assignment("Lab Test 1", "02/11/24", 10)
module1.add_assignment("Lab Test 2", "03/12/24", 15)

module2.add_assignment("Lab Test 1", "22/10/24", 15)
module2.add_assignment("Lab Test 2", "27/11/24", 15)
#print(module1)
#print(module2)

student1 = Student("Amanda Ajredini", "C23388586")
student1.add_module(module1)
student1.add_module(module2)

#print(student1)

module1.update_assignment("Lab Test 1", marks=22)

#print(student1)

student1.remove_module("OOP")
print(student1)



