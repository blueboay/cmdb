from django.shortcuts import render, HttpResponse
from AssetManagement import models
import pyDes
import base64

# Create your views here.
Key = "Gogenius"
Iv = "Gogen123"


# 加密
def encrypt_str(data):
    # 加密方法
    method = pyDes.des(Key, pyDes.CBC, Iv, pad=None, padmode=pyDes.PAD_PKCS5)
    # 执行加密码
    k = method.encrypt(data)
    # 转base64编码并返回
    return base64.b64encode(k)


# 解密
def decrypt_str(data):
    method = pyDes.des(Key, pyDes.CBC, Iv, pad=None, padmode=pyDes.PAD_PKCS5)
    # 对base64编码解密
    k = base64.b64decode(data)
    # 再执行Des解码并返回
    return method.decrypt(k)


# 获取主机超级用户密码并改成bytes类型
def get_password(data):
    password = models.HostInfo.objects.filter(id=data).values()[0]["SuperUserPass"]
    return password.encode("UTF-8")


# 获取主机信息所有数据
def get_host_data():
    return models.HostInfo.objects.all()


# 获取主机环境所有数据
def get_group_data():
    return models.HostGroup.objects.all()


# 获取主机分组表所有数据
def get_env_data():
    return models.HostENV.objects.all()


# 获取主机名
def get_host_name(host_id):
    server_name = models.HostInfo.objects.filter(id=host_id).values("ServerName")[0]["ServerName"]
    return server_name


# 检查主机名，分组名，环境名是否重复
def check(request):
    post_data = request.POST
    for i in post_data:
        name = post_data[i]
        if i == "host_name":
            if models.HostInfo.objects.filter(ServerName=name):
                return HttpResponse("Error")
            else:
                return HttpResponse("OK")
        elif i == "group_name":
            if models.HostGroup.objects.filter(ServerName=name):
                return HttpResponse("Error")
            else:
                return HttpResponse("OK")
        elif i == "env_name":
            if models.HostENV.objects.filter(ServerName=name):
                return HttpResponse("Error")
            else:
                return HttpResponse("OK")
        else:
            pass


# 主页
def index(request):
    return render(request, 'index.html')


# 环境分组
def host_environment_info(request):
    return render(request, 'am/hostENVInfo.html', {'data': get_env_data()})


# 主机分组
def host_group_info(request):
    return render(request, 'am/hostGroupInfo.html', {'data': get_group_data()})


# 资产列表
def host_info(request):
    all_data = render(request, 'am/hostInfo.html', {'data': get_host_data(),
                                                    "hostData": get_group_data(),
                                                    "envData": get_env_data()})
    post_data = request.POST
    if request.method == "POST":
        if post_data["ENVName"] != "环境" or post_data["GroupName"] != "分组" or post_data["Other"] != "":
            return HttpResponse("此功能尚未开发完成...")
        else:
            return all_data
    else:
        return all_data


# 资产列表详细信息
def host_more_info(request):
    get_data = request.GET
    host_data = models.HostInfo.objects.filter(id=get_data["host"]).values()
    server_name = get_host_name(get_data["host"])
    group_data = models.HostAndHGroup.objects.filter(ServerName=server_name).values("GroupName")

    # 将获取的密码进行解密，再转换成str类型
    decrypt_password = (decrypt_str(get_password(get_data["host"]))).decode("UTF-8")

    return render(request, 'am/hostMoreInfo.html', {"data": host_data,
                                                    "groupData": group_data,
                                                    "password": decrypt_password})


# 添加主机
def add_host(request):
    if request.method == "POST":
        data = request.POST
        group_names = data.getlist("HostGroup")
        for group_name in group_names:
            models.HostAndHGroup.objects.create(
                ServerName=request.POST["ServerName"],
                GroupName=group_name,
            )
        models.HostInfo.objects.create(
            ServerName=request.POST["ServerName"],
            IP=request.POST["IP"],
            RemotePort=request.POST["RemotePort"],
            SuperUser=request.POST["SuperUser"],
            #  存入数据库前先进行加密，再更改为str类型
            SuperUserPass=(encrypt_str(request.POST["SuperUserPass"])).decode("UTF-8"),
            Environment=request.POST["Environment"],
            OSType=request.POST["OSType"],
            OSVersion=request.POST["OSVersion"],
            Zabbix=request.POST["Zabbix"],
            Salt=request.POST["Salt"],
            Jumpserver=request.POST["Jumpserver"],
            Keepass=request.POST["Keepass"],
            Note=request.POST["Note"],
        )
    return render(request, "am/addhost.html", {"envData": get_env_data(), "hostGroupData": get_group_data()})


