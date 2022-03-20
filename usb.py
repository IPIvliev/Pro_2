import os
import pyudev
from glob import glob
 
def main():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    c=0
    for device in iter(monitor.poll, None):
 
        if device.action == 'add' and c == 0:
            
            path = glob("/media/pi/*/")
            print(path[0])
            c = 1
 
        if device.action == 'remove':
            c = 0
 
if __name__ == '__main__':
    main()