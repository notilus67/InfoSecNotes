# Software Security

## Content 
- Network Security
- Application Security
- Web Sec
- Mobile Sec
- Advanced threats 

```
int main(){
    int a = 34;
    char c[] = "hello";
    printf(a); // segmentation fault
    printf(&a); //"
    printf("%d",a); //34
    printf("%d",&a);  //地址 
    printf(c); //hello
    printf("%d",c); //地址
    printf(&c); //hello
    printf(&c+1); //"
    return 0;
}
```

## Lecture 1

- Memory Safe Languages (Rust etc.)

- [Common Weakness Enumeration](http://cwe.mitre.org/index.html)

- 蓝牙低能源数据传输
    - handle(数据地址) <--> label <--> value
    - 手机→Request for handle 0x00AD("Heart Rate Measurement")→智能手表
    - 智能手表→Response 0x00AD=80bpm→手机
    - handle地址有鉴权操作 - 需要蓝牙配对 - 加密传输
    - 使用Connect(Android API Call)的恶意程序不同于传统蓝牙(?)，无scan，可以隐藏要求的权限(?)
        - 使用BLE传输, 应用数据对所有应用可见，所以需要应用层加密

- 