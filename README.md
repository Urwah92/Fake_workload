
# CPU Workload Generator

This tool simulates CPU usage over time and generates a CSV file with the simulated data. It's useful for testing, analysis, or creating synthetic workload patterns.

### Download the binary
    curl -LO https://github.com/cloud-bulldozer/kube-burner/releases/download/v1.15.2/kube-burner-V1.15.2-linux-x86_64.tar.gz

### Extract
    tar -xzf kube-burner-V1.15.2-linux-x86_64.tar.gz

### Move to path
    chmod +x kube-burner
    mv kube-burner /usr/local/bin/

### Verify
    kube-burner version

---

##  How to Use

###  Prerequisites

- Python 3 installed (`python3 --version`)
- Bash (default on Linux/macOS)

---

### Run the Script

Use the `run_cpu_generator.sh` script with the following flags:

    ./run_cpu_generator.sh -t <duration> -i <interval> -c <min,max> -o <output.csv>


| Flag | Description                                     | Example         |
| ---- | ----------------------------------------------- | --------------- |
| `-t` | **(Required)** Total duration in seconds        | `-t 60`         |
| `-i` | Sampling interval in seconds *(default: 1)*     | `-i 1`          |
| `-c` | Min and Max CPU usage (comma-separated)         | `-c 15.0,80.0`  |
| `-o` | Output CSV filename *(default: cpu\_usage.csv)* | `-o output.csv` |

### Example
This will simulate CPU usage between 15% and 80% every 1 second for 60 seconds:

    ./run_cpu_generator.sh -t 60 -i 1 -c 15.0,80.0 -o output.csv



### Delete Pods
Command for k3s:

    k3s kubectl delete pod -n namespace -l name=kubelet-density


# More pods on a single node (For Minikube)
SSH into Minikube:

    minikube ssh

Edit the kubelet config:

    sudo vi /var/lib/kubelet/config.yaml

Add:

    maxPods: 1000

Right under:

    cgroupDriver: systemd

Save the file and restart kubelet:

    sudo systemctl restart kubelet

Exit Minikube SSH:

    exit
Verify from host:

    kubectl describe node | grep -i pods
