import requests , time
from bs4 import BeautifulSoup

class Proxy:
    
    def __init__(self,https=False):
        '''
        Set https = True if you wish to use an HTTPS website. \n
        https must be of type boolean
        '''
        if type(https)!=bool:
            raise ValueError(f'https must be of type boolean, got {type(https)} instead')
        self.https = https

        if https:
            self.checkIpUrl = 'https://api.ipify.org/?format=json'
        else:
            self.checkIpUrl = 'http://api.ipify.org/?format=json'
        self.setProxy()
        
        
    def updateIpList(self):
        '''
        This Method Pulls All Free Proxy Server From The Website https://free-proxy-list.net/.
        '''
        self.timeOfUpdate = time.time()
        self.id = 0
        proxyList = requests.get('https://free-proxy-list.net/')
        soup = BeautifulSoup(proxyList.text,'lxml')
        self.listOfIp = soup.find('tbody').findAll('tr')
    
    def setProxy(self):  
        '''
        This Method Gathers All Available Free Proxy Servers And Establishes A Connection With Them.        
        '''
        self.updateIpList()
        self.session = requests.Session()
        self.changeIp()
        # return session
        
    def changeIp(self):
        '''
        This Method Finds The Next Proxy Server That Is Available And Connects To It.
        '''
        while True:
            if 350 <= int(time.time() - self.timeOfUpdate):                  # update list every 5 min 
                self.updateIpList()
            data = self.listOfIp[self.id].findAll('td')
            self.currentIp = data[0].text
            proxyPort = data[1].text
            country = data[3].text
            is_https = data[6].text
            if self.https and is_https == 'no':
                self.id+=1
                continue
            protocols = 'http'
            self.session.proxies={
                'http': protocols+'://'+self.currentIp+':'+proxyPort,
                'https': protocols+'://'+self.currentIp+':'+proxyPort
                }
            try:
                print(f"Ip : {self.currentIp}       connecting...",end='\r')
                response = self.session.get(self.checkIpUrl,timeout=10).json()
                print(f"Ip : {self.currentIp}       Connected    ")
                print(f"Ip :      {response['ip']}\nCountry : {country}\nHttps :   {is_https}")
                # print(f"IP :      {response['ip']}\nCountry : {country}")
                self.id +=1
                return None
                # return self.session
            except:
                print(f"Ip : {self.currentIp}       Falied       ")
                self.id +=1
                
    def close(self):
        '''
        Close The Session
        '''
        self.session.close()
                
                