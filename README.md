# CMDB
### 部署环境
* OS：Linux
* Python：3.x
* Django：2.x
### 部署架构
Gunicorn+Ngnx+Supervisor
### 部署步骤
### 克隆项目到本地
    
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
