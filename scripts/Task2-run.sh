#!/bin/bash

set -e

# Check if the /Output directory exists before removing it
if hdfs dfs -test -d /Output; then
    echo "Removing existing /Output directory..."
    hdfs dfs -rm -r /Output
else
    echo "/Output directory does not exist."
fi

# Run the Hadoop streaming job
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./initialization.txt \
-file ./Task2-mapper.py \
-mapper "python3 ./Task2-mapper.py" \
-file ./Task2-reducer.py \
-reducer "python3 ./Task2-reducer.py" \
-input /Input/Trips.txt \
-output /Output/Task2

# Merging the output files into a single file
hadoop fs -getmerge /Output/Task2/part* Task2_output.txt
