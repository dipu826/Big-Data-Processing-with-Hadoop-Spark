#!/usr/bin/env python3
import sys

def gather_and_sort_trips():
    """
    program reads corporate trip data from standard input, keeps it in a list, sorts it by trip count in ascending order, and prints the results.
    """
    # Listing to store tuples of (company, trips) for sorting
    company_trip_data = []

    for line in sys.stdin:
        try:
            # Removing any leading or trailing whitespace from the line
            line = line.strip()

            # Spliting the line into trips and company, expecting a tab delimiter
            trips, company = line.split('\t')

            # Converting the trip count to an integer
            trips = int(trips)

            # Adding the (company, trip) tuple to the list.
            company_trip_data.append((company, trips))

        except ValueError:
            # Skipping lines that do not conform to the expected format
            continue

    # Sorting the list of tuples by trip count (second element) in ascending order.
    company_trip_data.sort(key=lambda x: x[1])

    # Print the sorted results, formatted with the company name followed by the trip count.
    for company, trips in company_trip_data:
        print(f'{company}\t{trips}')

if __name__ == "__main__":
    gather_and_sort_trips()
