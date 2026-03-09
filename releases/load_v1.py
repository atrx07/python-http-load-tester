import threading
import time
import urllib.request
import urllib.error
import sys

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_header():
    print(f"""{CYAN}
╔══════════════════════════╗
║             ATRX07         
║ Python HTTP Load Tester     
╚══════════════════════════╝
{RESET}""")

print_header()

target_url = input("Target URL (ex: http://localhost:8000): ").strip()
workers = int(input("Number of workers (max 200): "))

# Worker safety limit
if workers > 200:
    print(f"{RED}Error:{RESET} Maximum allowed workers is 200.")
    print(f"{YELLOW}Please run the test again with 200 or fewer workers.{RESET}")
    sys.exit()

duration = int(input("Test duration (seconds): "))

success = 0
errors = 0
latencies = []

lock = threading.Lock()
stop_time = time.time() + duration


def worker():
    global success, errors

    while time.time() < stop_time:
        start = time.perf_counter()

        try:
            req = urllib.request.Request(
                target_url,
                headers={"User-Agent": "PythonLoadTester/1.0"}
            )

            with urllib.request.urlopen(req, timeout=5) as response:
                response.read(1)

            latency = time.perf_counter() - start

            with lock:
                success += 1
                latencies.append(latency)

        except Exception:
            with lock:
                errors += 1


def progress_bar():
    while time.time() < stop_time:
        remaining = stop_time - time.time()
        elapsed = duration - remaining

        progress = min(elapsed / duration, 1)
        bar_length = 30
        filled = int(bar_length * progress)

        bar = "█" * filled + "-" * (bar_length - filled)

        sys.stdout.write(
            f"\r{CYAN}Test Progress:{RESET} |{bar}| {elapsed:.1f}/{duration}s"
        )
        sys.stdout.flush()

        time.sleep(0.2)


threads = []

print(f"\n{CYAN}Target:{RESET} {target_url}")
print(f"{CYAN}Workers:{RESET} {workers}")
print(f"{CYAN}Duration:{RESET} {duration}s")

print(f"\n{YELLOW}Starting load test...\n{RESET}")

# Start worker threads
for _ in range(workers):
    t = threading.Thread(target=worker, daemon=True)
    t.start()
    threads.append(t)

# Start progress bar thread
p = threading.Thread(target=progress_bar)
p.start()

# Wait for workers
for t in threads:
    t.join()

p.join()

total = success + errors
avg_latency = sum(latencies) / len(latencies) if latencies else 0
rps = total / duration if duration > 0 else 0

print(f"\n\n{CYAN}----- Test Results -----{RESET}")
print(f"{GREEN}Total Requests:{RESET} {total}")
print(f"{GREEN}Successful:{RESET} {success}")
print(f"{RED}Errors:{RESET} {errors}")
print(f"{YELLOW}Average Latency:{RESET} {avg_latency:.4f} sec")
print(f"{CYAN}Requests per second:{RESET} {rps:.2f}")

#this comment is to shiw that ive amde a change on this day
