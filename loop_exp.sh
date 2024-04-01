#!/bin/bash
model=$1
num_shot=$2
list_datasets=("dtd" "vgg_flower" "aircraft" "cub" "omniglot" "fungi" "traffic_signs" "mscoco" "quickdraw")
# Base directory where the YAML files are stored
base_dir="./configs/benchmark/${num_shot}-shot/${model}"
results_path="./results/benchmark/${num_shot}-shot/${model}"
# Create the results directory if it does not exist
mkdir -p "$results_path"
# Loop through each method
for method in "NCC" "LR" "matchingnet" "finetune"; do
    # Path to the method's directory
    method_dir="$base_dir/$method"

    # Check if the directory exists
    if [ -d "$method_dir" ]; then
        echo "Running experiments for method: $method"
        
        # Loop through each dataset in the list_datasets array
        for dataset in "${list_datasets[@]}"; do
            yaml_file="$method_dir/$dataset.yaml"
            echo "test $yaml_file"

            # Check if the YAML file exists
            if [ -f "$yaml_file" ]; then
                # Define the result file path
                result_file="$results_path/$method/$dataset.pt"

                # Check if the result file already exists
                if [ ! -f "$result_file" ]; then
                    echo "Running experiment with config: $yaml_file"
                    # Ensure the directory for this method exists
                    mkdir -p "$results_path/$method"
                    # Run the Python command with the YAML configuration
                    tsp python main.py --cfg "$yaml_file" --save-stats "$result_file"
                else
                    echo "Result file $result_file already exists. Skipping..."
                fi
            else
                echo "YAML file $yaml_file does not exist. Skipping..."
            fi
        done
    else
        echo "Directory for method $method and $model does not exist."
    fi
done
