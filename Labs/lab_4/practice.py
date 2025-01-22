# add before line_count_int = 1
while True:
    find_line_str = input("Which line (integer): ")
    try:
        find_line_int = int(find_line_str)  # Try converting to int
        break  # Exit the loop when valid integer is entered
    except ValueError:
        print(f"'{find_line_str}' is not a valid integer. Please enter a valid line number.")


