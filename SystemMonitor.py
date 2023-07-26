import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1, percpu=True)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'available': mem.available,
        'used': mem.used,
        'percent': mem.percent
    }

cpu_usage = get_cpu_usage()
memory_usage = get_memory_usage()

print("CPU Usage:")
for i, cpu in enumerate(cpu_usage):
    print(f"Core {i}: {cpu}%")
    print("Memory Usage:")
    print(f"Total: {memory_usage['total'] / (1024 ** 3):.2f} GB")
    print(f"Available: {memory_usage['available'] / (1024 ** 3):.2f} GB")
    print(f"Used: {memory_usage['used'] / (1024 ** 3):.2f} GB ({memory_usage['percent']}%)")
    print("----------------------")

    time.sleep(5)

