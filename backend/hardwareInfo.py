import platform
import cpuinfo
import psutil
import wmi

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
        


tm = taskmanager()
#### all variables
processor = tm.getProcessor()
bits = tm.getBits()
brand = tm.getBrand()
hz = tm.getHZ()
cpuVersion = tm.getCpuVersion()
processes = tm.getProcesses()




