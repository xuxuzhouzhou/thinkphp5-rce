import argparse
import sys
import textwrap
import time

import requests
requests.packages.urllib3.disable_warnings()

def main(url):
    full_url = f"{url}/toLogin"
    headers = {"Upgrade-Insecure-Requests": "1",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    data = {"username":"admin", "password":"123456"}
    try:
        response = requests.get(full_url, headers=headers, allow_redirects=False, verify=False, timeout=1 )
    except Exception:
        print(f"[-]{url}请求失败")
        return
    dic = response.json()
    if  dic.get("code") == 200 and dic.get("msg")== None:
        print(f"[+]{url}存在默认口令 admin:123456")
    else:
        print(f"[-]{url}不存在默认口令")
if __name__ == '__main__':
    start_time = time.time()
    with open("url.txt",mode="r",encoding="u8") as f:
        for line in f:
            line = line.strip()
            main(line)
    end_time = time.time()
    print(f"all done,task {end_time-start_time}s")

