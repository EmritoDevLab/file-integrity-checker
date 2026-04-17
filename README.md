# File Integrity Checker

A simple Python-based File Integrity Checker that monitors files for changes using SHA-256 hashing.

This project demonstrates a basic defensive security concept: detecting unauthorized file modifications through file integrity monitoring.

## Overview

The File Integrity Checker scans a folder, calculates SHA-256 hashes for the files inside it, and compares them to a saved baseline. If a file has been modified, deleted, or added, the tool reports it in the terminal.

## Features

- Creates a baseline of file hashes.
- Detects modified files.
- Detects deleted files.
- Detects newly added files.
- Stores results in JSON format.
- Uses a simple command-line interface.

## Technologies Used

- Python 3
- hashlib
- json
- os
- sys

## How It Works

### 1. Initialize a Baseline
On the first run, the tool scans the selected directory and saves a hash for each file in `baseline.json`.

### 2. Check File Integrity
On the next run, the tool scans the directory again and compares the current hashes with the saved baseline.

### 3. Show the Results
The tool reports whether each file is unchanged, modified, deleted, or new.

## Example Project Structure

```text
file-integrity-checker/
├── integrity_checker.py
├── baseline.json
├── test_files/
│   ├── log1.txt
│   └── log2.txt
└── README.md
```

## Usage

### Create a baseline

```bash
python integrity_checker.py init test_files
```

### Check file integrity

```bash
python integrity_checker.py check test_files
```

## Example Output

```text
[OK] test_files/log1.txt
[MODIFIED] test_files/log2.txt
[NEW] test_files/log3.txt
[DELETED] test_files/old_log.txt
```

## Why This Project Matters

File integrity monitoring is a valuable security practice for detecting tampering, unexpected changes, and possible compromise. This project shows a practical application of defensive cybersecurity concepts in a simple and understandable way.

## Future Improvements

- Add logging to a file.
- Add CSV export.
- Handle locked files more gracefully.
- Support individual files as well as directories.
- Add timestamps for each scan.
- Add email alerts for detected changes.
- Build a small GUI with Tkinter.
- Add colored terminal output.

## LinkedIn Summary

This project is a Python-based File Integrity Checker that detects unauthorized file changes using SHA-256 hashing.

It was built to practice file integrity monitoring, monitoring, and defensive security fundamentals.

## Contact

If you want to connect, I am building hands-on cybersecurity projects to strengthen my practical skills in monitoring, detection, and defensive security.
