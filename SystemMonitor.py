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

def get_disk_usage():
    partitions = psutil.disk_partitions()
    disk_usage = {}
    for partition in partitions:
        try: 
            usage = psutil.disk_usage(partition.mountpoint)
            disk_usage[partition.device] = {
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            }
        except Exception as e:
            print(f"Error getting disk usage for {partition.device}: {e}")
    return disk_usage


cpu_usage = get_cpu_usage()
memory_usage = get_memory_usage()
disk_usage = get_disk_usage()

# CPU Usage
print("CPU Usage:")
for i, cpu in enumerate(cpu_usage):
    print(f"Core {i}: {cpu}%")

# Memory Usage
print("\nMemory Usage:")
print(f"Total: {memory_usage['total'] / (1024 ** 3):.2f} GB")
print(f"Available: {memory_usage['available'] / (1024 ** 3):.2f} GB")
print(f"Used: {memory_usage['used'] / (1024 ** 3):.2f} GB ({memory_usage['percent']}%)")

# Disk Usage    
print("\nDisk Usage:")
for partition, usage_info in disk_usage.items():
    print(f"{partition}:")
    print(f"Total: {usage_info['total'] / (1024 ** 3):.2f} GB")
    print(f"Used: {usage_info['used'] / (1024 ** 3):.2f} GB ({usage_info['percent']}%)")
    print(f"Free: {usage_info['free'] / (1024 ** 3):.2f} GB")
    print(f"Usage: {usage_info['percent']}%\n")


print("----------------------")

time.sleep(5)

