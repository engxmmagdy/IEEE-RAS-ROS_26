

import platform
import datetime

def log_system_info():
    sys_type = platform.system()
    time = datetime.datetime.now()
    with open("sys_log.txt","w") as file:
        file.write("system type: "+format(sys_type)+"\n")
        file.write("timestamp: "+format(time)+"\n")

def main():
    log_system_info()

if __name__ == "__main__" :
    main()