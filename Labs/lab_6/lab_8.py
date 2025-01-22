
def get_tuple(movie_string):
    """Convert a movie string to a tuple (movie_name, year)."""
    # Split the string to get the movie name and year
    parts = movie_string.split(" (")
    movie = parts[0].strip()
    year = int(parts[1].split(")")[0])

    return (movie, year)



def create_dictionary(user_file):
    """Create a dictionary from the input file."""
    movie_dict = {} # Initialize an empty dictionary

    try:
        # Open the file to read
        file = open(user_file, "r")

        for line in file:

            parts = line.strip().split(", ") # Split line by commas
            actor = parts[0] # First part is the actor's name
            movies = parts[1:] # Remaining parts are the movies

            for movie in movies:
                movie_name, year = get_tuple(movie) # Get movie tuple
                if(movie_name, year) not in movie_dict:
                    movie_dict[(movie_name, year)] = set() # Create a new set if doesn't exist

                movie_dict[(movie_name, year)].add(actor) # Add actor to the set
        
        file.close() # Close the file after reading

    except FileNotFoundError:
        print(f"Error: The file '{user_file}' was not found.")

    return movie_dict # Return the filled dictionary


def perform_operation(movie_dict, movie1, movie2, operator):
    """Perform set operations based on user input."""
    actors1 = movie_dict.get(movie1, set()) # Get actors for movie1
    actors2 = movie_dict.get(movie2, set()) # Get actors for movie2
    
    if operator == "&": # Intersection
        return actors1 & actors2
    
    elif operator == "|": # Union
        return actors1 | actors2
    
    elif operator == "-": # Symmetric difference
        return actors1 ^ actors2


def menu(movie_dict):
    """Display a menu for user input and perform operations."""
    while True:
        user_input = input("Please enter two movies as 'name(year)' separated by the appropriate operator (&, |, -), or enter \".\" to quit: ")

        if user_input == ".":
             break # Exit the loop if the user inputs '.'
        
        # Manually search for the operator and split the string
        operator = None
        for op in ["&", "|", "-"]:
            if op in user_input:
                operator = op
                # Split the input into parts based on the operator
                parts = user_input.split(op)
                break

        if operator and len(parts) == 2:
            movie1_str = parts[0].strip()  # First movie
            movie2_str = parts[1].strip()  # Second movie

        try:
            movie1 = get_tuple(movie1_str)  # Get tuple for movie1
            movie2 = get_tuple(movie2_str)  # Get tuple for movie2

            # Perform the operation and display the result
            result = perform_operation(movie_dict, movie1, movie2, operator)
            print(f"The set of actors for this operation is:\n{result}")
        except ValueError:
            print("Invalid input format. Please try again") # Handle incorrect input



# Main Scope
user_file = input("Enter a file to open: ") # Prompt user for file name
movie_dict = create_dictionary(user_file) # Create dictionary from file
menu(movie_dict) # Display menu and perform operations
