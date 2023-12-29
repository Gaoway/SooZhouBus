import requests
import json
import time
from tkinter import messagebox


class szgj:
    def __init__(self) -> None:
        self.url = 'https://szgj.2500.tv/api/v1/busline/bus?line_guid=0000000000LINELINEINFO18082357212871'
        self.suse = 12
        self.ustc = 24
        self.len = 4
        self.name = '1021'

    def get_bus_info(self, url):
        businfo = requests.get(url)
        businfo_json    = json.loads(businfo.text)
        self.businfo    = businfo_json['data']['standInfo']

        return self.businfo
       
    def load_info(self):
        self.get_bus_info(self.url)
        self.bus_serial = []
        for i in self.businfo:
            if len(self.businfo[i]) == 0:
                continue
            info = self.businfo[i][0]
            serial = int(info['serial'])
            self.bus_serial.append(serial)
        return self.bus_serial

    def ustc_req(self):
        self.load_info()
        self.ustc_gap = 100
        gap_list = []
        for i in self.bus_serial:
            gap = self.ustc - i
            if gap > 0:
                gap_list.append(gap)
                if self.ustc_gap > gap:
                    self.ustc_gap = gap
        print(self.name,'bus to ustc: ', gap_list)
        return gap_list

    def sushe_req(self):
        self.load_info()
        self.sushe_gap = 100
        for i in self.bus_serial:
            gap = self.suse - i
            if gap > 0:
                if self.sushe_gap > gap:
                    self.sushe_gap = gap
        print('closest bus to sushe: '+ str(self.sushe_gap))
        return self.sushe_gap

    def monitor_ustc(self): 
        i=40
        while(i>=0): 
            i=i-1
            self.ustc_req()
            if (self.ustc_gap == self.len or self.ustc_gap == self.len-1):
                print(f'{self.name} 即将进站{self.ustc_gap}')
                messagebox.showinfo(f'{self.name} 即将进站',f'{self.name} 即将进站{self.ustc_gap}')
                if i >= 6:
                    i = 6
            time.sleep(30)

class bus1021(szgj):
    def __init__(self) -> None:
        super().__init__()
        self.url = 'https://szgj.2500.tv/api/v1/busline/bus?line_guid=0000000000LINELINEINFO18082357212871'
        self.suse = 12
        self.ustc = 24
        self.len = 4
        self.name = '1021'

class bus143(szgj):
    def __init__(self) -> None:
        super().__init__()
        self.url = 'https://szgj.2500.tv/api/v1/busline/bus?line_guid=1aa773c8-e865-4847-95a1-f4c956ae02ef'
        self.suse = 0
        self.ustc = 29
        self.len = 3
        self.name = '143'

class bus146(szgj):
    def __init__(self) -> None:
        super().__init__()
        self.url = 'https://szgj.2500.tv/api/v1/busline/bus?line_guid=96c177f0-0828-4a31-ba19-ddce9e9649e0'
        self.suse = 0
        self.ustc = 22
        self.len = 3
        self.name = '146'

class busall(bus1021, bus143, bus146):
    def __init__(self) -> None:
        super().__init__()
        self.bus1021 = bus1021()
        self.bus143 = bus143()
        self.bus146 = bus146()

    def monitor_ustc(self):
        i=40
        buslist = newlist =  [self.bus1021, self.bus143, self.bus146]
        while(i>=0):
            i=i-1
            buslist = newlist
            newlist = []
            for bus in buslist:
                gap_list = bus.ustc_req()       
                if len(gap_list) != 0:
                    newlist.append(bus)
                if (bus.ustc_gap == bus.len or bus.ustc_gap == bus.len-1):
                    print(f'{bus.name} 即将进站 {bus.ustc_gap}')
                    if i >= 10:
                        i = 10
                time.sleep(1)
            time.sleep(30)


if __name__ == '__main__':
    #szgj146    = bus146()
    #szgj1021   = bus1021()
    #szgj143    = bus143()
    #szgj1021.monitor_ustc()
    #szgj146.monitor_ustc()
    #szgj146.monitor_ustc()
    szgjall = busall()
    szgjall.monitor_ustc()
