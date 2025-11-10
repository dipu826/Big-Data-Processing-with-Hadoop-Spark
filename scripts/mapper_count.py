#!/usr/bin/env python3
import sys

def operation_input():
    """
    We process each line from the standard input, assuring a proper cab ID and trip count. 
    If the results are valid, print them in a proper way; otherwise, log errors.

    """
    for line in sys.stdin:
        try:
            # Striping the whitespace and spliting the line into taxi ID and trips
            line = line.strip()
            taxi_id, trips = line.split('\t')
            
            # Checking if taxi_id is not empty and trip is a digit.
            if taxi_id and trips.isdigit():
                # Printing the formatted output with taxi ID and trip count
                print(f'{taxi_id}\t{trips}')
        except ValueError as ve:
            # Log specific ValueError with line content for debugging
            sys.stderr.write(f"ValueError processing line: {line} | Error: {str(ve)}\n")
        except Exception as ex:
            # Log any unexpected errors that may occur during processing
            sys.stderr.write(f"Unexpected error processing line: {line} | Error: {str(ex)}\n")

if __name__ == "__main__":
    operation_input()
