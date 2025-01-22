import random
import math


# Class for Waypoints
class Waypoint:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.name}: {self.latitude}° N, {self.longitude}° E"


# GPS Unit Class
class GPSUnit:
    def __init__(self):
        self.waypoints = {}
        self.current_lat = None
        self.current_long = None

    def gps_get_long_lat(self):
        """Generate random longitude and latitude values."""
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        return latitude, longitude

    def set_current_position(self):
        """Set the current position using gps_get_long_lat."""
        self.current_lat, self.current_long = self.gps_get_long_lat()

    def save_waypoint(self, name):
        """Save the current position as a waypoint with the given name."""
        if self.current_lat is None or self.current_long is None:
            print("Current position is not set.")
            return
        waypoint = Waypoint(name, self.current_lat, self.current_long)
        self.waypoints[name] = waypoint
        print(f"Waypoint '{name}' saved at {waypoint}")

    def get_waypoint(self, name):
        """Retrieve a waypoint by name."""
        if name in self.waypoints:
            return self.waypoints[name]
        else:
            print(f"Waypoint '{name}' not found.")
            return None

    def distance_to_waypoint(self, waypoint):
        """Calculate the distance between the current position and a given waypoint using the Haversine formula."""
        if self.current_lat is None or self.current_long is None:
            print("Current position is not set.")
            return

        # Haversine formula to calculate distance
        lat1 = math.radians(self.current_lat)
        lon1 = math.radians(self.current_long)
        lat2 = math.radians(waypoint.latitude)
        lon2 = math.radians(waypoint.longitude)

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Radius of Earth in kilometers (use 3956 for miles)
        radius = 6371
        distance = radius * c
        return distance

    def bearing_to_waypoint(self, waypoint):
        """Calculate the bearing between the current position and a given waypoint."""
        if self.current_lat is None or self.current_long is None:
            print("Current position is not set.")
            return

        # Convert to radians
        lat1 = math.radians(self.current_lat)
        lon1 = math.radians(self.current_long)
        lat2 = math.radians(waypoint.latitude)
        lon2 = math.radians(waypoint.longitude)

        # Calculate the bearing
        dlon = lon2 - lon1
        x = math.sin(dlon) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
        bearing = math.atan2(x, y)

        # Convert bearing from radians to degrees
        bearing = math.degrees(bearing)
        if bearing < 0:
            bearing += 360

        return bearing

    def calculate_path_length(self, path):
        """Calculate the total length of a path (a list of waypoints)."""
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += self.distance_to_waypoint(path[i + 1])
        return total_distance

    def create_new_path(self, waypoints):
        """Create a path by giving a list of waypoints."""
        path = []
        for name in waypoints:
            waypoint = self.get_waypoint(name)
            if waypoint:
                path.append(waypoint)
        return path


# Main program
def main():
    gps = GPSUnit()

    while True:
        print("\nCommands: set_position, save_waypoint, get_waypoint, distance, bearing, path_length, quit")
        command = input("Enter command: ").strip().lower()

        if command == "quit":
            print("Exiting the GPS program.")
            break
        elif command == "set_position":
            gps.set_current_position()
            print(f"Current position set: {gps.current_lat:.4f}° N, {gps.current_long:.4f}° E")
        elif command.startswith("save_waypoint"):
            _, name = command.split(maxsplit=1)
            gps.save_waypoint(name)
        elif command.startswith("get_waypoint"):
            _, name = command.split(maxsplit=1)
            waypoint = gps.get_waypoint(name)
            if waypoint:
                print(waypoint)
        elif command.startswith("distance"):
            _, name = command.split(maxsplit=1)
            waypoint = gps.get_waypoint(name)
            if waypoint:
                distance = gps.distance_to_waypoint(waypoint)
                print(f"Distance to {waypoint.name}: {distance:.2f} km")
        elif command.startswith("bearing"):
            _, name = command.split(maxsplit=1)
            waypoint = gps.get_waypoint(name)
            if waypoint:
                bearing = gps.bearing_to_waypoint(waypoint)
                print(f"Bearing to {waypoint.name}: {bearing:.2f}°")
        elif command.startswith("path_length"):
            path_names = input("Enter the waypoints in the path (separated by commas): ").split(',')
            path = gps.create_new_path(path_names)
            if path:
                length = gps.calculate_path_length(path)
                print(f"Total path length: {length:.2f} km")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
