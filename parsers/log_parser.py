def parse_failed_ssh_attempts(log_file):
    failed_attempts = []

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                failed_attempts.append(line.strip())

    return failed_attempts


if __name__ == "__main__":
    log_path = "sample_logs/auth_sample.log"
    failed_logs = parse_failed_ssh_attempts(log_path)

    print("Failed SSH Login Attempts:\n")
    for log in failed_logs:
        print(log)
