# 1 What the course is about

How do we provide reliable and secure communication for the data we send over a packet-switched internetwork?

How do we protect our networks and devices from hostile devices connected to the same internetwork? 

## 1.1 Course Content 

Networks and internetworks: 技术 服务 协议:TCP/IP等 

Non-cryptographic security: Data integrity, replay detection, message filtering, intrusion detection/ prevention systems 

Cryptographic security: Data confidentiality, data integrity, data origin authentication and entity authentication

Case studies: Wireless networks, mobile networks, TCP-AO, IPsec, TLS, DNSSEC.

# 2 Networks and internetworks

## 2.1  Concepts

A **network** is a collection of computing devices connected by a shared communication medium. The medium affects the "visibility" of network traffic and its susceptibility to errors. 

**Importance of Detecting Modifications**: 数字网络中传输着用于监视和管理网络的大量machine-to-machine消息，比如更新路由器上的转发表用的路由协议消息，还有连接URL/email与IP地址的DNS协议消息。这些消息受到更改会对网络与设备的正常工作造成极大影响。

**Circuit Switching**： 电路交换，预约传输线路，在通讯结束之前，该电路始终被这一对用户占用。Frequency-division multiplexing(FDM，频分多路复用), time-division multiplexing(TDM，时分多路复用)

- FDM：每个频带给一个持续通讯连接(duration connection)，频带、频带宽度

