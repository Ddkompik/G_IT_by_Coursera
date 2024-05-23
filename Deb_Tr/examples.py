import psutil

res_cpu = psutil.cpu_percent()
print(res_cpu)
res_disc = psutil.disk_io_counters()
print(res_disc)
res_net = psutil.net_io_counters()
print(res_net)
