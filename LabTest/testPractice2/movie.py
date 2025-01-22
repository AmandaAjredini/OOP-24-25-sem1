
class Movie(object):
    def __init__(self, director: str = '', actors: str = '', support_cast: str = '', producer: str = '', budget: float = 0.0, revenue: float = 0.0):
        self.director = director
        self.actors = actors
        self.support_cast = support_cast
        self.producer = producer
        self.budget = budget
        self.revenue = revenue

    def __eq__(self, other):
        if not isinstance(other, Movie):
            raise TypeError("Can only compare between Movie types")

        if self.revenue == other.revenue:
            return True
        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, Movie):
            raise TypeError("Can only compare between Movie types")

        if self.revenue > other.revenue:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Movie):
            raise TypeError("Can only compare between Movie types")

        if self.revenue < other.revenue:
            return True
        else:
            return False

    def __str__(self):
        return (f"Movie:\n"
                f"Director: {self.director}\n"
                f"Lead Actors: {self.actors}\n"
                f"Supporting Cast: {self.support_cast}\n"
                f"Production House: {self.producer}\n"
                f"Production Budget: {self.budget}\n"
                f"Revenue Earned: {self.revenue}")


# Main Scope
movie1 = Movie("Christopher Nolan",
               "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
               "Michael Caine, Topher Grace, Ellen Burstyn",
               "Emma Thomas",
               165_000_000.0,
               677_000_000.0)

movie2 = Movie("Steven Spielberg",
               "Tom Hanks, Matt Damon, Edward Burns",
               "Tom Sizemore, Barry Pepper, Giovanni Ribisi",
               "Steven Spielberg",
               140_000_000.0,
               482_000_000.0)

print(movie1 == movie2)