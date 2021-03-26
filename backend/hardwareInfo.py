import platform
import cpuinfo
import psutil
from psutil import virtual_memory
import wmi
from tabulate import tabulate
import GPUtil

runningProcessesF = wmi.WMI()

class taskmanager:
    
    def getProcessor(self):
        self.yourProcessor = platform.processor()
        return self.yourProcessor

    def getBits(self):
        self.yourBits = cpuinfo.get_cpu_info()['bits']
        return self.yourBits

    def getBrand(self):
        self.yourBrand = cpuinfo.get_cpu_info()['brand_raw']
        return self.yourBrand

    def getHZ(self):
        self.yourHZ = cpuinfo.get_cpu_info()['hz_actual']
        return self.yourHZ

    def getCpuVersion(self):
        self.yourCpuVersion = cpuinfo.get_cpu_info()['cpuinfo_version_string']
        return self.yourCpuVersion

    def getProcesses(self):
        self.runningProcesses = []
        for process in runningProcessesF.Win32_Process():
            self.runningProcesses.append(f"{process.Name}")
        return self.runningProcesses


def getDisk(what):
    totalmem = 0
    freemem = 0
    usedmem = 0

    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        totalmemstr = int(''.join([i for i in get_size(partition_usage.total)[:-4] if i.isdigit()]))
        freememstr = int(''.join([i for i in get_size(partition_usage.free)[:-4] if i.isdigit()]))
        usedmemstr = int(''.join([i for i in get_size(partition_usage.used)[:-4] if i.isdigit()]))
        totalmem += totalmemstr
        freemem += freememstr
        usedmem += usedmemstr
    
    if what == "used":
        return usedmem
    elif what == "free":
        return freemem
    elif what == "total":
        return totalmem

 

    

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        


tm = taskmanager()
svmem = psutil.virtual_memory()

#### all variables

processor = tm.getProcessor()
bits = tm.getBits()
brand = tm.getBrand()
hz = tm.getHZ()
cpuVersion = tm.getCpuVersion()
processes = tm.getProcesses()
TotalRAM = get_size(svmem.total)
AvailableRam = get_size(svmem.available)
UsedRAM = get_size(svmem.used)
PercentageRAM = get_size(svmem.percent)
TotalMemory = getDisk("total")
FreeMemory = getDisk("free")
UsedMemory = getDisk("used")