# 编辑主机信息
def change_host_info(request):
    if request.method == "POST":
        post_data = request.POST
        get_data = request.GET
        old_host_name = get_host_name(get_data["id"])
        models.HostAndHGroup.objects.filter(ServerName=old_host_name).delete()
        group_names = post_data.getlist("HostGroup")
        for group_name in group_names:
            models.HostAndHGroup.objects.create(
                ServerName=request.POST["ServerName"],
                GroupName=group_name,
            )
        models.HostAndHGroup.objects.filter(ServerName=old_host_name).update(ServerName=request.POST["ServerName"])
        models.HostInfo.objects.filter(id=get_data["id"]).update(
            ServerName=request.POST["ServerName"],
            IP=request.POST["IP"],
            RemotePort=request.POST["RemotePort"],
            SuperUser=request.POST["SuperUser"],
            #  存入数据库前先进行加密，再更改为str类型
            SuperUserPass=(encrypt_str(request.POST["SuperUserPass"])).decode("UTF-8"),
            Environment=request.POST["Environment"],
            OSType=request.POST["OSType"],
            OSVersion=request.POST["OSVersion"],
            Zabbix=request.POST["Zabbix"],
            Salt=request.POST["Salt"],
            Jumpserver=request.POST["Jumpserver"],
            Keepass=request.POST["Keepass"],
            Note=request.POST["Note"],
        )
        return HttpResponse("OK")


# 添加主机分组
def add_host_group(request):
    if request.method == "POST":
        models.HostGroup.objects.create(
            GroupName=request.POST["GroupName"],
            Note=request.POST["Note"],
        )
    return render(request, "am/addhostgroup.html")


# 更改主机分组
def change_host_group(request):
    if request.method == "POST":
        get_data = request.GET
        old_group_name = models.HostGroup.objects.filter(id=get_data["id"]).values("GroupName")[0]["GroupName"]
        models.HostAndHGroup.objects.filter(GroupName=old_group_name).update(GroupName=request.POST["GroupName"])
        models.HostGroup.objects.filter(id=get_data["id"]).update(
            GroupName=request.POST["GroupName"],
            Note=request.POST["Note"],
        )
        return HttpResponse('OK')


# 添加环境
def add_host_environment(request):
    if request.method == "POST":
        models.HostENV.objects.create(
            EnvName=request.POST["EnvName"],
            Note=request.POST["Note"],
        )
    return render(request, "am/addHostENV.html")


# 更改环境
def change_host_environment(request):
    if request.method == "POST":
        get_data = request.GET
        old_env_data = models.HostENV.objects.filter(id=get_data["id"]).values("EnvName")[0]["EnvName"]
        new_env_data = request.POST["EnvName"]
        models.HostENV.objects.filter(id=get_data["id"]).update(
            EnvName=request.POST["EnvName"],
            Note=request.POST["Note"],
        )
        if old_env_data != new_env_data:
            models.HostInfo.objects.filter(Environment=old_env_data).update(Environment=new_env_data)
        return HttpResponse('OK')


# 编辑功能
def edit(request):
    if request.method == "GET":
        get_data = request.GET
        for i in get_data.items():
            if i[0] == "hostGroup":
                data = models.HostGroup.objects.get(id=get_data["hostGroup"])
                return render(request, "am/editHostGroup.html", {"data": data})
            elif i[0] == "hostENVGroup":
                data = models.HostENV.objects.get(id=get_data["hostENVGroup"])
                return render(request, "am/editHostENV.html", {"data": data})
            elif i[0] == "host":
                data = models.HostInfo.objects.get(id=get_data["host"])
                server_name = get_host_name(get_data["host"])
                groups = models.HostAndHGroup.objects.filter(ServerName=server_name).values("GroupName")
                groups_list = []
                for group in groups:
                    groups_list.append(group["GroupName"])
                zabbix_data = models.HostInfo.objects.filter(id=get_data["host"]).values("Zabbix")
                salt_data = models.HostInfo.objects.filter(id=get_data["host"]).values("Salt")
                jumpserver_data = models.HostInfo.objects.filter(id=get_data["host"]).values("Jumpserver")
                keepass_data = models.HostInfo.objects.filter(id=get_data["host"]).values("Keepass")

                # 将获取的密码进行解密，再转换成str类型
                decrypt_password = (decrypt_str(get_password(get_data["host"]))).decode("UTF-8")

                return render(request, "am/editHost.html", {"data": data,
                                                            "envData": get_env_data(),
                                                            "hostGroupData": get_group_data(),
                                                            "usegroupdata": groups_list,
                                                            "ZabbixData": zabbix_data,
                                                            "SaltData": salt_data,
                                                            "JumpserverData": jumpserver_data,
                                                            "KeepassData": keepass_data,
                                                            "password": decrypt_password})
            else:
                return HttpResponse("请求错误")


# 册除功能
def delete(request):
    if request.method == "GET":
        get_data = request.GET
        for i in get_data.items():
            if i[0] == "hostGroup":
                models.HostGroup.objects.filter(id=get_data['hostGroup']).delete()
                return HttpResponse("删除成功")
            elif i[0] == "hostENVGroup":
                models.HostENV.objects.filter(id=get_data['hostENVGroup']).delete()
                return HttpResponse("删除成功")
            elif i[0] == "host":
                server_name = get_host_name(get_data['host'])
                models.HostAndHGroup.objects.filter(ServerName=server_name).delete()
                models.HostInfo.objects.filter(id=get_data['host']).delete()
                return HttpResponse("删除成功")
            else:
                return HttpResponse("请求错误")
