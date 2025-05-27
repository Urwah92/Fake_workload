import argparse
import csv
import random
import time
import numpy as np
import pandas as pd

def generate_cpu_data_numpy(duration, interval, min_cpu, max_cpu, output):
    steps = duration // interval
    timestamps = np.arange(0, duration, interval)
    cpu_usage = np.round(np.random.uniform(min_cpu, max_cpu, size=steps), 2)
    df = pd.DataFrame({'time_sec': timestamps, 'cpu_percent': cpu_usage})
    df.to_csv(output, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate CPU usage and export to CSV.")
    parser.add_argument("--duration", type=int, required=True, help="Total duration in seconds")
    parser.add_argument("--interval", type=int, default=1, help="Sampling interval in seconds")
    parser.add_argument("--min-cpu", type=float, default=10.0, help="Minimum CPU usage %")
    parser.add_argument("--max-cpu", type=float, default=90.0, help="Maximum CPU usage %")
    parser.add_argument("--output", type=str, default="cpu_usage.csv", help="Output CSV filename")
    args = parser.parse_args()
    generate_cpu_data_numpy(args.duration, args.interval, args.min_cpu, args.max_cpu, args.output)
