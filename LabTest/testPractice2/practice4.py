class Person:
    """Base class for a person, contains name, age, and address."""

    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}"

    def celebrate_birthday(self):
        """Increases the person's age by 1."""
        self.age += 1


class Student(Person):
    """Class for a student, which inherits from the Person class."""

    def __init__(self, name: str, age: int, address: str, student_id: str):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.courses = []

    def add_course(self, course: str):
        """Adds a course to the student's list."""
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{course} is already added.")

    def remove_course(self, course: str):
        """Removes a course from the student's list."""
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} is not in the student's course list.")

    def __str__(self):
        courses = ", ".join(self.courses) if self.courses else "No courses"
        return super().__str__() + f"\nStudent ID: {self.student_id}\nCourses: {courses}"


class Course:
    """Class for a course, which contains students and course details."""

    def __init__(self, course_name: str, course_code: str):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []

    def add_student(self, student: Student):
        """Adds a student to the course."""
        if student not in self.students:
            self.students.append(student)
        else:
            print(f"{student.name} is already enrolled in {self.course_name}.")

    def remove_student(self, student: Student):
        """Removes a student from the course."""
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"{student.name} is not enrolled in {self.course_name}.")

    def __str__(self):
        student_names = ", ".join([student.name for student in self.students]) if self.students else "No students"
        return f"Course: {self.course_name} ({self.course_code})\nEnrolled Students: {student_names}"

    def __add__(self, other):
        """Combines two courses into one with concatenated names and codes."""
        if not isinstance(other, Course):
            raise TypeError("You can only combine two courses.")

        combined_course_name = f"{self.course_name} & {other.course_name}"
        combined_course_code = f"{self.course_code}-{other.course_code}"
        combined_course = Course(combined_course_name, combined_course_code)
        combined_course.students = self.students + other.students  # Combine the student lists
        return combined_course

    def __eq__(self, other):
        """Checks if two courses are equal by comparing names and course codes."""
        if not isinstance(other, Course):
            raise TypeError("You can only compare two courses.")
        return self.course_name == other.course_name and self.course_code == other.course_code

    def __gt__(self, other):
        """Compares the number of students between two courses."""
        if not isinstance(other, Course):
            raise TypeError("You can only compare courses.")
        return len(self.students) > len(other.students)


# Main Scope
student1 = Student(name="John Doe", age=20, address="123 Elm Street", student_id="S12345")
student2 = Student(name="Jane Smith", age=22, address="456 Oak Avenue", student_id="S67890")

# Create courses
course1 = Course(course_name="Math 101", course_code="M101")
course2 = Course(course_name="Physics 101", course_code="P101")

# Add students to courses
course1.add_student(student1)
course2.add_student(student1)
course2.add_student(student2)

# Add courses to student
student1.add_course("Math 101")
student1.add_course("Physics 101")

# Print student and course details
print(student1)
print(course1)
print(course2)

# Create a combined course by using the + operator
combined_course = course1 + course2
print(combined_course)

# Check equality of two courses
print(course1 == course2)

# Compare courses by number of students
print(course1 > course2)

# Simulate a birthday
student1.celebrate_birthday()
print(student1)
