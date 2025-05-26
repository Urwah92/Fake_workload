#!/bin/bash

# Default values
DURATION=""
INTERVAL=1
MIN_CPU=10.0
MAX_CPU=90.0
OUTPUT="cpu_usage.csv"

# Parse flags
while getopts "t:i:c:o:" opt; do
  case $opt in
    t) DURATION="$OPTARG" ;;         # Total duration in seconds
    i) INTERVAL="$OPTARG" ;;         # Interval in seconds
    c) 
      IFS=',' read -r MIN_CPU MAX_CPU <<< "$OPTARG"
      ;;
    o) OUTPUT="$OPTARG" ;;           # Output CSV file name
    \?) echo "Invalid option -$OPTARG" >&2; exit 1 ;;
  esac
done

# Validate required input
if [ -z "$DURATION" ]; then
  echo "Error: Duration (-t) is required"
  echo "Usage: ./run_cpu_generator.sh -t <duration> -i <interval> -c <min,max> -o <output.csv>"
  exit 1
fi

# Run the kube-burner file
kube-burner init -c kubelet-density.yml --kubeconfig /etc/rancher/k3s/k3s.yaml
# Run the Python script
python3 generate_cpu_workload.py --duration "$DURATION" --interval "$INTERVAL" --min-cpu "$MIN_CPU" --max-cpu "$MAX_CPU" --output "$OUTPUT"
