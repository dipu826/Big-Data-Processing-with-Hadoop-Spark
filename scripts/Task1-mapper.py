#!/usr/bin/env python3
import sys
from collections import defaultdict

# Create a dictionary to keep trip data organized by trip type for each cab.
# The keys will be cab IDs, while the values will be dictionaries including 
# trip types ('short','medium', 'long') and fares.

trip_data = defaultdict(lambda: {"short": [], "medium": [], "long": []})

def categorize_trip(distance):
    if distance >= 200:
        return "long"
    elif distance >= 100:
        return "medium"
    else:
        return "short"

def result_trip_stats():
    """
    Print statistics for each trip type (short, medium, and long) for each cab,
    including total trips, maximum and minimum fare, and average fare.

    """
    for taxi_id, trips in trip_data.items():
        for trip_type, fares in trips.items():
            if fares:
                total_trips = len(fares)
                max_fare = max(fares)
                min_fare = min(fares)
                avg_fare = sum(fares) / total_trips
                print(f"{taxi_id}\t{trip_type}\t{total_trips}\t{max_fare}\t{min_fare}\t{avg_fare}")

# Processing each line of input from standard input
# The assumed input format is TripID, TaxiID, Fare, Distance, Pickup_X, Pickup_Y, Dropoff_X, Dropoff_Y.
for line in sys.stdin:
    data = line.strip().split(',')
    taxi_id = data[1] 
    fare = float(data[2])  
    distance = float(data[3])  

    # Classifying the trip and add the fare to the corresponding category
    trip_category = categorize_trip(distance)
    trip_data[taxi_id][trip_category].append(fare)

# Output the computed statistics for all taxis
result_trip_stats()