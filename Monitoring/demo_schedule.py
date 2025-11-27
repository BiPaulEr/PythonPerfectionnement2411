import schedule, time, psutil


def get_cpu_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_usage_per_cpu = psutil.cpu_percent(interval=1, percpu=True)
    return f"CPU : {cpu_usage} - {cpu_usage_per_cpu}"

def get_ram_info():
    mem = psutil.virtual_memory()
    return f"RAM : {mem.percent}%"   

def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    return f"DISK : {disk_usage.percent}%"   

def info_system():
    print(get_cpu_info())
    print(get_ram_info())
    print(get_disk_info())

schedule.every(1).seconds.do(info_system)

while True:
    schedule.run_pending()
    time.sleep(0.05)