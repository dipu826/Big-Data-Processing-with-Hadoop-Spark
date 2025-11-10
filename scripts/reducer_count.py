#!/usr/bin/env python3
import sys

def operation_trip_counts():
    """
    Processes trip data from standard input and totals the number of trips for each cab ID.
    After processing all input data, the cab ID and total number of trips are output.
    """
    current_taxi_id = None
    total_trips = 0

    for line in sys.stdin:
        try:
            # Removing any leading or trailing whitespace from the line
            line = line.strip()

            # Splitting the line into taxi ID and trip count, separated by a tab
            taxi_id, trips = line.split('\t')

            # Converting trip count to an integer
            trips = int(trips)
            
            # If the current taxi ID changes, print the aggregated trip count of the previous taxi ID.
            if taxi_id != current_taxi_id:
                if current_taxi_id is not None:
                    print(f'{current_taxi_id}\t{total_trips}')
                
                # Updating the current taxi ID and reset trip count
                current_taxi_id = taxi_id
                total_trips = 0
            
            # Accumulating the trip count for the current taxi ID
            total_trips += trips
        
        except ValueError as ve:
            # Handle and log ValueError for lines that cannot be processed due to format errors.
            sys.stderr.write(f"ValueError processing line: {line} | Error: {str(ve)}\n")
        except Exception as ex:
            # Handling and log unexpected exceptions that may occur
            sys.stderr.write(f"Unexpected error processing line: {line} | Error: {str(ex)}\n")

    # Output the total trips for the last taxi ID after the loop completes
    if current_taxi_id is not None:
        print(f'{current_taxi_id}\t{total_trips}')

if __name__ == "__main__":
    operation_trip_counts()
