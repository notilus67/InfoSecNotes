# 0 智慧卡攻击简述

- Social Attacks(啥玩意儿？？)
- 硬件攻击 Hardware Attacks
    - 物理/入侵: 接触硅芯片 Physical/Invasive: Obtaining Access to the Silicon
        - 芯片探测与总线读取 Chip Probing and Bus Reading
        - 逆向 Reverse Engineering
        - 芯片重写攻击 Chip Rewriting Attacks
        - 钻探(?) Drilling
    - 侧信道 Side Channel
        - 故障感应攻击 Fault Induction Attacks
            - 故障攻击 Glitch Attacks
            - 差分故障攻击 Differential Fault Analysis(DFA)
        - 直接内存读取 Direct Memory Reading
        - 功耗分析 Power Analysis
            - 简单功率分析 Simple Power Analysis(SPA)
            - 差分功率攻击 Differential Power Analysis(DPA)
        - 电磁辐射 Radiation Electromagnetic Radiation
        - 时间攻击(?) Timing Attacks
- 逻辑攻击 Logical Attacks
    - Java卡平台攻击 Java card Platform Attacks

# 1 Lecture 1

## 1.1 啥是smart card

- Magnetic Stripe Card
磁条卡容易篡改(no tamper resistance) 相对容易被copy

- Smart Card: integrated circuit card / embedded microcomputer chip
    - Components
        - CPU
        - ROM: **OS**
        - EPROM: **初始化, lock bytes**, 一次写，永久读
        - EEPROM: **应用/OS扩展**, 写/擦/读永久
        - RAM: **OS/应用的工作空间**, 写/擦/读临时数据
        - FLASH: flash属于广义的EEPROM，因为它也是电擦除的ROM。但是flash做的改进就是擦除时不再以字节为单位，而是以块为单位，一次简化了电路，数据密度更高，降低了成本。上M的ROM一般都是flash。
    - passive / active(powered) 
    - limitations
        - 无电源、时钟
        - 证书撤销列表 (revocation list?)
        - Data Storage
- Powered/Communicating by Radio:
    - 电磁感应: A passive contact-less smart card/RFID is powered by electromagnetic induction. 
    - 不同模式的调制/调谐Modulation. 
- NFC (Near Field Communication，近场通信)
    - 等同于手机的contact-less接口
    - 读卡器模式(Reader/Writer mode) / 仿真卡模式 (Card Emulation Mode) / 点对点模式 (Peer to Peer Mode)
- Information in the Card 
    - 应用 Application(s)
    - 密钥 Cryptographic Keys
    - 操作系统 Smart card operating system(SCOS)
    - 系统策略 Smart card operating system policies
    - 持卡人 cardholder data
    - 签发人 issuer data
    - card management data
    - card manufacturing data
- Smart Card Lifecycle
    - 组装 Manufacturing (chip & card)
    - 初始化 Initialisation
    - 个性化 Personalisation
    - 使用 Utilisation
    - 终结 Termination

## 1.2 smart card 商业运用
- 移动通信: SIM (多应用Java卡), IMSI、密钥Ki/Kc、A3/8算法(基于RAND和Ki计算)

- 银行业
    - 磁条卡: 盗刷(skimming)、伪造(counterfeiting)
    - chip cards (EMV, by Europay, Mastercard & Visa)
        - EMV缺陷（略过，参见slides和[EMVtechReport](https://www.cs.ru.nl/E.Poll/papers/EMVtechreport.pdf)）

## 1.3 新兴应用

- 卫星TV卡
    - global secret
    - one-way communication
    - key分配/管理问题

- trasport exploits (略)

## 1.4 开发工具

- SIM Toolkit

- Wireless Browser(?)

- Java (java card)

- Multos: c/c++开发

- 兼容DIY(汇编/C微控制器)

## 1.5 SIM应用安全

- 逻辑攻击 
    - 窃听接口
    - RFID Sniffer
    - Key cracker(?)
- 物理攻击
    - chip/circuit 监视更改
    - 需要Probe station(探测站?), FIB for track/circuit modification (聚焦离子束电路更改)
- 安全性: 
    - PIN
    - GSM加密不足

## 1.6 标准

ISO, GSM/3GPP, Java Card, EMV, Multos, ITSO

## 1.7 OTA

over the air, 安全性需另查资料

## 1.8 嵌入式系统安全

- 仿造产品检测
    - 图形化监视(?)Visual Inspection
    - 开封 decapsulation
    - X光 监视
- 硬件木马
    - 形式验证\功能测试\光学监视\侧信道\木马检测电路
- 攻击目标:
    - 硬件本身
    - 设备中的永久数据
    - runtime数据
    - 程序控制流
    - 程序指令
- CPS: 略

## 1.9 补充结论

没什么特别要注意的，仅随意摘选：

1. 智慧卡范畴: 银行卡 SIM 电子护照 身份证 交通卡 卫星电视

2. 智慧卡可添加标准化的应用层安全以克服系统缺陷(?)

3. 智能卡是一种网络安全资产和重要的使能器，但通常只是复杂系统安全解决方案的一部分。