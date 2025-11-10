#!/usr/bin/env python3
import sys

def operation_input():
    """
    Process lines from standard input to see if they belong in the Taxis or Trips datasets.
    It produces structured output based on the detected data type, ready for further processing or joining.

    """
    for line in sys.stdin:
        try:
            # Removing any leading or trailing whitespace
            line = line.strip()

            # Skipping the header line if present
            if line.startswith("Taxi#"):
                continue

            # Spliting the line into fields
            fields = line.split(',')

            # Checking if the line matches the Taxis dataset (4 fields expected)
            if len(fields) == 4:
                taxi_id, company, model, year = fields
                # Output the taxi_id with a tag which indicates that it's from the Taxis dataset and include the company
                print(f'{taxi_id}\ttaxi\t{company}')
            
            # Checking that the line matches the Trips dataset (8 fields anticipated)
            elif len(fields) == 8:
                trip_id, taxi_id, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y = fields
                # Output the taxi_id with a tag indicating it comes from the Trips collection, then count the trip.
                print(f'{taxi_id}\ttrip\t1')
            
            # Handling unexpected formats by reporting the number of fields
            else:
                sys.stderr.write(f"Unexpected number of fields: {len(fields)} in line: {line}\n")
        
        except Exception as e:
            # Log any errors encountered during processing
            sys.stderr.write(f"Error processing line: {line} | Error: {str(e)}\n")

if __name__ == "__main__":
    operation_input()
