import re
from collections import defaultdict


def parse_failed_ssh_attempts(log_file):
    ip_attempts = defaultdict(int)

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    ip = match.group(1)
                    ip_attempts[ip] += 1

    return ip_attempts


if __name__ == "__main__":
    log_path = "sample_logs/auth_sample.log"
    failed_attempts = parse_failed_ssh_attempts(log_path)

    print("SSH Failed Login Attempts by IP:\n")

    for ip, count in failed_attempts.items():
        print(f"{ip} -> {count} failed attempts")
