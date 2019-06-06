import requests
import sys
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class waybackMachineClass():

        def __init__(self,domain):
                self.waybackURL = "https://web.archive.org/cdx/search?url="+domain+"%2F&matchType=prefix&collapse=urlkey&output=json&fl=original%2Cmimetype%2Ctimestamp%2Cendtimestamp%2Cgroupcount%2Cuniqcount&filter=!statuscode%3A%5B45%5D..&limit=100000&_=1547318148315"
                self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        def getUrls(self):
                r = requests.get(self.waybackURL,headers=self.headers)
                html = r.text
                jsonObj = json.loads(html)
                return jsonObj

