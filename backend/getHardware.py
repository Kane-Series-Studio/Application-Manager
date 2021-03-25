
from tabulate import tabulate
import GPUtil
import psutil
import platform


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


cpufreq = psutil.cpu_freq()
PhysicalCords = psutil.cpu_count(logical=False)
TotalCords = psutil.cpu_count(logical=True)
MaxCPUFreq = f"{cpufreq.max:..2f}"
MinCPUFreq = f"{cpufreq.min:..2f}"
Cores = cores()


def CPUPrintOut():
    print("="*40, "CPU Info", "="*40)
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print("CPU Usage Per Core:")


def cores():
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")


svmem = psutil.virtual_memory()
TotalRAM = get_size(svmem.total)
AvailableRam = get_size(svmem.available)
UsedRAM = get_size(svmem.used)
PercentageRAM = get_size(svmem.percent)
swap = psutil.swap_memory()
totalSWAP = get_size(swap.total)
freeSWAP = get_size(swap.free)
usedSWAP = get_size(swap.used)
percentageSWAP = get_size(swap.percent)


def getRamOut():

    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")


uname = platform.uname()
System = uname.system
NodeName = uname.node
Release = uname.release
Version = uname.version
Machine = uname.machine
Processor = uname.processor


def InfoSystem():

    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")


#! BLOW THIS CODE IS NOT USABLE METHODS, THESE ARE SINCE THEY MUST BE FUNCTIONS, WILL BE UPDATED LATER!!
#! BLOW THIS CODE IS NOT USABLE METHODS, THESE ARE SINCE THEY MUST BE FUNCTIONS, WILL BE UPDATED LATER!!
#! BLOW THIS CODE IS NOT USABLE METHODS, THESE ARE SINCE THEY MUST BE FUNCTIONS, WILL BE UPDATED LATER!!
#! BLOW THIS CODE IS NOT USABLE METHODS, THESE ARE SINCE THEY MUST BE FUNCTIONS, WILL BE UPDATED LATER!!
#! BLOW THIS CODE IS NOT USABLE METHODS, THESE ARE SINCE THEY MUST BE FUNCTIONS, WILL BE UPDATED LATER!!
#! BLOW THIS CODE IS NOT USABLE METHODS, THESE ARE SINCE THEY MUST BE FUNCTIONS, WILL BE UPDATED LATER!!
#! BLOW THIS CODE IS NOT USABLE METHODS, THESE ARE SINCE THEY MUST BE FUNCTIONS, WILL BE UPDATED LATER!!
#! BLOW THIS CODE IS NOT USABLE METHODS, THESE ARE SINCE THEY MUST BE FUNCTIONS, WILL BE UPDATED LATER!!

'''
partitions = psutil.disk_partitions()


def getDisk():
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_device = print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")


if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:

        if str(address.family) == 'AddressFamily.AF_INET':

            # VARIABLES
            Address = Address.address
            AddressNetmask = address.netmask
            AddressBrodcastIP = address.broadcast
        elif str(address.family) == 'AddressFamily.AF_PACKET':

            # VARIABLES
            AddressMAC = address.address
            AddressNetMask = address.netmask
            AddressBrodcastMAC = address.broadcast

net_io = psutil.net_io_counters()
TotalBytesSent = get_size(net_io.bytes_sent)
TotalBytesRecevied = get_size(net_io.bytes_recv)


def getGpu():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
        gpu_load = f"{gpu.load*100}%"
        # get free memory in MB format
        gpu_free_memory = f"{gpu.memoryFree}MB"
        # get used memory
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                       "temperature", "uuid")))'''