- TDM：将信道上传输时间划分为若干帧(frame)，每个帧有若干时间槽(time slot)。**不同帧中同一位置的时间槽均为某一特定连接使用**。[速率计算参见](https://blog.csdn.net/sinat_34640019/article/details/78072433)

[**Packet Switching（link）**](https://baike.baidu.com/item/%E5%88%86%E7%BB%84%E4%BA%A4%E6%8D%A2/1193080?fr=aladdin): 分组交换，先到先得。

- 分组：带有首部的数据段，首部指明了该分组发送的地址。

- store and forward: 交换机(switch)先得到该数据包的所有bit，才会forward给下一个router。Q条速率相同(假定)的线路，Q-1个routers，该数据包要被发送Q次，每次产生一个延时L/R，则一共产生Q*L/R个延时

- 与电路交换网相比，利用率高/数据率/排队机制/优先级

## 2.2 Vulnerabilities 

- Network Error: 通信过程bits改变
- Eavesdropping: confidentiality
- Modification: message integrity & message origin authenticity
- On-path Fabrication: message integrity & message origin authenticity 
- Off-path Fabrication: message origin authenticity，和on-path的区别在于是否干涉了原发信
- Interruption: availability

Type|Eavesdrop|Modify|Fabricate
-:|:-:|:-:|:-:
Active, on-path|$\color{green}{√}$|$\color{green}{√}$|$\color{green}{√}$
Active, off-path|$\color{red}{×}$|$\color{red}{×}$|$\color{green}{√}$
Passive, on-path|$\color{green}{√}$|$\color{red}{×}$|$\color{red}{×}$

> **总结1**: **Security** depends on
> - the functional and security requirements of the application data （需求）
> - the nature of the communication medium （传输介质特性）
> - the nature of the threats （威胁属性）

> **总结2**：使用分组交换意味着可能会引入error，由此我们需要的下列网络服务: 
    > - Addressing 寻址
    > - Forwarding 转发
    > - Detection of errors due to accidental modification (weak integrity) 对意外的查错
    > - Reliable delivery 可靠性
    > - In-order delivery 顺序


> **总结3**：使用shared network links或internetworks，需要以下安全服务：
    > - Confidentiality 机密性
    > - Detection of errors due to deliberate modification 
    (strong integrity) 对恶意的查错
    > - Detection of message replays 重放检测
    > - Confirmation of data orign (authentication) 消息来源验证

> **总结4**：总结2和总结3即为总结1提到的Network Security提出的缘由，这些services通过定义部署在网络上电脑的软件/硬件中的**协议**来实现。

# 3 Internetworks

## 3.1 Requirements 

从鼠标点击链接的整个访问过程（略），值得注意的是structure由http协议生成，content由link生成。

- Virtual Channel需求：
    
    - 消息发送到正确的设备 → device identifiers → network/internetwordk addresss
    - 消息发送到正确的程序 → application identifiers
    - Large messages需要被分割小型化以用network frames传输
    - messages必须被转化为network frames并在network link上传输

- **Reliable** Virtual Channel: 发送的必须到，到的必须一样
    - **identify** damaged/lost messages
    - **retransmit** damaged/lost messages
    - **identify**&**discard** duplicate messages
    - **order** received messages

- **Secure** Virtual Channel: 有害设备、机密内容
    - is disclosed to 3rd party? 加密消息
    - is modified? 完整性验证
    - Message确来自声称发送方: 来源验证

- Layered Processing: 消息处理按功能划分为层级结构，在传输层/网络层/数据链路层都要处理相关的specific information，或是检错，或是加密。详见TCP/IP模型。

## 3.2 Networks of Computers 

A **computer network** is a collection of computers that share a communication infrastructure. 

冲突域（物理层, 在同一个hub, switch的每一个端口都是一个冲突域）

广播域（数据链路层, switch的所有端口在一个广播域）

- 硬件地址
    - MAC(media access control) & network interface card
    - unicast(单点) message V.S. broadcast message

- 扩展网络的设备
    - Hub(集线器) 物理层 集合节点 无碰撞检测 （纯转发）
    - Repeater(中继器) 物理层 相同的网络的互联 扩大传输距离 （纯转发）
    - Switch(交换机) 数据链路层 多口 上位网桥
    - Bridge(网桥) 数据链路层 根据MAC转发帧 只有两个端口
    - Router(路由器) 网络层 读取ip 计算路径

- Link Encryption
    - 有线： 物理保护
    - 无线： LANs(如802.11)有加密

- Protection in Mobile Networks
    - 手机和基站之间有加密，but传输到公开交换电话网后没有
    - GSM(2G)只加密voice 主要是明文传输问题
    - UMTS(3G) LTE(4G) 通信传输的钓鱼可用MAC检测

## 3.3 Internetworks

- Concern: 
    - 唯一确定internetwork中每个host的身份
    - 能够传达消息给每个host

- 由于硬件地址标准各不相同，需要一个独立的标准
    - internet address = network identifier(netid) + host identifier(hostid)

- internetwork中的转发: 第一个网络帧由sender构造，最后一个网络帧由recipient处的edge router构造

- end-to-end secuirty: 
    - 无线网络中在网络边界(如无线路由器或基站)解密
    - 另外，应用数据应部署安全服务 → 只有接收方能解密/校错
    - IPsec 或 SSL/TLS 协议

## 3.4 网络协议与分层网络通信 

- Network Messages Structure:
    - A **network frame** is a "container" for a fixed number of bits.
    - 网络帧 = 应用数据 + 传输用信息(链路层的硬件地址;网络层的网络地址;传输层的端口号) 
    - 每部分的frame结构不一，比如TCP/UDP头16bits - 端口号; IP header


- OSI Layers (Layer - Unit - Purpose - Examples) 

- 网络协议实施
    - A **protocol** defines what the inputs and outputs of a processing step should be. 
    - 网络软件构造网络帧
    - 协议栈: 应用程序数据的处理可以看作发生在协议栈的层中(TCP/IP协议套件)
    - 协议处理前的叫service data unit，处理后的叫protocol data unit
        - TCP segment / UDP datagram 是PDU，也是IP协议的SDU **注意不要记反**
        - IP PDU即IP datagram，也是Ethernet/Bluetooth等链路层协议的SDU
        - Ethernet PDU即Ethernet frame

- Physical & Logical Communication Channels: 层级处理的网络效应体现在应用PDUs的交换上; 应用PDU的交换发生在virtual/logical信道上。

## 3.5 协议Vulns

- Vulns来源: 协议设计；协议实施；协议实施的配置

- Vulns影响: 无法提供安全服务(e.g. WEP不能提供完整性校验)
    - IP缺乏来源验证 → DoS (host)
    - 死亡之ping → buffer overflow
    - heartbleed → 信息泄露
    - SYN flood → DoS (TCP)

- 来自协议的:
    - 协议设计: TCP/IP不能精确IP数据报的来源；许多协议可
    - 缓存溢出 inappropriate随机数生成

- 来自基础设施协议:
    - 名称解析: ARP(ip2mac) DNS(NS2ip)
    - 路由协议: OSPF BGP RIP

- 应用层协议: Announcement/Query-response

- 传输层协议: TCP(reliable)/UDP(unreliable)

- reliable protocol必stateful, unreliable protocol倾向于是stateless
    - IP和HTTP是stateless协议
    - stateful比stateless应对off-path攻击更安全，因为off-path无法猜测state information（比如TCP序号）

- Internet Protocol: [IP数据包checksum计算](https://www.cnblogs.com/zafu/p/10822164.html)/[frame结构](https://upload.wikimedia.org/wikipedia/commons/7/72/Ethernet_Frame.png)用程序员计算器蛮简单的

## 3.6 网络通信的安全服务

- wireshark看不到frame的FCS(帧校验序列), 因为校验失败的被丢弃了; FSC计算了MAC(SRC+DST),length/type,DATA, 详见CRC32

- VPN会加密整个IP数据包包括IP地址，否则不会加密

- 一个frame有两个checksum，一个计算application data，由收件人验证一次；一个计算网络地址，由每个路由器验证

- 除非checksum计算用了什么只有通信双方知道的密钥，否则收件人无法鉴别恶意修改和伪造。

- Key Agreement & Ciphersuite Negotiation
    - 预先交换; 通过互联网交换; 保护交换过程

- 安全服务的尺度(scope)
    - 数据链路层的加密只能保证单个network的机密性(?)
    - host-to-host protection: SSL/TLS/IPsec (transport mode)
    - network-to-network protection: IPsec (tunnel mode), 路由器到路由器之间(?)
    - link protection: WEP/WPA/WPA2, host到路由器之间
    - 有些安全服务可能会在离开/进入收发方所在网络时被配置或移除(VPN和无线蜂窝网络)

- 除了保护message还要保护host
    - 运行有缺陷网络协议的host可能受到攻击
        - crash(死亡之ping SYN洪水)
        - 信息泄露(heartbleed)
        - 攻击第三者: 某种smurf攻击
    - 对策
        - 验证message来源
        - 正确实现协议
        - 去除不要的协议
        - 对某些host network, 屏蔽协议messages

# 4 网络协议与漏洞

## 4.1 tcp/ip协议栈

- HTTP PDU是TCP SDU; TCP PDU是IP SDU; IP PDU是Ethernet SDU. 
- 同一层的协议提供了类似服务的不同实施方式
- 高层协议可能会使用底层协议的服务(应用层使用TCP/UDP);HTTP利用TCP的可靠性, TCP利用IP的互联网消息传输(IP本来就是用于delivery的)
- 不同层协议独立(把ipv4换成ipv6对HTTP和TCP无影响)
- 因此可以插入中间协议
- IP的最大长度是两个字节(TotalLength)能表示的上限:65535
    - [包含可选项的ip的Header Length和Total Length计算](https://zhidao.baidu.com/question/364836343.html)
    
### 4.1.1 tcp/ip协议栈的安全服务

- IPsec: IP SDU(如TCP段)的安全服务
    - 协议1 Authentication Header(AH), 完整性
    - 协议2 Encapsulating Security Payload(ESP), 完整性+机密性
    - 会加一个AH header到IP body中

- TLS: SSL标准化的产物
    - 在TCP投和应用层PDU之间加了一个Record Layer
    - 封装应用层PDU 所以不会加密IP头
    - 对称加密、公私钥不对称加密、密钥交换算法

### 4.1.2 封装顺序

<img src="/images/orderOfEncapsulation.png" width="auto">

选用不同的安全服务，处理流程不同; 仅供参考，参见课件159/836。

> 总结： 
    应用层需要的服务包括： 
    1. point-to-point传输 (连接层)
    2. host-to-host传输 (网络层)
    3. application-to-application传输(传输层)
    4. 可靠传输 (同数据完整性)
    5. 顺序传输

## 4.2 传统tcp/ip攻击

- IP Spoofing → IPsec
    IP协议 checksum 无验证 易伪造
- smurf攻击 → 限制攻击者的能动性
    - ICMP(internet control message protocol) 网络层协议 在主机和路由器之间报错
    - 结合IP欺骗假装受害者身份，发出大量ICMP request; 受害者会被ICMP response淹没(出现大量echo报文)
    - **发送ICMP request到广播地址**，所有host都会向受害者发送ICMP response
    - 无法验证ICMP request来源，可以采用Ingress filtering(入过滤)/配置路由器不转发到广播地址的入包/配置边缘路由器drop外部ICMP包

- The Ping of Death → 打补丁,使OS不再对过大的包进行重组
    - IP fragmentation
        - identification段一致
        - flag作尾标记
        - fragment offset用于定位
    - IP数据报超过2^16字节，未作对应(只copy 2^16)的话，会发生buffer overflow
    - 攻击者构造fragment和>2^16的ICMP包

- TCP SYN flooding
    - TCP握手: ack=上一个seq+1
    - server(不一定是server，可能是正常host(?))有一个储存half-open连接的表，发送SYN/ACK后会加个entry到表里。但正在使用TCP的应用内存有限。
    - 如果client没发送ACK, server就会一直保留half-open直到资源用尽
    - 攻击者伪装不同的ip地址发SYN包 → 两种DoS: 
        - server无法处理TCP连接
        - 被伪装的主机被server block,无法使用服务

- **TCP Connection Sproofing** → 随机设置初始序列号ISN
    - TCP是stateful协议，所以off-path attack会失败
        - SYN/ACK发往正确的ip地址
        - (未遂)受害人受到SYN/ACK，发送RST使B停止half-open连接
    - - attacker需要:
      - victim不能发送RST → 使用SYN Flooding瘫痪victim
      - 与victim互动，猜测其所用Initial Sequence Number
      - 与B互动防止发信到victim
    - attacker不会受到B的消息，但可以向B发消息/使用remote shell protocol

- DNS Cache Poisioning 
    - domain name system 
    - off-path比on-path难, 类似TCP注入攻击, 需要猜QID/ISN

## 4.3 总结

- Outgoing Messages的安全问题
    - 加密算法提供confidentiality
    - 加密算法用于协议中提供integrity和来源验证
    - 数字签名提供integrity和来源验证

- Incoming Messages的安全问题
    - 默认所有Messages不可信
    - sender身份认证
    - 过滤
    - 去除不需要的服务和协议

- TCP/IP的安全问题
    - 不知道真实来源(IP欺骗/ARP或DNS缓存投毒)
    - 用尽资源(MAC洪水 DoS)
    - **非confidentiality的问题，无法通过加密解决**

# 5 IP Addresses, Forwarding, Routing

## 5.1 互联网地址

[ABCD类ipv4地址等基础知识](:https://www.cnblogs.com/BrokenSwitch/p/8473472.html)

- CIDR(Classless Inter-Domain Routing, 无类别域间路由)
    - 连续的1表示net-id, 连续的0表示host-id(子网掩码的来源)
    - CIDR表示法:192.168.23.35/21, 21表示net-id
    - CIDR block (略)

- [自治系统](https://baike.baidu.com/item/%E8%87%AA%E6%B2%BB%E7%B3%BB%E7%BB%9F/129715?fr=aladdin): = 路由选择域(routing domain), 运行相同的路由协议
    - 多出口的自治系统(Multihomed AS), 互联
    - 末端自治系统(Stub AS)
    - 中转自治系统(Transit AS)

- 私有IPv4地址 
    - 可重复使用的IP地址, 不可转发到不同的network
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16

## 5.2 构建转发表

- 交换机/网桥: 硬件地址; 最简单的搭建方式是监视网络流量，如果没有Dest Addr的入口，交换机会广播到所有接口(因为是交换机，同network，不同network link的所有host都会收到该信息)
- 路由器: 其他网络的net-id
- 
- 

## 5.3 IP数据包重写



# Wordlist

highly distributed, highly heterogeneous(异构的)

tamper with = modify maliciously

Prior Knowledge: 事先知悉，先验知识；联想到了什么？

message authentication code = checksum + cryptographic algorithms

propagate: 传播

spoofing: 欺骗 

[复用(mutiplexing)](https://baike.baidu.com/item/%E5%A4%8D%E7%94%A8/9857249)，频分复用FDM/时分复用TDM/统计时分复用STDM（TDM上位）/波分复用WDM（波长代替频率）/码分复用CDM（同样的时间，同样的频带，不同码型）