
### 程序结构：
```
fabric/
├── bin
│   ├── __init__.py
│   ├── __pycache__
│   └── run.py
├── conf
│   ├── __init__.py
│   └── user_info
├── core
│   ├── __init__.py
│   ├── main.py
│   └── __pycache__
│       ├── __init__.cpython-35.pyc
│       └── main.cpython-35.pyc
├── download
│   ├── abc.pdf
│   └── tt.sh
├── Fabric.png
└── README.txt

```

### 示例数据
[app]  
vm1={"user": "root", "password": "freedom", "ip": "10.0.0.11","port":"22"}  
vm3={"user": "root", "password": "freedom", "ip": "10.0.0.13","port":"22"}  

解释：
[app]为主机分组信息
vm1={"user": "root", "password": "freedom", "ip": "10.0.0.11","port":"22"} 和vm3={"user": "root", "password": "freedom", "ip": "10.0.0.13","port":"22"}  为主机信息
每个主机信息中包含user,password,ip,port四项信息。
	
### 运行环境：
    Python3.0或以上版本环境均可。


### 执行方法：：
	cd fabric/bin/
	python run.py
	

### 使用方法：
    系统支持以下:
	put  file_name
	get file_name
	其他系统支持的命令，top等持续返回结果的命令除外。
	
	