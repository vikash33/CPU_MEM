import psutil
import sys

# Get the type of check: 'cpu', 'mem', or 'both'
check_type = sys.argv[1] if len(sys.argv) > 1 else "both"

# Get current CPU and memory usage
cpu_usage = psutil.cpu_percent(interval=1)
mem_usage = psutil.virtual_memory().percent

print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {mem_usage}%")

# Check if usage is high based on input
high_cpu = cpu_usage > 80 and (check_type == "cpu" or check_type == "both")
high_mem = mem_usage > 80 and (check_type == "mem" or check_type == "both")

if high_cpu or high_mem:
    print("\nHigh usage detected. Top 5 processes:")
    # Get all processes with their CPU and memory usage
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except:
            continue

    # Sort by combined CPU + memory usage
    top_processes = sorted(processes, key=lambda p: p['cpu_percent'] + p['memory_percent'], reverse=True)[:5]

    # Print top 5 processes
    for p in top_processes:
        print(f"PID: {p['pid']}, Name: {p['name']}, CPU: {p['cpu_percent']}%, MEM: {p['memory_percent']}%")
else:
    print("\nSystem usage is normal.")
