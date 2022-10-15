# shutil module is used to calculate the disc space
# psutil module is used to calculate the cpu usage
import shutil, psutil
#du=shutil.disk_usage("/")
#print(du)

# % of free disc space

#free_disc_space=(du.free/du.total)*100
#print(free_disc_space)



#psutil.cpu_percent(0.1)  # how much of cpu is being used


def chec_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    return free > 20

def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    return usage < 75

if not chec_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print("Everything is ok")

