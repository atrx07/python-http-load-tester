# Python HTTP Load Teste

A lightweight multithreaded HTTP load testing tool written in Python.

This project was built by @atrx07 as a simple CLI utility to simulate HTTP requests and measure response performance. It uses a **controlled structure with built-in limits** to prevent misuse and encourage responsible testing practices.

### (installation and usage steps below)

---

## Description

This is a terminal-based load testing tool that sends concurrent HTTP requests to a target URL and measures metrics such as latency and requests per second.

The tool includes **safety limits and structured controls** to prevent excessive misuse while still allowing meaningful testing for development environments.

It is designed primarily for:

- Learning about concurrency in Python
- Testing personal or development servers
- Simple performance benchmarking

---

## Disclaimer

This project is intended **only for educational purposes and authorized testing**.

Do **not** use this tool against systems, servers, or networks without explicit permission from the owner.

The author is **not responsible for misuse** of this software.

---

## Warning

Improper use of load testing tools can disrupt services or cause unintended downtime.

Always ensure that you:

- Have **permission** to test the target server
- Use **reasonable request limits**
- Avoid testing production systems without proper authorization

---

## Features

- Multithreaded request workers
- Request timing using `perf_counter`
- Requests per second calculation
- Terminal progress display
- Colored CLI output
- Worker safety limits

---

## Usage

Run the tool from the terminal:

```
python main.py
```

Follow the prompts to enter:

- Target URL
- Number of workers
- Total number of requests

---

## Installation

Clone the repository:

```
git clone https://github.com/atrx07/python-http-load-tester.git
cd python-http-load-tester
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the tool:

```
python main.py
```

---

## Project Structure

```
python-http-load-tester
│
├── main.py
├── requirements.txt
├── releases
│   └── load_v1.py
└── README.md
```

---

## Requirements

Python 3.8+

Required Python packages:

```
requests
colorama
tqdm
```

Install them using:

```
pip install -r requirements.txt
```

---

## Example Output

```
┌──────────── ATRX ────────────┐

Starting load test...

Workers: 50
Total Requests: 1000

Progress: █████████████████ 100%

Results
--------------------------------
Total Requests: 1000
Success: 998
Failed: 2
Average Latency: 120ms
Requests/sec: 340
```

---

## License

This project is open source and free to use for educational purposes.
