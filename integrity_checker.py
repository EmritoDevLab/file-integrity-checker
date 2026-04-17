import hashlib
import json
import os
import sys

BASELINE_FILE = "baseline.json"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def build_baseline(directory):
    baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            baseline[path] = calculate_hash(path)
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)
    print("Baseline created and saved.")

def check_integrity(directory):
    if not os.path.exists(BASELINE_FILE):
        print("No baseline found. Please run init first.")
        return

    with open(BASELINE_FILE, "r") as f:
        old_baseline = json.load(f)

    current_baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            current_baseline[path] = calculate_hash(path)

    for path, old_hash in old_baseline.items():
        if path not in current_baseline:
            print(f"[DELETED] {path}")
        elif current_baseline[path] != old_hash:
            print(f"[MODIFIED] {path}")
        else:
            print(f"[OK] {path}")

    for path in current_baseline:
        if path not in old_baseline:
            print(f"[NEW] {path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python integrity_checker.py <init|check> <directory>")
    elif sys.argv[1] == "init":
        build_baseline(sys.argv[2])
    elif sys.argv[1] == "check":
        check_integrity(sys.argv[2])
    else:
        print("Invalid command. Use 'init' or 'check'.")