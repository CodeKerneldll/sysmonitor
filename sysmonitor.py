# system_monitor.py
import psutil, time

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        print(f"CPU: {cpu}% | RAM: {ram.percent}% ({ram.used//1024**2}MB/{ram.total//1024**2}MB)")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nMonitor desligado")
