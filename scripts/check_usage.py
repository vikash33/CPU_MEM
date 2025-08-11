import sys
import subprocess

check_type = sys.argv[1] if len(sys.argv) > 1 else "both"

print(f"Check type: {check_type}")

def run_top(sort_by):
    if sort_by == "cpu":
        cmd = "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6"
    elif sort_by == "mem":
        cmd = "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6"
    else:
        return ""

    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return f"Error running command: {result.stderr}"

if check_type in ["cpu", "both"]:
    print("\nTop 5 CPU consuming processes:")
    print(run_top("cpu"))

if check_type in ["mem", "both"]:
    print("\nTop 5 Memory consuming processes:")
    print(run_top("mem"))
