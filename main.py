import requests
from fake_useragent import UserAgent
import json
import re

def get_header():
    return {
        'User-Agent' : UserAgent().random
    }

def CheckIp(ip,Agreement = 'http'):
    try:
        return requests.get(
            url = 'http://www.baidu.com',headers=get_header(),proxies={'{}'.format(Agreement):'{}://{}'.format(Agreement,ip)}
        ).status_code
    except:
        return 'Error'

if __name__ == "__main__":
    # https://www.89ip.cn/  89免费代理
    url = r'http://api.89ip.cn/tqdl.html?api=1&num=5000&port=&address=&isp='
    response = requests.get(url = url ,headers=get_header())
    for i in re.findall(r'\d+\.\d+\.\d+\.\d+:\d+',response.text):
        try:
            print(i + CheckIp(i))
        except:
            print(i+'失败')