# Web安全学习路线

2020/01/21

Ref: 
- 各厂商安服测试用例
- [ctf-wiki](https://ctf-wiki.github.io/ctf-wiki/)
- [Web-hacking-101 中文版](https://wizardforcel.gitbooks.io/web-hacking-101/)
- [awesome-ctf](https://github.com/apsdehal/aWEsoMe-cTf)
- security-testing课堂

## 0 Started

### 0.1 信息搜集

Passive域名枚举
 - https://www.virustotal.com/gui/domain/**(domain)**/relations
 - http://ipv4info.com/ censys shodan archive.org archive.is(webback) netcraft alexa netcraft dnsdumpster securitytrails 
 - https://scans.io/study/sonar.fdns_v2
    ```cat 2019-12-27-1512115201-fdns_a.json.gz| pigz -p 16 -dc| grep ".rhul.ac.uk" | jq .name```
 - [Regon-ng/alt-dns启动脚本]https://github.com/jhaddix/domain (需要python2版的Regon-ng待修复)
 - [域名字典 - SecList](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)
 - TLS证书数据库
    - https://crt.sh/?q=XXX
    - https://transparencyreport.google.com/https/certificates?hl=en&cert_search_auth=&cert_search_cert=cert_search=include_expired:true;include_subdomains:true;domain:XXX&lu=cert_search
    - censys
 - 基于ARP的host发现:[netdiscover](https://github.com/alexxy/netdiscover)
 - ICMPv6 Neighbor发现: [alive6](https://github.com/vanhauser-thc/thc-ipv6) 其他参见security_testing.md
 - ARP(缓存)投毒: Dsniff Arpoison Ettercap

服务
- chrome/firefox装**Wappalyzer**插件
- 漏洞库

功能
- OWASP ZAP或者**Burp Pro**在代理模式下继续探索网站（自动分析），构造错误地址/错误解析参数
- 思考有什么可能allowed的

目录
- 字典: dirb命令 等
- 爬虫: dirhunt

其他
- **[推荐]** [OWASP/Amass](https://github.com/OWASP/Amass)
- **[推荐]** [FuzzScanner](https://github.com/TideSec/FuzzScanner)
- [Google Hacking db](https://www.exploit-db.com/google-hacking-database)，[教程](https://www.blackhat.com/presentations/bh-europe-05/BH_EU_05-Long.pdf)
- maltego(人 邮件 Aliases等的关系) netglub 
- [Github repo scanner](https://github.com/UKHomeOffice/repo-security-scanner)
- [Gitrob - github repo scan](https://github.com/michenriksen/gitrob)

## 0.2 应用测试 （思路略）

https://github.com/FortyNorthSecurity/EyeWitness

`nmap -sSV -oA OUTPUTFILE -T4 -iL IPS.csv`

## 1 通用Web漏洞/业务逻辑漏洞

### 1.1 SQLI 

(1) 基础
- 看Ref
- [sqlmap用户手册](http://drops.xmd5.com/static/drops/tips-143.html)
- Mysql的`;--`以及后续查询后面要跟个空格  

(2) 防护
- 预编译语句(prepared statements) 
    ```
    prepare ins from 'insert into t select ?,?';
    mysql> set @a=999,@b='hello'; 
    mysql> execute ins using @a,@b; 
    mysql> select * from t;
    ```
- 使用Ruby on Rails / Django / Symphony,
    - Rails的SQLi列表：https://www.rails-sqli.org/ 

### 1.2 XSS

(1) 基础
- DOM-based/Blind/Self
    - Blind工具： XSShunter

(2) 杂记
- [OWASP XSS过滤器绕过速查表](https://owasp.org/www-community/xss-filter-evasion-cheatsheet)
- Cookie-httpOnly的有无: 不让任何API/脚本访问document.cookie
    - 无，可以试试alert document.cookie document.domain
    - 有，其他方式bypass [参考](https://www.freebuf.com/articles/web/129384.html)
- SOP(same-origin policy): 协议 主机 端口(http和https非同源)
- 使用alert(document.domain)判断XSS执行的源
- 浏览器内置的XSS Auditors可以绕过(js七十二变×)
- xss不一定马上执行
- js校验如果本地(client)做了，可能server上没做

(3) 防护

常用的防止XSS技术包括：

- 1. 与SQL注入防护的建议一样，假定所有输入都是可疑的，必须对所有输入中的script、iframe等字样进行严格的检查。这里的输入不仅仅是用户可以直接交互的输入接口，也包括HTTP请求中的Cookie中的变量，HTTP请求头部中的变量等。 

- 2. 不仅要验证数据的类型，还要验证其格式、长度、范围和内容。

- 3. 不要仅仅在客户端做数据的验证与过滤，关键的过滤步骤在服务端进行。

- 4. 对输出的数据也要检查，数据库里的值有可能会在一个大网站的多处都有输出，即使在输入做了编码等操作，在各处的输出点时也要进行安全检查。

### 1.3 SSRF 

### 0 Command Injection

(3) 防护: 不在应用层调用OS命令，否则使用白名单验证输入

### 0 L|R FI: Local and Remote File Inclusion

(1) 原理

- include 执行一个文件为php代码
- (optional)借助PHP Wrappers/Filters的LRFI

(2) 

(3) 防护

- 对PHP Wrappers/Filters进行限制，关闭eval()
- 禁用Allow_url_fopen/Allow_url_include
- 处理 / . %00
- 配置open_basedir(允许打开的目录) - 使用fopen()或file_get_contents()等时会进行文件位置检查
- 检查/tmp目录
- 使用硬编码的include，不允许动态获取文件名


