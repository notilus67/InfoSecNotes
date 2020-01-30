# Professor

- vulns of transport cards 
- (currently) randomness analysis & hardware security analysis
- network security for IoT
- applications in cyber-criminal investigation

# 1 Lecture 1 

## 1.1 Open Resources

1. ssh into linux.cim.rhul.ac.uk
    账号同no-machine

2. ssh into pentest3.isg.rhul.ac.uk 
    new@pentest3.isg.rhul.ac.uk
    imnewhere

3. https://media.ccc.de/c/36c3

## 1.2 Stages (仅供参考)

- Target scoping

- Information gathering

- Target discovery

- Enumerating targets

- Vulnerability mapping 

- Social engineering

- Target exploitation

- Privilege escalation

- Maintaining access

- Documentation and reporting

## 1.3 Methodology
> 有点兴趣但是**没时间**全看啊，至少面试前把OWASP系列重新看一百年吧

> 更了解对象; 可重复的过程; 渗透测试不像攻击，客户需要划定范围使其模仿恶意意图，否则鲜有价值

- NIST SP 800-115: Guide to Information Security Testing and Assessment (2008)
    - 这里面说testing是比较预期与实际，examination是一整套评估

- PCI: Penetration Testing Guidance (2015)
    - 有个Report Evaluation Tool

- PTES: Penetration Testing Execution Standard (2014)
    - 事前交互 Pre-engagement interactions
    - 情报搜集 Intelligence gathering
    - 威胁建模 Threat modelling: 威胁建模是一种通过确定目标和漏洞，然后对抗措施来防止或减轻威胁对系统的影响，从而优化网络/应用程序/互联网安全的过程. 
    - 漏洞分析 Vulnerability analysis
    - 漏洞利用 Exploitation
    - 后利用(?) Post-expolitation
    - 报告 Reporting

- OWASP: Open Web Application Security Project Testing (2014)
    - 信息搜集
    - 配置和部署管理
    - 身份管理
    - 验证测试(Authentication)
    - 认证测试(Authorization)
    - 会话管理
    - 输入验证
    - error处理
    - weak密码学
    - 商业逻辑
    - 客户端
    - 移动服务
    - 云服务
    - HTTP DOS

- SP11: A Web Application Hacker's Methodology

- OSSTMM: Open Source Security Testing Methodology Manual (2010)
    - 有个security量化计算公式

## 1.4 Further

讨论test和审计的区别；讨论黑白灰盒测试的区别.

读Kali Linux: Assuring
Security by Penetration Testing, Part I.2: Penetration Testing Methodology

[读公开的pentest报告](https://github.com/juliocesarfort/public-pentesting-reports/tree/master/OffensiveSecurity)

# Lecture 2 Information Gathering 

- Passive（接触目标) 
- Semi-passive（假装正常流量）
- active(直接连接)

## 2.1 潜在interest

域名 子网 系统架构 可达IP 网络协议 running服务 系统枚举 WAF/IDS/IPS 访问控制 远程访问

## 2.2 具体策略（不全）

GOOGLE的高级搜索(待补) site filetype 

[Google Hacking db](https://www.exploit-db.com/google-hacking-database), [教程](https://www.blackhat.com/presentations/bh-europe-05/BH_EU_05-Long.pdf)

DNS部分：基本略过
 - WHOIS用的是TCP 43端口
 - dns的区域传输只准从primary server到secondary server
 - rDNS(reverse dns)主要是防垃圾邮件用 

host发现
 - `nmap -sn 192.168.1.0/24`
 - IP ping`nmap -sn --disable-arp-ping -P0 192.168.1.0/24`
 - TCP SYN Ping(其他还有TCP ACK Ping、UDP Ping等) `nmap -sn --disable-arp-ping -PS80 10.13.37.0/24`
 - OS识别 
 - [You can -j REJECT but you can not hide: Global
scanning of the IPv6 Internet](https://media.ccc.de/v/33c3-8061-you_can_-j_reject_but_you_can_not_hide_global_scanning_of_the_ipv6_internet)
 - traceroute/tcptraceroute/ping -R命令
 
# Lecuture 3 Enumerating Targets & Vulnerability Mapping

## 3.1 Port Scan

- Port Scan 有一种情况是被blocked, (firewall / packet filter), 用nmap TCP ACK scan的话大概还是能猜出来

- Detection & Prevention
    - Network Intrusion Detection System: 部分扫描选项可以pass
    - Firewalls
        - Network: basic packet filtering (stateless)
        - Net/Trans: stateful packet filtering
        - Transport: Circuit Level Gateway / Proxy
        - Application: Application layer firewalls

Skype的p2p语音传输: UDP "session"

**待调查:**Avoid firewall: [Loose Source and Record Route](https://security.stackexchange.com/questions/33313/does-loose-source-and-record-route-drop-the-source-address/33334#33334)

nmap -sF / -sA 结合FIN和ACK扫描，找

- 其他工具: ZMap Masscan

- nc/telnet xxx.xxx.xx.xx 22 

## 3.2 Service

FTP(21) Telnet(23) SMTP(25) TFTP(69) 未加密

Finger(79) 未授权

DNS(53)没打补丁

SNMP(UDP 161) 信息泄露 默认密码

SMB 枚举恭喜那个文件，略 

## 3.3 自动扫描器

[Nessus](https://zh-cn.tenable.com/products/nessus/nessus-essentials?tns_redirect=true) OpenVAS 

 # Wordlist

Double blind: 受验双方都不清楚详情, black box通常是其一环

Red Teaming: 红队测试, 将不局限于传统渗透测试,将更着重于针对企业人员、业务系统、供应链、办公系统、企业物理安全等真实脆弱点进行攻击评估。

pre/post-execution: 执行前后


