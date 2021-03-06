# CMDB
### 部署环境
* OS：CentOS 7
* Python：3.x
* Django：2.x
### 部署架构
Gunicorn+Ngnx+Supervisor
### 部署步骤一：准备环境
#### 部署MySQL(部署过程省略)
#### 克隆项目到本地
    git clone https://github.com/blueboay/CMDB.git
#### 安装Python3.x
    yum install python34 python34-pip
#### 安装Django2.x
    python3.4 -m pip install django
#### 安装Nginx
    yum install nginx
#### 安装Gunicorn和Supervisor
    yum install supervisor
    python3.4 -m pip install gunicorn
#### 安装项目依赖Python模块
    python3.4 -m pip install pyDes
    python3.4 -m pip install PyMySQL
    python3.4 -m pip install requests
    python3.4 -m pip install redis
### 部署步骤二：修改配置
创建Supervisor配置文件：

    [program:gunicorn]
    directory= /Path/Tp/ProjectName
    command = /usr/bin/gunicorn ProjectName.wsgi -b 127.0.0.1:8000
    user = root
    autostart= true
    autorestart= true
    redirect_stderr = true
    stdout_logfile = /var/log/gunicorn.log
创建Nginx配置文件：

    server {
    
        listen 5000;
        
        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_next_upstream http_500 http_502 http_503 error timeout invalid_header;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $remote_addr;
        }
        
        location ~.*\.(html|css|js)$ {
            root /Path/Tp/ProjectName;
            proxy_next_upstream http_500 http_502 http_503 error timeout invalid_header;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $remote_addr;
        }
    }
修改settings.py连接数据库配置：

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cmdb',
            'HOST': '192.168.1.1',
            'PORT': '3306',
            'USER': 'username',
            'PASSWORD': '123456',
        }
    }
同步数据库配置：

    python3.4 manage.py makemigrations
    python3.4 manage.py migrate
### 部署步骤三：启动验证
    systemctl start supervisord.service
    systemctl enable supervisord.service
    systemctl start nginx
    systemctl enable nginx
