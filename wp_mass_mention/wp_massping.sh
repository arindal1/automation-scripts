#!/bin/bash

echo "Enter the size of the group:"
read group_size

if ! [[ $group_size =~ ^[0-9]+$ ]]; then
    echo "Please enter a valid integer for the group size."
    exit 1
fi

sleep 2  # Delay before starting

for ((i = 1; i <= group_size; i++)); do
    echo "@"
    for ((j = 0; j < i; j++)); do
        echo -e "\e[B"  # Press the "down" arrow key
    done
    echo ""
    echo -e "\eOM"  # Press "Enter"
    echo -e "\e[1S"  # Press "Shift+Enter"
    sleep 0.5  # Add a small delay between iterations
done
