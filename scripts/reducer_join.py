#!/usr/bin/env python3
import sys

def operation_taxi_data():
    """
    Lines are processed from standard input to provide company-specific trip numbers.
    Each line corresponds to either a taxi record with a firm name or a trip record with a trip count.
    Returns the total number of trips per company.

    """
    current_taxi_id = None
    current_company = None
    trip_count = 0

    for line in sys.stdin:
        try:
            # Removing any leading or trailing whitespace from the line
            line = line.strip()

            # Splitting the line into taxi ID, record type (taxi or trip), and value
            taxi_id, record_type, value = line.split('\t')

            # Checking if we have moved to a new taxi ID
            if taxi_id != current_taxi_id:
                # Output the aggregated result for the previous taxi ID
                if current_taxi_id is not None:
                    if current_company is not None:
                        print(f'{current_company}\t{trip_count}')
                    else:
                        sys.stderr.write(f"Company missing for taxi_id: {current_taxi_id}\n")

                # Reseting variables for the new taxi ID
                current_taxi_id = taxi_id
                current_company = None
                trip_count = 0

            # Processing the record based on its type
            if record_type == 'taxi':
                # Setting the current company name for the taxi ID
                current_company = value
            elif record_type == 'trip':
                # Increment the trip count for the taxi ID
                trip_count += int(value)
            else:
                # Log an error if an unexpected record type is encountered
                sys.stderr.write(f"Unexpected record type: {record_type}\n")

        except ValueError as ve:
            # Handling and log ValueErrors, which can occur if the data format is incorrect
            sys.stderr.write(f"ValueError processing line: {line} | Error: {str(ve)}\n")
        except Exception as ex:
            # Log any other unexpected errors that may occur
            sys.stderr.write(f"Unexpected error processing line: {line} | Error: {str(ex)}\n")

    # Output the total trip count for the last taxi ID processed
    if current_company:
        print(f'{current_company}\t{trip_count}')

if __name__ == "__main__":
    operation_taxi_data()
