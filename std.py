import requests
import json
import logging
import time
from config import station, station1, url
from tkinter import messagebox


class szgj:
    def __init__(self) -> None:
        self.url    = url
        self.station    = station
        self.station1   = station1
        self.sushe  =   12
        self.ustc   =   24

    def get_bus_info(self):
        businfo = requests.get(self.url)
        businfo_json    = json.loads(businfo.text)
        self.businfo_std    = businfo_json['data']['standInfo']

        return self.businfo_std
       
    def target_req(self, target):
        self.get_bus_info()
        min = 40
        min_info    = {}
        for i in self.businfo_std:
            bus_stat    = self.station1.index(i)
            if (target-bus_stat)>0 and (target-bus_stat)<min :
                min = (target-bus_stat)
                min_info    = self.businfo_std[i]
        
        return min, min_info
    
    def ustc_req(self):
        min, min_info   = self.target_req(self.ustc)
        print('closest bus to ustc: '+ str(min))
        print('closest bus info:')
        for i in min_info:
            print(i)
        time.sleep(1)
            
    def sushe_req(self):
        min, min_info   = self.target_req(self.sushe)
        print('closest bus to wenhui: '+ str(min))
        print('closest bus info:')
        for i in min_info:
            print(i)
        time.sleep(1)
    
    def get_station_info(self):
        self.get_bus_info()
        station_info = {}
        for i in self.businfo_std:
            bus_stat    = self.station1.index(i)
            station_info.update({bus_stat:self.businfo_std[i]})
        self.station_info   = station_info
        return self.station_info
        
    def target_req1(self, target, length=3):
        self.get_station_info()
        sort_station    = sorted(self.station_info, reverse=True)
        target_station  = []
        for i in sort_station:
            if i< target and len(target_station)<length:
                target_station.append(i)
        return target_station
                
    def ustc_req1(self, length = 3):
        target  = self.ustc
        target_station  = self.target_req1(target, length)
        
        print(f'>>>-------------{target-target_station[0]}站-------------<<<')
        
        for i in target_station:
            print(f'{self.station[self.station1[i]]}--arrival distance to 苏研院: {target-i}')  
            print(f'bus info: {self.station_info[i]}')
        
        return target_station
          
    def sushe_req1(self, length = 2):
        target  = self.sushe
        target_station  = self.target_req1(target, length) 
        print(f'>>>-------------{target-target_station[0]}站-------------<<<')
        for i in target_station:
            print(f'{self.station[self.station1[i]]}--arrival distance to 文荟公寓: {target-i}')  
            print(f'bus info: {self.station_info[i]}')
        
        return target_station
    
    def watch_ustc(self):
        echo = 20
        i=0
        while(i<=echo): 
            i=i+1
            target_station  = self.ustc_req1()
            if (self.ustc-max(target_station)==4 and self.ustc-max(target_station)>2):
                print(f'即将进站{self.ustc-max(target_station)}')
                messagebox.showinfo('即将进站',f'即将进站{self.ustc-max(target_station)}')
                break
            time.sleep(30)
        
            
if __name__ == '__main__':
    szgj    = szgj()
    #szgj.ustc_req1() 
    #szgj.sushe_req1()
    szgj.watch_ustc()
    

        
        