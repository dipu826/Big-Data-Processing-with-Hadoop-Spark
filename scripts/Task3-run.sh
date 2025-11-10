#!/bin/bash

set -e

# Define file paths for intermediate and final outputs
JOIN_OUTPUT_MERGED="./join_output_merged.txt"
COUNT_OUTPUT_MERGED="./count_output_merged.txt"
FINAL_OUTPUT="./final_output.txt"
SORTED_OUTPUT="./Task3_output.txt"

# Step 1: Joining Taxis and Trips datasets
echo "Starting join operation..."
hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapreduce.job.reduces=3 \
    -input /Input/Taxis.txt \
    -input /Input/Trips.txt \
    -output /Output/Task3/join_output \
    -mapper mapper_join.py \
    -reducer reducer_join.py \
    -file mapper_join.py \
    -file reducer_join.py

# Merging the join output on the master node
echo "Merging join output..."
hdfs dfs -getmerge /Output/Task3/join_output/ $JOIN_OUTPUT_MERGED

# Step 2: Prepare the count input by sending the merged join output back to HDFS.
echo "Preparing HDFS for count input..."
hdfs dfs -rm -r -f /Output/Task3/count_input || true
hdfs dfs -mkdir -p /Output/Task3/count_input
hdfs dfs -put $JOIN_OUTPUT_MERGED /Output/Task3/count_input/

# Step 3: Counting the number of trips per taxi company
echo "Starting count operation..."
hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapreduce.job.reduces=3 \
    -input /Output/Task3/count_input/join_output_merged.txt \
    -output /Output/Task3/count_output \
    -mapper mapper_count.py \
    -reducer reducer_count.py \
    -file mapper_count.py \
    -file reducer_count.py

# Merging the count output on the master node
echo "Merging count output..."
hdfs dfs -getmerge /Output/Task3/count_output/ $COUNT_OUTPUT_MERGED

# Step 4: Prepare sort input by uploading the combined count output to HDFS.
echo "Preparing HDFS for sort input..."
hdfs dfs -rm -r -f /Output/Task3/sort_input || true
hdfs dfs -mkdir -p /Output/Task3/sort_input
hdfs dfs -put $COUNT_OUTPUT_MERGED /Output/Task3/sort_input/

# Step 5: Sorting the taxi companies by number of trips
echo "Starting sort operation..."
hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapreduce.job.reduces=3 \
    -input /Output/Task3/sort_input/count_output_merged.txt \
    -output /Output/Task3/sort_output \
    -mapper mapper_sort.py \
    -reducer reducer_sort.py \
    -file mapper_sort.py \
    -file reducer_sort.py

# Merging the final sorted output on the master node
echo "Merging final sorted output..."
hdfs dfs -getmerge /Output/Task3/sort_output/ $FINAL_OUTPUT

# Verifying if the final output file was created successfully
if [ -f "$FINAL_OUTPUT" ]; then
    echo "Final output file $FINAL_OUTPUT exists."
else
    echo "Final output file $FINAL_OUTPUT does not exist."
    exit 1
fi

# Step 6: Sorting the final output locally by the second column (numerically)
echo "Sorting final output locally..."
if sort -k2,2n $FINAL_OUTPUT > $SORTED_OUTPUT; then
    echo "Sorted output file created: $SORTED_OUTPUT"
else
    echo "Failed to create sorted output file."
    exit 1
fi

# Upload the sorted output to HDFS
echo "Uploading sorted output to HDFS..."
hdfs dfs -mkdir -p /Output/Task3
hdfs dfs -put $SORTED_OUTPUT /Output/Task3/

echo "Script execution completed."
