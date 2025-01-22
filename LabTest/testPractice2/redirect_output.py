import sys

class RedirectOutput:
    def __init__(self, filename: str):
        # Open the file in write mode (or append mode if needed)
        self.filename = filename
        self.original_stdout = sys.stdout  # Save the original stdout
        self.file = open(filename, 'w')  # Open the file for writing

    def write(self, message: str):
        # Display message before writing to the file (direct to stdout)
        self.file.write(message)
        self.file.flush()  # Ensure that data is written to the file immediately

    def flush(self):
        # Flush method to ensure output is written immediately
        self.file.flush()

    def close(self):
        # Display message after writing to the file (direct to stdout)

        self.file.close()  # Close the file

    def __enter__(self):
        # Enter the context manager, redirecting the output
        sys.stdout = self
        sys.__stdout__.write("Redirecting output to file...\n")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore the original stdout and close the file when exiting the context
        sys.stdout = self.original_stdout
        self.close()
        sys.__stdout__.write("Finished writing to the file.\n")

# Example usage
with RedirectOutput("output.txt") as redirect:
    print("This will be written to the file.")
    print("All output from print statements will be redirected to the file.")


