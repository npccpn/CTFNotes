# PHP伪协议

[CTF-WEB：PHP 伪协议 - 乌漆WhiteMoon - 博客园](https://www.cnblogs.com/linfangnan/p/13535097.html)

## 文件包含函数

+ include()

+ include_once()——当重复调用同一文件时只调用一次

+ require()——执行如果发生错误，函数会报错并终止脚本

+ require_once()——当重复调用同一文件时只调用一次

## PHP支持的伪协议

+ file://——访问本地文件系统

+ http://——访问HTTP(s)网址

+ php://——访问各个输入/输出流

+ phar://——PHP归档

+ zip://——压缩流

## 举例

1. ?file=php://filter/read=convert.base64-encode/resource=index.php
   **php://filter/** 是一种访问本地文件的协议
   **/read=convert.base64-encode/** 表示读取的方式是 base64 编码
   **resource=index.php** 表示目标文件为index.php
   如果不进行 base64 编码传入，index.php 就会直接执行，无法看到文件中的内容

2. **php://input**可以访问请求的原始数据的只读流，可以读取 POST 请求的参数

3. **data://** 将include的文件流重定向到用户控制的输入流
   
   ```
   /test.php?file=data://text/plain;base64,PD9waHAgcGhwaW5mbygpO2V4aXQoKTsvLw==
   ```

4. **phar://** 发现有一个文件上传功能，无法绕过，仅能上传jpg后缀的文件。与此同时，无法进行文件包含截断。allow_url_include=on 的状态下，就可以考虑phar伪协议绕过。
   写一个shell.php文件，里面包含一句话木马。然后，压缩成xxx.zip。然后改名为xxx.jpg进行上传。最后使用phar进行包含  
   这里的路径为上传的 jpg 文件在服务器的路径
   
       /index.php?id=phar://路径/xxx.jpg/shell

5. **zip://** 上述phar:// 的方法也可以使用 zip://
   
   把1.php文件压缩成zip，再把zip的后缀改为png，上传上去，并且可以获得上传上去的png的地址。
   
   1.zip文件内仅有1.php这个文件
   
   ```
   /php?file=zip://1.png%231.php  
   
   // 也可以尝试不改名为png，直接使用zip上传测试一下
   /php?file=zip://1.zip%231.php  
   ```
   
   



有待看懂

[CTF之PHP命令执行 - hithub - 博客园](https://www.cnblogs.com/meng-han/p/16735478.html)

https://zhuanlan.zhihu.com/p/37648302


