
class SemTranscript(object):
    def __init__(self, name: str, courses: list, grades: list):
        self.name = name
        self.courses = courses
        self.grades = grades
        self.avg_grade = self.calculate_average()

    def calculate_average(self):
        """ Calculate the average grade for the semester. """
        if len(self.grades) == 0:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def __add__(self, other):
        """ Overloaded addition operator to combine two semester transcripts. """
        if not isinstance(other, SemTranscript):
            raise TypeError("Can only add another SemTranscript object")

        # Combine courses and grades from both semesters
        combined_courses = self.courses + other.courses
        combined_grades = self.grades + other.grades

        # Create and return a new SemTranscript for the combined semester data
        return SemTranscript(self.name, combined_courses, combined_grades)

    def __str__(self):
        """ Return the string representation of the semester transcript. """
        courses_str = ""
        for course, grade in zip(self.courses, self.grades):
            courses_str += f"{course}: {grade}\n"

        return (f"Student: {self.name}\n"
                f"Courses: {courses_str}"
                f"Average Grade: {self.avg_grade:.2f}\n")

    def __repr__(self):
        """ Return the formal string representation for debugging purposes. """
        return f"SemTranscript('{self.name}', {self.courses}, {self.grades})"


# Main Scope
# First semester data
student1_sem1 = SemTranscript("John Doe", ["Math", "Physics", "Chemistry"], [85, 90, 88])

# Second semester data
student1_sem2 = SemTranscript("John Doe", ["Biology", "Computer Science", "English"], [92, 89, 84])

# Print individual semester transcripts
print(student1_sem1)
print(student1_sem2)

# Combine two semesters and calculate the new average grade for the year
combined_transcript = student1_sem1 + student1_sem2
print("\nCombined Transcript for the Year:")
print(combined_transcript)
