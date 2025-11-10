#!/usr/bin/env python3
import sys

def operation_input():
    """
    Reads lines from standard input, expecting a company and the number of trips, separated by a tab character. 
    It rearranges the order and prints the trip count first, followed by the firm name.


    """
    for line in sys.stdin:
        try:
            # Removing any leading or trailing whitespace
            line = line.strip()

            # Splitting the line into company and trips based on tab delimiter
            company, trips = line.split('\t')

            # Output the trips count first, followed by the company name
            print(f'{trips}\t{company}')

        except ValueError:
            # Skip lines that do not correspond to the intended format, such as missing fields.

            continue

if __name__ == "__main__":
    operation_input()
