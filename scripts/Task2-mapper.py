#!/usr/bin/env python3
import sys
import math

# Global variables to store medoid coordinates and the iteration count
medoids = []
iteration_count = 0

def load_medoids(file_path):
  
    global medoids, iteration_count
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # The first line contains the number of iterations
        iteration_count = int(lines[0].strip())
        # Subsequent lines contain the coordinates of the medoids
        for line in lines[1:]:
            coordinates = tuple(map(float, line.strip().split()))
            medoids.append(coordinates)

def euclidean_dist(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.

    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def mapping_trips_to_medoids():
    """
    Reading trip data from standard input and map each trip to the nearest medoid.
    """
    # Loading initial medoid data from the specified file
    load_medoids("initialization.txt")

    for line in sys.stdin:
        # Spliting the input line by commas to parse trip data
        fields = line.strip().split(',')
        if len(fields) == 8:  # Ensuring that the trip record has the correct format
            trip_id = fields[0]
            dropoff_coords = (float(fields[6]), float(fields[7]))  # Dropoff coordinates (x, y)

            # Finding the closest medoid to the dropoff point
            closest_medoid_index = -1
            smallest_distance = float('inf')
            for index, medoid_coords in enumerate(medoids):
                distance = euclidean_dist(dropoff_coords, medoid_coords)
                if distance < smallest_distance:
                    smallest_distance = distance
                    closest_medoid_index = index

            # Output format: <medoid_index> <trip_id, dropoff_x, dropoff_y, distance>
            print(f"{closest_medoid_index}\t{trip_id},{dropoff_coords[0]},{dropoff_coords[1]},{smallest_distance:.2f}")

if __name__ == "__main__":
    mapping_trips_to_medoids()
