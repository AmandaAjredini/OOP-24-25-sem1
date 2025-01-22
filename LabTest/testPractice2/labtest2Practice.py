# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# 11-12-2020

class Document(object):
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name):
        #name mangling done to make variables private
        self.__characters = []
        self.__cursor = 0
        self.__filename = file_name

    @property #getter for characters
    def characters_prop(self):
        return self.__characters

    @characters_prop.setter #setter for characters
    def characters_prop(self, value):
        self.__characters = value

    @property #getter for cursor
    def cursor_prop(self):
        return self.__cursor

    @cursor_prop.setter # setter for cursor
    def cursor_prop(self, value):
        self.__cursor = value

    @property
    def filename_prop(self): #getter for filename
        return self.__filename

    @filename_prop.setter #setter for filename
    def filename_prop(self, value):
        self.__filename = value

    def insert(self, character: str):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        if not isinstance(character, str) or len(character) != 1:
            raise ValueError("Only single characters can be inserted!")
        
        self.__characters.insert(self.__cursor, character)
        self.__cursor += 1

    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """
        if self.__cursor >= len(self.__characters):
            raise IndexError("Cursor is out of bounds! Nothing to delete.")
        del self.__characters[self.__cursor]

    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.__filename, 'w') as f:
            f.write(''.join(self.__characters))

        print(f"Your file {self.__filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps: int):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        if steps <= 0:
            raise ValueError("Steps must be positive!")
        new_position = self.__cursor + steps

        if new_position > len(self.__characters):
            raise ValueError("Cursor cannot move beyond the end of the document!")
        self.__cursor = new_position


    def backward(self, steps: int):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """
        if steps <= 0:
            raise ValueError("Steps must be positive!")
        new_position = self.__cursor - steps

        if new_position < 0:
            raise ValueError("Cursor cannot move before the beginning of the document!")
        self.__cursor = new_position

    def __str__(self):
        return ''.join(self.__characters)



# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake news'

for letter in characters:
    doc.insert(letter)

doc.backward(4)
doc.delete()
doc.insert('b')
doc.save()
print(doc)