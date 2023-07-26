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

if __name__ == "__name__":
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()

        print("CPU Usage: {}%".format(cpu_usage))
        print("Memory Usage: {}%".format(memory_usage['percent']))

        time.sleep(5)
