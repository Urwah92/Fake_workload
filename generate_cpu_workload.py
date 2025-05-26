import argparse
import csv
import random
import time

def generate_cpu_data(duration, interval, min_cpu, max_cpu, output):
    data = []
    start_time = int(time.time())

    for i in range(0, duration, interval):
        timestamp = i  # relative time in seconds
        cpu_usage = round(random.uniform(min_cpu, max_cpu), 2)  # simulate CPU usage
        data.append({"time_sec": timestamp, "cpu_percent": cpu_usage})

    with open(output, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["time_sec", "cpu_percent"])
        writer.writeheader()
        writer.writerows(data)
    print(f"[+] Generated CPU data saved to: {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate CPU usage and export to CSV.")
    parser.add_argument("--duration", type=int, required=True, help="Total duration in seconds")
    parser.add_argument("--interval", type=int, default=1, help="Sampling interval in seconds")
    parser.add_argument("--min-cpu", type=float, default=10.0, help="Minimum CPU usage %")
    parser.add_argument("--max-cpu", type=float, default=90.0, help="Maximum CPU usage %")
    parser.add_argument("--output", type=str, default="cpu_usage.csv", help="Output CSV filename")
    
    args = parser.parse_args()
    generate_cpu_data(args.duration, args.interval, args.min_cpu, args.max_cpu, args.output)
