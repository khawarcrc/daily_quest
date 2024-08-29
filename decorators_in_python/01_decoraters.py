# def my_decorator(func):
#     def wrapper():
#         print("before the function is called")
#         func()
#         print("after the function is called")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("hello")


# say_hello()
import psutil

def monitor_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {usage}%")
    if usage > 80:
        print("Warning: High CPU usage")

monitor_cpu_usage()
import psutil


import psutil

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

# Get memory usage
memory_info = psutil.virtual_memory()
print(f"Memory Usage: {memory_info.percent}%")


# # List all running processes
# for process in psutil.process_iter(['pid', 'name', 'status']):
#     print(f"PID: {process.info['pid']}, Name: {process.info['name']}, Status: {process.info['status']}")
