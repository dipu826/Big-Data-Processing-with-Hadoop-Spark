#!/usr/bin/env python3
import sys
from collections import defaultdict

# Variable to track the current taxi being processed
current_taxi = None

# Dictionary to hold trip data for each trip type ('short','medium', and 'long').
# The dictionary holds counts, max fare, min fare, and total fare.
trip_summary = defaultdict(lambda: {
    "count": 0,
    "max_fare": 0,
    "min_fare": float('inf'),
    "total_fare": 0.0
})

def output_stats(taxi_id, summary_data):
    """
    Outputs the summarized trip statistics for each trip type in a specific cab.

    Parameters:
    taxi_id (str): The ID of the taxi.
    summary_data (dict): Dictionary containing trip counts, max fare, min fare, and total fare.
    """
    for trip_type, data in summary_data.items():
        if data["count"] > 0:
            avg_fare = data["total_fare"] / data["count"]
            print(f"{taxi_id}\t{trip_type}\t{data['count']}\t{data['max_fare']}\t{data['min_fare']}\t{round(avg_fare, 2)}")

# Reads each line of input data from standard input
# Expected input format: TaxiID, TripType, Count, MaxFare, MinFare, AvgFare
for line in sys.stdin:
    taxi_id, trip_type, count, max_fare, min_fare, avg_fare = line.strip().split('\t')
    count = int(count)
    max_fare = float(max_fare)
    min_fare = float(min_fare)
    avg_fare = float(avg_fare)

    # Initializing the first taxi ID
    if current_taxi is None:
        current_taxi = taxi_id

    # Checking if the taxi ID has changed, process the current taxi's data if it has
    if taxi_id != current_taxi:
        output_stats(current_taxi, trip_summary)
        trip_summary = defaultdict(lambda: {"count": 0, "max_fare": 0, "min_fare": float('inf'), "total_fare": 0.0})
        current_taxi = taxi_id

    # Updating the summary data for the current trip type
    trip_summary[trip_type]["count"] += count
    trip_summary[trip_type]["total_fare"] += count * avg_fare
    trip_summary[trip_type]["max_fare"] = max(trip_summary[trip_type]["max_fare"], max_fare)
    trip_summary[trip_type]["min_fare"] = min(trip_summary[trip_type]["min_fare"], min_fare)

# Emiting the last taxi's data if it exists
if current_taxi is not None:
    output_stats(current_taxi, trip_summary)