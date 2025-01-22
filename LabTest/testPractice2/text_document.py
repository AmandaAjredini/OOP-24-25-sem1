import os

class TextDocument(object):
    def __init__(self, filename: str):

        if not os.path.isfile(filename):
            raise FileNotFoundError(f"File '{filename}' does not exist.")

        self.filename = filename

    def __add__(self, other):
        if not isinstance(other, TextDocument):
            raise TypeError("Can only concatenate with another file.")

        with open(self.filename, 'r') as file1, open(other.filename, 'r') as file2:
            new_content = file1.read() + "\n" + file2.read()

        new_file_path = "concatenated.txt"
        with open(new_file_path, 'w') as new_file:
            new_file.write(new_content)

        return TextDocument(new_file_path)

    def __gt__(self, other):
        if not isinstance(other, TextDocument):
            raise TypeError("Can only compare with another file.")

        with open(self.filename, 'r') as file1, open(other.filename, 'r') as file2:
            length1 = len(file1.read().split())
            length2 = len(file2.read().split())

        return length1 > length2

    def __mul__(self, other):
        if not isinstance(other, int) or other <= 0:
            raise ValueError("Multiplier must be a positive integer")

        with open(self.filename, 'r') as file:
            content = file.read()

        with open(self.filename, 'w') as file:
            file.write(content * other)

        return self

    def __str__(self):
        return f"File with name: {self.filename}"



# Main Scope
while True:
    print("\n--- TextDocument Operations Menu ---")
    print("1. Concatenate two files")
    print("2. Compare two files")
    print("3. Multiply file content by an integer")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            file1 = input("Enter the path of the first file: ").strip()
            file2 = input("Enter the path of the second file: ").strip()
            doc1 = TextDocument(file1)
            doc2 = TextDocument(file2)
            result_doc = doc1 + doc2
            print(f"Files concatenated successfully into: {result_doc.filename}")

        except Exception as e:
            print(f"Error: {e}")

    elif choice == "2":
        try:
            file1 = input("Enter the path of the first file: ").strip()
            file2 = input("Enter the path of the second file: ").strip()
            doc1 = TextDocument(file1)
            doc2 = TextDocument(file2)
            result = doc1 > doc2

            if result:
                print(f"First file is greater that the second file.")
            else:
                print(f"First file is not greater than the second file")

        except Exception as e:
            print(f"Error: {e}")

    elif choice == "3":
        try:
            file = input("Enter the path of the file: ").strip()
            multiplier = int(input("Enter the integer multiplier: ").strip())
            doc = TextDocument(file)
            doc * multiplier
            print(f"File content multiplied successfully. Check the file: {file}")

        except Exception as e:
            print(f"Error: {e}")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")