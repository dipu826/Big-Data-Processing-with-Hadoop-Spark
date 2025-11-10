#!/usr/bin/env python3
import sys
import math

def calc_best_medoid(cluster_points):

    best_medoid = None
    lowest_total_distance = float('inf')

    # Iterating over each point in the cluster to evaluate as potential medoid
    for _, x1, y1, _ in cluster_points:
        # Calculatinfd the sum of distances from this point to all other points in the cluster
        total_distance = sum(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) for _, x2, y2, _ in cluster_points)
        # Updating the best medoid if a new lower total distance is found
        if total_distance < lowest_total_distance:
            lowest_total_distance = total_distance
            best_medoid = (x1, y1)
    
    return best_medoid

def reducing_clusters():
    """
    Processing input data to find and print the optimal medoid for each cluster.
    """
    current_cluster_index = None
    cluster_points = []

    # Reading each line of input
    for line in sys.stdin:
        # Spliting input line into medoid index and associated values
        medoid_index, values = line.strip().split('\t')
        trip_id, x, y, distance = values.split(',')
        x, y = float(x), float(y)  # Distance is no longer used

        # Checking if processing a new cluster
        if current_cluster_index is None:
            current_cluster_index = medoid_index

        # If the medoid index changes, process and reset the current cluster.
        if medoid_index != current_cluster_index:
            # Finding and printing the best medoid for the current cluster
            best_medoid = calc_best_medoid(cluster_points)
            print(f"{best_medoid[0]:.6f}\t{best_medoid[1]:.6f}")
            current_cluster_index = medoid_index
            cluster_points = []

        # Appending the current point to the cluster
        cluster_points.append((trip_id, x, y, distance))

    # Processing the last cluster after the loop
    if cluster_points:
        best_medoid = calc_best_medoid(cluster_points)
        print(f"{best_medoid[0]:.6f}\t{best_medoid[1]:.6f}")

if __name__ == "__main__":
    reducing_clusters()
